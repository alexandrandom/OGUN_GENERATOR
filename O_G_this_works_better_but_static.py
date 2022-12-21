import pandas as pd
import numpy as np
import random

#DEFINING VARIOUS SCORES
ects=np.arange(0,6.5,0.5).tolist()
ects.pop(0)
zaliczenie=["Zaliczenie na ocenę", "Egzamin", "Egzamin ustny", "Projekt w grupach", "Prezentacja multimedialna", "Esej"]
nieobecnosci=np.arange(0,3,1).tolist()

#READING SOURCE FILE AND DELETING UNUSED COLUMNS
df=pd.read_excel("source.xlsx")

df=df.iloc[:,2]

#DEFINING LOGICALLY SEPARATED WORD CHUNKS
listaw=[]
listaa=[]
lista_p=[]
lista_m=[]
lista_s=[]
listai=[]

whattosplitwith=[' w ', ' we ', ' a ', ',', ' - ', ' ', ' i ']
listy=[listaw,listaa,lista_p,lista_m,lista_s,listai]

for i in df:
    for splitterheh in whattosplitwith:
        try:
            lista=i.split(splitterheh)
            index=whattosplitwith.index(splitterheh)
            (listy[index]).append(lista)
        except:
            pass
#GENERATING NEW NAMES -- SECOND PART FIRST -- APPLYING LOGIC TO PREPOSITIONS WHEN EXTRACTING COMPONENTS
listaw1=[]
listaa1=[]
lista_p1=[]
lista_m1=[]
lista_s1=[]
listai1=[]

listy1=[listaw1,listaa1,lista_p1,lista_m1,lista_s1,listai1]
for lista in listy:
    for element in lista:
        if len(element)>1:

            index=listy.index(lista)
            (listy1[index]).append(element[-1])

#EXTRACTING THE BASE COMPONENT // FIRST PART OF A NEW NAME
wsad=[]
for lista in listy:
    for element in lista:
            wsad.append(element[0])
            if len(element)>1 and len(element)!=2:
                wsad.append(element[1])

#THIS WORKS BETTER, BUT IS USING ONLY ONE STATIC LIST INSTEAD OF CHOSING ONE FROM ALL OF THEM
#DYNAMIC VARIABLES!(TODO)
comp1=random.choice(wsad)
comp2=random.choice(listaw1)
comp3=random.choice(zaliczenie)
comp4=random.choice(ects)
comp5=random.choice(nieobecnosci)
print(f"{comp1} w {comp2}")

print(f"{comp4} ECTS. Sposób zaliczenia: {comp3}. Liczba nieobecności: {comp5}.")
