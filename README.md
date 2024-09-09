# Api Rest en Python con el Framework de Flask - CRUD MUY BÁSICO

Una vez instalado Python en tu equipo (lo puedes obtener aquí: https://www.python.org/downloads/) , es necesario seguir los siguientes pasos para ejecutar el proyecto:

**Creación de Entorno Virtual de Python**

1. Instala el modulo venv de python

```
pip install virtualenv
```

2. Descarga y descomprime la carpeta del proyecto y abrela en VSCODE (preferiblemente)
3. Una vez ingresado en el IDE, abre una terminal powershell (preferiblemente) en VSCODE, puedes usar el comando CTRL+SHIFT+Ñ, posteriormente ingresa este comando para crear el entorno virtual. 

```
py -m venv env
```
Es preferible crearlo con el nombre "env".

4. Inicia el entorno virtual

```
/env/Scripts/activate
```
Los puedes desactivar con ``` deactivate ```

**Instalación de FLASK**

Instalaremos el framework de Flask, además de la libreria para la conexión con MYSQL, en una terminal ejcuta:

```
pip install flask flask_mysqldb
```

**Conexión a Base de Datos**

El proyecto ya viene preconfigurado para una conexión con MYSQL, lo unico que debes hacer es cambiar los siguientes atributos segun tu necesidad. Reomendable utilizar XAMPP O WAMPP. 
   
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'api_flask'

**RECUERDA IMPORTAR O CREAR LA BASE DE DATOS**

Finalmente ejecuta el proyecto:
```
  py src/app.py
```
