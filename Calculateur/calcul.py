import csv;


def extraction(name):
  ## extraction du bon csv en fonction de la ville
    chemin=r"C:\Users\user\Desktop\Imafa\Assurance_meteo\data"
    chemin+="/"+str(name) + "csv"

    f= open (r"C:\Users\user\Desktop\Imafa\Assurance_meteo\data/nice.csv")
    liste=[]
    myReader = csv.reader(f)
    for row in myReader:
        liste+=row
    return liste

extraction("nice")

## split
## division en année:
    ##annee1=liste[0:365]
   ## annee2= liste[]


def primefirst(liste,pivot,cout_fixe):
    for k in range (0,len(liste)):
        if (float(liste[k]) > pivot):
            liste[k] = cout_fixe
        else:
            liste[k] = 0
    return sum(liste)


def prime(name,pivot,cout_fixe):
     liste= extraction(name)
     annee1=liste[0:365]
     annee2=liste [365: 730]
     annee3=liste [730 : 1095]
     annee4 = liste [1095 : 1461]
     annee5 = liste [1461 : 1826]
     print (annee2)

     return (primefirst(annee5,pivot,cout_fixe)+primefirst(annee1,pivot,cout_fixe)+ primefirst(annee2,pivot,cout_fixe)+ primefirst(annee3,pivot,cout_fixe)+primefirst(annee4,pivot,cout_fixe))/5


print(prime("nice",20,1000))







