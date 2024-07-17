import os
import sys
sys.path.append('C:\\Users\\Dairm\\PycharmProjects\\ControladorReconocimientoFacial\\.venv\\Espejo\\Clases')

from Clases.Login import Login
from Clases.Menu import Menus
from Clases.Opciones import opcionesMenu

menus = Menus()
login = Login()

m = menus.login_menu()
booleana = False
booleana = login.elegir_metodo(m)
print(booleana)

if booleana == True or booleana == None:
    n = menus.menu()
    opciones = opcionesMenu()
    opciones.opcion(n)
