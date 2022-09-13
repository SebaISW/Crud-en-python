from argparse import _MutuallyExclusiveGroup
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from turtle import title


#Desarrollo de la interfaz grafica
root=Tk()
root.title('Prueba de interfaz app')
root.geometry("640x480")

miId = StringVar()
miNombre = StringVar()
miCargo = StringVar()
miSalario = StringVar()


def dbConnect():
    myCon = sqlite3.connect("base")
    miCur = myCon.cursor()

    try:
        miCur.execute('''
            CREATE TABLE empleado IF NOT EXIST (
            ID INTEGER PRIMARY KEY AUTOINCREMENT
            NOMBRE VACHAR(50) NOT NULL,
            CARGO VARCHAR(50) NOT NULL,
            SALARIO INT NOT NULL)
            ''')
        messagebox.showinfo("CONEXION", " Base de datos creada exitosamente")
    except:
        messagebox.showinfo("CONEXION", " Conexion exitosa con la base de datos")

def dbDelete():
    myCon = sqlite3.connect("bse")
    myCur = myCon.cursor()
    if messagebox.messagebox.askyesno(message = "Los datos se pederan definitvamente, ¿Desea Continuar?", title = "ADVERTENCIA"):
        myCur.execute("DROP TABLE empleado")


def exit():
    valor = messagebox.askquestion("Salir, Está seguro que desea salir?")
    if valor == "yes":
        root.destroy()

def clear():
    miId.set("")
    miNombre.set("")
    miCargo.set("")
    miSalario.set("")

def message():
    acerca = '''
    Aplicacion
    Version 1.0
    Running Python + sqlite3 + tkinter'''



#METODOS

def create():
    myCon = sqlite3.connect("base")
    myCur = myCon.cursor()
    try:
        datos = miNombre.get(),miCargo.get(),miSalario.get()
        myCur.execute('INSERT INTO empleado VALUES (NULL,?,?,?)'(datos))
        myCon.commit()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique conexion con BBDD")
        pass
clear()

def show():
    myCon = sqlite3.connect("base")
    myCur = myCon.cursor()
    reg = tree.get_children()
    for i in reg:
        tree.delete(i)
    
    try:
        myCur.execute("SELECT * FROM empleado")
        for row in myCur:
            tree.insert("",0,text=row[0], values=(row[1],row[2],row[3]))
    except:
        pass



#Tabla
tree = ttk.Treeview(height = 10, columns = ('#0' , '#1' , '#2'))
tree.place(x=0, y=130)
tree.column('#0', width=100)
tree.column('#1', width=200)
tree.column('#2', width=200)
tree.column('#3', width=100)
tree.heading('#0', text="ID", anchor=CENTER)
tree.heading('#1', text="Nombre", anchor=CENTER)
tree.heading('#2', text="Cargo", anchor=CENTER)
tree.heading('#3', text="Salario", anchor=CENTER)

def update():
    myCon = sqlite3.connect("base")
    myCur = myCon.cursor()
    try:
        dat = miNombre.get(),miCargo.get(),miSalario.get()
        myCur.execute("UPDATE empleado SET NOMBRE=?, CARGO=?, SALARIO=? WHERE ID=" + miId.get(), (dat))
        myCon.commit()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un error al modificar el registro")
        pass

def delete():
    myCon = sqlite3.connect("base")
    myCur = myCon.cursor()
    try:
        if messagebox.messagebox.askyesno(message="Realmente desea elimina el registro?", title="ADVERTENCIA"):
            myCur.execute("DELETE FROM empleado WHERE ID=" + miId.get())
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al tratar de eliminar el registro")
        pass
    clear()
    show()
# Añadimos los elementos

menubar=Menu(root)
dbMenu=Menu(menubar,tearoff=0)
dbMenu.add_command(label="Crear/Conectar Base de Datos", command=dbConnect)
dbMenu.add_command(label="Eliminar Base de Datos", command=delete)
dbMenu.add_command(label="Salir", command=exit)
menubar.add_cascade(label="Inicio", menu=dbMenu)

#Esto es una modificacion muy modificada

root.mainloop()