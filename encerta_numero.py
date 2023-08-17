#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
import random

# Variables:
nom_usuari = input('Hola! Quin és el teu nom? ')
intents = 0
numero = random.randint(1, 20)

# Execució

print (f'Benvingut/da {nom_usuari}, estic pensant en un nombre entre 1 i 20, podries endevinar-lo en un màxim de 6 intents?')

# Bucle o repetició:
while intents < 6:
    estimacio = int(input('Prova sort... '))
    intents = intents + 1
    
    if estimacio > numero:
        print ('La teva estimació és alta.')
    if estimacio < numero:
        print ('La teva estimació és baixa.')
    if estimacio == numero:
        print(f'Enhorabona! Has aconseguit endevinar el número en {intents} intents.')
        break
else:
    print('No hi ha hagut sort!')