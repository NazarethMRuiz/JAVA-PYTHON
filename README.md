# PYTHON
Segundo examen - Parte dos 

Funcionamiento general

Este programa generar registros a la base de datos H2 dentro de un proyecto de Spring, de esta forma la API recibe un conjunto de datos por medio de JSON para poder hacer los dentro de registros de la tabla.

Pasos para la ejecucición. 

# REQUERIMIENTOS GENERALES
Es necesario contar con lo siguiente: 

* Visual Studio Code.
* Python 3 o superior.
* Git.
* Spring 5.
* Java 8.
* H2 Database
* Spring Web

# REQUERIMIENTOS - PYTHON:
* Libreria Request: 
Ejecute en conlo el siguiente comendo
* pip install requests

# INSTALACIÓN
Para Spring unicamente la dependencia en el pom:

<dependency>
			<groupId>com.h2database</groupId>
			<artifactId>h2</artifactId>
			<scope>runtime</scope>
</dependency>


# CONFIGURACIÓN

Se debe ejecutar el proyecto de tipo Spring, mediante el cual ejecutamos el servidor en la siguiente dirección local: http://localhost:8080/apiv1/employee/add 
Mediante el archivo de Python, se obtendrá el JSON que servirá como cuerpo de la petición que será recibido por la aplicación de Spring, los datos se mostraran dentro de la Base de Datos (H2) http://localhost:8080/h2-console. 
 



