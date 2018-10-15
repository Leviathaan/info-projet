# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:58:01 2018

@author: etudiant
"""
import csv

with open('donnees_projet','r') as f : ### importer la liste que nous voulons étudier
    reader = csv.reader(f)
    your_list = list(reader)

liste = [[float(your_list[i][j])for j in range(len(your_list[i]))]for i in range (1,len(your_list))]
## transformer les chaines de caractère dans la liste mise à part la première colonne 


plafond_note = your_list[0]
print(plafond_note)
plafond_note1 = [float(plafond_note[i])for i in range (len(plafond_note)-1)] ##première colonne de 
##la liste transofrmé en chiffre sans validation

#################### Programme 1

s=sum(plafond_note1)
minimum=s/2 ##valeur minimum à avoir si on veut valider l'UE

def somme_note (l,ligne): ## somme de une ligne de chaque élève
    x=0 ## variable égale à la somme des chiffres d'une liste
    for i in range(len(l[ligne])-1):
        x += l[ligne][i]
    return x

def validation (l): ## somme de chaque ligne
    liste_validation=[]
    somme_colonne=0
    for i in range (len(l)):
        somme_colonne = somme_note(l,i)
        liste_validation.append(somme_colonne)
    return liste_validation

####################### Programme 2
mini_colonne = [] ## liste dans laquelle on met la moyenne à avoir pour chaque colonne
x=0
for i in range(len(plafond_note1)):
    x=plafond_note1[i]/2
    mini_colonne.append(x)



def comparaison_ligne (l): ## 
    nombre_UE_valide = []
    ligne = 0
    nombre_valide = 0
    for i in range (len(l)):
        ligne = l[i]
        nombre_valide = 0
        for j in range (len(ligne)-1):
            if ligne[j] >= mini_colonne[j]:
                nombre_valide +=1
        nombre_UE_valide.append(nombre_valide)
    return nombre_UE_valide

nombre_UE_valide = comparaison_ligne(liste)

def validation_possible (l,nombre_UE_ok):
    validation_propose =[]
    for i in range (len(l)):
        if l[i]>= nombre_UE_ok :
            validation_propose.append(1)
        else :
            validation_propose.append(0)
    return validation_propose

validation_propose3= validation_possible (nombre_UE_valide,3)

validation_liste=[]
for i in range(len(liste)):
    validation_liste.append(liste[i][4])

###if len(validation_propose) == len(validation_liste) : # pernet de voir si les deux listes de même taille
   ## print('vrai')


def comparer_validations (liste_un,liste_deux):
    for i in range (len(liste_un)):
        if liste_un[i]==liste_deux[i]:
            resultat ='bon'
        else: 
            resultat='faux'
    return resultat
 
validation_propose2=0   
        
if comparer_validations(validation_propose3,validation_liste)=='faux':
    validation_propose2=validation_possible(nombre_UE_valide,2)
    print(comparer_validations(validation_propose2,validation_liste))
    


        
########### Les fonctions utilisables ######
     
# x = float(your_list[1][0]) ## permet de transformer une chaine de caractère en chiffre
# liste = [[float(liste[i][j])for j in range(len(list[i]))]for i in range (len(list))] ## permet
## de transformer toutes les chaine de caractères en chiffre pour les liste de liste
# l[0][i] : la ligne 0 et les colonnes de la ligne 0
# len(l[0]) : les termes de la ligne 0 = première liste dans liste des listes