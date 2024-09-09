from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from config import config

app=Flask(__name__)

conexion = MySQL(app)

@app.route('/cursos', methods=['GET'])
def obtener_todo():
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM cursos"
        cursor.execute(sql)
        datos=cursor.fetchall()
        cursos=[]
        for fila in datos:
            curso={'codigo': fila[0], 'nombre': fila[1], 'creditos':fila[2]}
            cursos.append(curso)
        return jsonify({'cursos': cursos, 'mensaje': "Cursos Listados."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"}), 404

def curso_db(codigo):
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM cursos WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            curso={'codigo': datos[0], 'nombre': datos[1], 'creditos':datos[2]}
            return curso
        else:
            return None
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/cursos/<codigo>', methods=['GET'])
def obtener_curso(codigo):
    try:
        curso = curso_db(codigo)
        if curso != None:
            return jsonify({'cursos': curso, 'mensaje': "Curso Encontrado."})
        else:
            return jsonify({'mensaje': "Curso NO Encontrado."}), 404
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/cursos', methods=['POST'])
def agregar_curso():
    try:
        curso = curso_db(request.json['codigo'])
        if curso == None:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO cursos (codigo, nombre, creditos) 
                    VALUES ('{0}','{1}',{2})""".format(request.json['codigo'], request.json['nombre'], request.json['creditos'])
            cursor.execute(sql)
            conexion.connection.commit() #CONFIRMAR!
            return jsonify({'mensaje': "Curso Creado."})
        else:
            return jsonify({'mensaje': "Curso NO Creado, dado que ya existe el id: " + request.json['codigo']})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/cursos/<codigo>', methods=['PUT'])
def actualizar_curso(codigo):
    try:
        curso = curso_db(codigo)
        if curso != None:
            cursor = conexion.connection.cursor()
            sql = """UPDATE cursos SET nombre = '{0}', 
            creditos = {1} """.format(request.json['nombre'], request.json['creditos'],codigo)
            cursor.execute(sql)
            conexion.connection.commit() #CONFIRMAR!
            return jsonify({'mensaje': "Curso Actualizado."})
        else:
            return jsonify({'mensaje': "Curso NO Actualizado, dado que NO existe el id: " + codigo })
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/cursos/<codigo>', methods=['DELETE'])
def eliminar_curso(codigo):
    try:
        curso = curso_db(codigo)
        if curso != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM cursos WHERE codigo = '{0}'".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit() 
            return jsonify({'mensaje': "Curso Eliminado."})
        else:
            return jsonify({'mensaje': "Curso NO Eliminado, NO existe."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


def error_not_found(error):
    return "<h1>La pagina no existe...</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, error_not_found)
    app.run()