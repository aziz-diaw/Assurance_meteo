import pandas as pd
######## extraction des données Xslx
def extraction(name):
    chemin = r"C:\Users\user\Desktop\Assurance_meteo\data"
    chemin += "/" + str(name) + ".xlsx"
    fichier = pd.read_excel(chemin)
    liste = []
    for k in range (0,21):
        valeur = 2001 + k
        liste+= [fichier[valeur].tolist()]
    return liste


### calcul de la prime sur une seule année
def primefirst(liste,pivot,cout_fixe):
    for k in range (0,len(liste)):  ## on s'arrete à -1 à cause des valeurs Nan
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
         S = S + primefirst(liste[20-i],pivot,cout_fixe)
     return S/5

def resultats_non_ass(liste,ca,cout_fixe,pivot):   ## les résultats sur une année quelconque en non assurée
    for k in range (0,len(liste)):
        if (float(liste[k]) > pivot):
            liste[k] = -cout_fixe
        elif (0<float(liste[k])  and float(liste[k])< pivot):
            liste[k]= ((pivot - float(liste[k]))/pivot)*ca
        else:
            liste[k]= ca
    return sum(liste)


def resultas_non_ass_ville(name,annee,ca,cout_fixe,pivot):   ## les résultats sur une année précise pour une entreprise non assurée
    liste = extraction(name)
    periode=[]
    valeur =  int(annee) - 2001  ## sa position
    periode += liste[valeur]
    return resultats_non_ass(periode,ca,cout_fixe,pivot)


def prime_periode(name, pivot, cout_fixe,periode): ## le calcul de la prime sur la période pour pouvoir faire l'analyse rétro
    liste = extraction(name)
    S=0
    valeur = int(periode) - 2001  ## position de l'année d'analyse rétrospective sur la liste des années
    for k in range (0,5):
        S = S + primefirst(liste[valeur-k], pivot, cout_fixe)

    return (S/valeur)


def resultats_ass(liste,ca,cout_fixe,pivot):   ## les résultats sur une année en assuré
    for k in range (0,len(liste)):
        if (float(liste[k]-1) > pivot):
            liste[k] = 0  ## car on lui rembourse ses couts fixes
        elif (0<float(liste[k])  and float(liste[k])< pivot):
            liste[k]= ((pivot - float(liste[k]))/pivot)*ca
        else:
            liste[k]= ca
    return sum(liste)


def resultas_ass_ville(name,annee,ca,cout_fixe,pivot):
    liste = extraction(name)
    periode = []
    valeur = int(annee) - 2001  ## sa position
    periode += liste[valeur]
    return resultats_ass(periode, ca, cout_fixe, pivot)










