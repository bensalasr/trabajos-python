import csv

estudiantes= {}

def agregar(nombre,apellido,nota1,nota2,nota3):  
    estudiantes.update({"nombre":nombre,"apellido":apellido,"nota1":nota1,"nota2":nota2,"nota3":nota3,"nota4":nota4}) 

def promedio(nota1,nota2,nota3,nota4):
    promedio=(nota1+nota2+nota3+nota4)/4
    return promedio

def mostrar(estudiantes):
     if not estudiantes in estudiantes:
          print("pss no hay")
     for estudiantes in estudiantes:
        print(nombre,apellido,nota1,nota2,nota3,nota4,promedio)

def export():
    if not estudiantes:
         print("no hay para exportar")
         return
nombre_del_Archivo=input("ingrese nombre de archivo(sin csv)") + ".csv"
for estudiante in estudiantes:
    writer.writerow(["nombre","apellido","nota1","nota2","nota3","nota4"])

def menu():
    print("1. agregar estudiantes")
    print("2. ver todos los alumnos")
    print("3. buscar por rut")
    print("4. exportar a csv")

opcion=input("ingrese una opcion")

if opcion =="1":
        nombre=input("ingrese nombre ")
        apellido=input("ingrese apellido ")
        nota1=float(input("ingrese nota1 "))
        nota2=float(input("ingrese nota2 "))
        nota3=float(input("ingrese nota3 "))
        nota4=float(input("ingrese nota4 ")) 
        agregar(nombre,apellido,nota1,nota2,nota4)
elif opcion == "2":
      mostrar(estudiantes)

menu()
