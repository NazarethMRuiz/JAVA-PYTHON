#LIBRERIAS
import requests

#CLASE - ARCHIVO
class Empoyee:
    def mostrar(self):
            self.archivo = open("Python_p2\Files\employee.txt", "r", encoding="utf-8")
            lista = self.archivo.read().split('\n')
            empleado1 = lista[0].split(sep=', ')
            
            
            diccionarioEmpleado1 = {"firstname": empleado1[0],"surname": empleado1[1],
                                    "country":{"name": empleado1[2],
                                                "airports": [{"name":empleado1[2]}]},
                                    "languageName": [{"name": empleado1[3]}]}  
            
            resp1 = requests.post('http://localhost:8080/apiv1/employee/add', json=diccionarioEmpleado1)

            print(resp1)
            print(resp1.json())
            
            return diccionarioEmpleado1

#BLOQUE
p=Empoyee()
p.mostrar()