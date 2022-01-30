import csv

######## extraction des données CSV
def extraction(name):
  ## extraction du bon csv en fonction de la ville
    chemin=r"C:\Users\user\Desktop\Assurance_meteo\data"
    chemin+="/"+str(name) + ".csv"
    liste_annee=[]
    f= open(chemin)
    liste=[]
    myReader = csv.reader(f)
    for row in myReader:
        liste+=row
    annee1 = liste[0:365]
    annee2 = liste[365:730]
    annee3 = liste[730:1095]
    annee4 = liste[1095:1461]
    annee5 = liste[1461:1826]
    liste_annee +=[annee1,annee2,annee3,annee4,annee5]
    return liste_annee


### calcul de la prime sur une année
def primefirst(liste,pivot,cout_fixe):
    for k in range (0,len(liste)):
        if (float(liste[k]) > pivot):
            liste[k] = cout_fixe
        else:
            liste[k] = 0
    return sum(liste)


#### calcul de la prime sur une profondeur de 5 ans et moyennisation donc on prend les 5 derniéres années qui précédent 2022
def prime(name,pivot,cout_fixe):
     liste= extraction(name)
     S=0
     for i in range(0,5):
         S = S + primefirst(liste[i],pivot,cout_fixe)
     return S/5



def resultats_non_ass(liste,ca,cout_fixe,pivot):   ## les résultats sur une année
    for k in range (0,len(liste)):
        if (float(liste[k]) > pivot):
            liste[k] = -cout_fixe
        elif (0<float(liste[k])  and float(liste[k])< pivot):
            liste[k]= ((pivot - float(liste[k]))/pivot)*ca
        else:
            liste[k]= ca
    return sum(liste)


def resultas_non_ass_ville(name,annee,ca,cout_fixe,pivot):  ## on s'arréte en 2018 pour pouvoir au moins calculer la prime pour cette année en fonction d'une année restanre (2017)
    liste = extraction(name)
    periode=[]
    valeur = 2021 - int(annee)
    periode += liste[len(liste)-valeur]
    return resultats_non_ass(periode,ca,cout_fixe,pivot)


def prime_periode(name, pivot, cout_fixe,periode):
    liste = extraction(name)
    S=0
    valeur = int(periode) - 2017    ## car nos données s'arrétent à 2017
    for k in range (0,valeur):
        S = S + primefirst(liste[k], pivot, cout_fixe)

    return (S/valeur)


def resultats_ass(liste,ca,cout_fixe,pivot):   ## les résultats sur une année
    for k in range (0,len(liste)):
        if (float(liste[k]) > pivot):
            liste[k] = 0  ## car on lui rembourse ses couts fixes
        elif (0<float(liste[k])  and float(liste[k])< pivot):
            liste[k]= ((pivot - float(liste[k]))/pivot)*ca
        else:
            liste[k]= ca
    return sum(liste)


def resultas_ass_ville(name,annee,ca,cout_fixe,pivot):  ## on s'arréte en 2018 pour pouvoir au moins calculer la prime pour cette année en fonction d'une année restanre (2017)
    liste = extraction(name)
    periode=[]
    valeur = 2021 - int(annee)
    periode += liste[len(liste)-valeur]
    return resultats_ass(periode,ca,cout_fixe,pivot)










