#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero = open("/etc/passwd",'r')
lista_usuarios = {}

while 1:
    lineas = fichero.readline()
    argumentos = lineas.split(":")
    ##usuario = argumentos[0]
    ##shell = argumentos[-1]
    ##print usuario,shell[:-1]
    lista_usuarios[argumentos[0]] = argumentos[-1][:-1]
    if not lineas:
        break

fichero.close()
fichero = open("/etc/passwd",'r')
print "\nHay", len(fichero.readlines()), "usuarios\n"
fichero.close()

try:
    print "Usuario root:",lista_usuarios["root"]
    print "Usuario imaginario:",lista_usuarios["imaginario"]
except KeyError: #elevamos la excepción en el caso de que sea imaginario para que no salga el error por pantalla
    print "El usuario no se ha encontrado en la lista de usuarios\n"
