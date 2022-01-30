import csv

######## extraction des données CSV
def extraction(name):
  ## extraction du bon csv en fonction de la ville
    chemin=r"C:\Users\user\Desktop\Assurance_meteo\data"
    chemin+="/"+str(name) + ".csv"

    f= open(chemin)
    liste=[]
    myReader = csv.reader(f)
    for row in myReader:
        liste+=row
    return liste

### calcul de la prime sur une année
def primefirst(liste,pivot,cout_fixe):
    for k in range (0,len(liste)):
        if (float(liste[k]) > pivot):
            liste[k] = cout_fixe
        else:
            liste[k] = 0
    return sum(liste)


#### calcul de la prime sur une profondeur de 5 ans et moyennisation
def prime(name,pivot,cout_fixe):
     liste= extraction(name)
     annee1=liste[0:365]
     annee2=liste[365:730]
     annee3=liste[730:1095]
     annee4=liste[1095:1461]
     annee5=liste[1461:1826]

     return (primefirst(annee5,pivot,cout_fixe)+primefirst(annee1,pivot,cout_fixe)+ primefirst(annee2,pivot,cout_fixe)+ primefirst(annee3,pivot,cout_fixe)+primefirst(annee4,pivot,cout_fixe))/5

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
    annee1 = liste[0:365]
    annee2 = liste[365:730]
    annee3 = liste[730:1095]
    annee4 = liste[1095:1461]
    annee5 = liste[1461:1826]
    periode=[]
    if(annee=="2021"):
        periode = annee5
    elif (annee == "2020"):
        periode = annee4
    elif (annee == "2019"):
        periode = annee3
    elif (annee == "2018"):
        periode = annee2

    return resultats_non_ass(periode,ca,cout_fixe,pivot)


def prime_periode(name, pivot, cout_fixe,periode):
    liste = extraction(name)
    annee1 = liste[0:365]
    annee2 = liste[365:730]
    annee3 = liste[730:1095]
    annee4 = liste[1095:1461]
    annee5 = liste[1461:1826]
    if periode =="2021":
        return ( primefirst(annee1, pivot, cout_fixe) + primefirst(annee2, pivot, cout_fixe) + primefirst(annee3, pivot, cout_fixe) + primefirst(annee4, pivot, cout_fixe)) / 4
    if periode =="2020":
        return ( primefirst(annee1, pivot, cout_fixe) + primefirst(annee2, pivot,cout_fixe) + primefirst(annee3, pivot, cout_fixe) ) / 3
    if periode =="2019":
        return ( primefirst(annee1, pivot, cout_fixe) + primefirst(annee2, pivot,  cout_fixe)  ) / 2
    if periode =="2018":
        return ( primefirst(annee1, pivot, cout_fixe))


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
    annee1 = liste[0:365]
    annee2 = liste[365:730]
    annee3 = liste[730:1095]
    annee4 = liste[1095:1461]
    annee5 = liste[1461:1826]
    periode=[]
    if(annee=="2021"):
        periode = annee5
    elif (annee == "2020"):
        periode = annee4
    elif (annee == "2019"):
        periode = annee3
    elif (annee == "2018"):
        periode = annee2

    return resultats_ass(periode,ca,cout_fixe,pivot)










