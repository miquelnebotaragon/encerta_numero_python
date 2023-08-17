<h1 align="center"><b>Joc. Encerta el número</b></h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">
    <img alt="License: GPL--3+" src="https://img.shields.io/badge/License-GPL--3+-yellow.svg" />
  </a>
  <a href="https://twitter.com/miquelnebot" target="_blank">
    <img alt="Twitter: Miquel Nebot" src="https://img.shields.io/twitter/follow/miquelnebot.svg?style=social" />
  </a>
</p>
<div align="center"><img src="https://github.com/miquelnebotaragon/endevina_numero/assets/57944755/d8f0cc43-c2b2-4202-bb0c-97c1fa3ac541"></div>


# 👁️‍🗨️ Introducció
Aprenem jugant. Pràctiques amb Python.

# 💻 Escenari
Debian GNU/Linux 12 (bookworm) x86_64

# 0️⃣ Abans de començar
1. Haurem de tenir instal·lat Python en el nostre ordinador. Verificarem si disposam d'aquest programari i la seva versió mitjançant la instrucció següent a dins el Terminal (Ctrl+Alt+T): 

```console
user@debian-mnebot:~$ sudo python3 -V
```
Si no el tenim instal·lat, el podem aconseguir fàcilment teclejant:
```console
user@debian-mnebot:~$ sudo apt install python3
```
2. Per a la importació del mòdul necessari (**random**) és imprescindible disposar al nostre ordinador de l'administrador de paquets **PIP**, per això, i si no ho hem fet amb anterioritat, l'instal·larem a través de la terminal de la següent manera:
```console
user@debian-mnebot:~$ sudo apt install python3-pip
```
3. Instal·larem, finalment, el mòdul necessari:
```console
user@debian-mnebot:~$ sudo pip install random
```

# 👇 Descàrrega i execució
Copiarem el codi següent 👇 a un arxiu amb extensió **.py** al nostre ordinador (per exemple **encerta_numero.py**).
<p></p>📝 Descàrrega de l'arxiu .py des d'<a href="https://github.com/miquelnebotaragon/encerta_numero/blob/main/encerta_numero.py" target="_blank">aquí</a>.

# 🏆 Vull saber-ne més
Desglossant el codi:
## Part 1:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
import random

```
Aquesta és la part inicial i més senzilla:
<p>· Enumeram els mòduls a importar, en aquest cas només un, random.</p>


```python

# Variables:
nom_usuari = input('Hola! Quin és el teu nom? ') 
intents = 0 # Establim a zero el nombre inicial d'intents... anirà pujant com veurem a continuació.
numero = random.randint(1, 20) # Feim treballar el módul "random" generant un nombre aleatori entre 1 i 20 d'aquesta manera.

```

<p>· Mostram en pantalla un text on sol·licitam a l'usuari que escrigui el seu nom.</p>
<p>· La segona variable s'encarregarà de fixar el nombre d'intents inicial a zero. Ja veurem a continuació com es va incrementant aquest valor.</p>
<p>· Finalment, feim treballar el mòdul "random" generant un nombre aleatori entre 1 i 20.

## Part 2:
```python

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


```

· Finalment procedim a l'execució del programa imprimint en pantalla un missatge de benvinguda per a l'usuari i sol·licitant que intenti endevinar el número en menys de 6 intents.  

El programa, mitjançant una estructura de control de fluxe iterativa (_while_), anirà repetint el bucle analitzant les condicions proposades. Si s'arriba al nombre màxim d'intents, bota directament a la funció _print_ situada a dins l'estructura _else_.

# ➕ Informació
1️⃣ L'arxiu **.py** ha estat comentat al detall (#) per tal de possibilitar l'anàlisi del seu funcionament.<p></p>
2️⃣ Aquesta aplicació ha estat creada únicament amb finalitat d'estudi i divulgació. No em faig responsable dels possibles problemes ni prejudicis que pugui provocar el seu ús.
