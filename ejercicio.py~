#!/usr/bin/python
# -*- coding: utf-8 -*-

# hola, hola

fd = open('/etc/passwd', 'r')

lineas = fd.readlines()
fd.close()

for linea in lineas:
    elementos = linea.split(':')
    print elementos[0], elementos[-1][:-1]
