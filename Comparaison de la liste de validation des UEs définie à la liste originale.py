# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:03:26 2018

@author: etudiant
"""

import csv

with open('donnees_projet','r') as f : ### importer la liste que nous voulons Ã©tudier
    reader = csv.reader(f)
    your_list = list(reader)

liste = [[float(your_list[i][j])for j in range(len(your_list[i]))]for i in range (1,len(your_list))]
## transformer les chaines de caractÃ¨re dans la liste mise Ã  part la premiÃ¨re colonne 

plafond_note = your_list[0]
plafond_note1 = [float(plafond_note[i])for i in range (len(plafond_note)-1)] ##premiÃ¨re colonne
s=sum(plafond_note1)
minimum=s/2 ##valeur minimum Ã  avoir si on veut valider l'UE

print(minimum)



def somme_note (l,ligne): ## somme de une ligne 
    x=0
    for i in range(len(l[x])-1):
        x += l[x][i]
    return x

########### Les fonctions utilisables ######
     
# x = float(your_list[1][0]) ## permet de transformer une chaine de caractÃ¨re en chiffre
# liste = [[float(liste[i][j])for j in range(len(list[i]))]for i in range (len(list))] ## permet
## de transformer toutes les chaine de caractÃ¨res en chiffre pour les liste de liste
# l[0][i] : la ligne 0 et les colonnes de la ligne 0
# len(l[0]) : les termes de la ligne 0 = premiÃ¨re liste dans liste des listes



#Je veux comparer la liste de validations des UEs que nous avons définie à la liste originale
    
import numpy as np

liste=np.array(liste)
validation = liste[:,4]
liste_de_validation_créée=[]
x=0
for i in range(len(liste[x])):
    if liste_de_validation_créée[i]!=liste[i]:
        print("La validation par somme des matières n'est pas valable")

        
    
    
    
        















