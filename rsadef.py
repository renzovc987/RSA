from decimal import Decimal 
import random
import sys
import numpy as np
import string  

def pre_procesar(mensaje):
    tildes = ['á', 'é', 'í', 'ó', 'ú']
    tildes_cambio = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(tildes)):
        mensaje = mensaje.replace(tildes[i], tildes_cambio[i])
    mensaje = mensaje.upper()
    mensaje = (mensaje.strip().replace(" ", ""))
    translator = str.maketrans('', '', string.punctuation)
    mensaje = mensaje.translate(translator)
    mensaje = mensaje.replace("…", "")
    mensaje = mensaje.replace("¡", "")
    mensaje = mensaje.replace("\n", "")
    return mensaje


def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b)


def crifrarssa(a,p,q):
    abecedario2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    no = a
    no = no.upper()
    c=0
    for i in abecedario2:
        c = c + 1
        if i == no:
            break
        
    no = c
    n = p*q 
    t = (p-1)*(q-1) 
    
    for e in range(2,t): 
        if gcd(e,t)== 1: 
            break
    for i in range(1,10): 
        x = 1 + i*t 
        if x % e == 0: 
            d = int(x/e) 
            break
    ctt = Decimal(0)
    ctt =pow(no,e)
    ct = ctt % n
    if ct>26:
        c1=ct%26
    else:
        c1=ct
    
    
    dtt = Decimal(0) 
    dtt = pow(ct,d)
    dt = dtt % n
    if dt>26:
        d1=dt%26
    else:
        d1=dt

    return abecedario2[c1-1] , abecedario2[d1-1], d,e,n



mensaje = str(input("Ingrese el mensaje : "))
texto = ["", ""]
texto = pre_procesar(mensaje)

p = int(input("p: "))
q = int(input("q: "))

c3=""
c4=""

for i in texto:
    c1,c2,d,e,n = crifrarssa(i,p,q)
    c3=c3+c1
    c4=c4+c2

print("Clave privada","(",d,",",n,")")
print("Clave pública","(",e,",",n,")")  
print("Escribe Cifrado      :",c3)
print("Escribe Descrifrado  :",c4)