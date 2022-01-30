from tkinter.ttk import Style
from bs4 import BeautifulSoup
import requests
from csv import writer

from sklearn.neighbors import NearestCentroid


years = ["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]

months = ["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
towns = [["07156","paris-montsouris"],["07650","marseille-marignane-marseille-provence"],["07015","lille-lesquin"],["07690","nice-cote-d-azur"]]

def extraction_donnes(month,year,town) -> list[list[str]]:
    url = f"https://www.infoclimat.fr/climatologie-mensuelle/{town[0]}/{month}/{year}/{town[1]}.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    # l'objet soup, retourne la page html choisit
    lists2 = soup.find("tbody")
    newList = lists2.find_all("tr")
    temp = []
    info = []
    for lists in newList:
        try:
            newList = lists.find_all("a",class_="tipsy-trigger-right")
            newList2 = lists.find_all("span")
            date = newList[2].text.replace('\n','')           
        except:
            pass
        try:
            newList = lists.find_all("td")
            newList2 = newList[2].find_all("span")
            precipitation = newList2[1].text.replace(".",",")
            #precipitation = int(precipitation)
        except:
            pass
        
        temp.append([date,precipitation])
    
    # supression des doublons
    info.append(temp[0])
    for j in range(1,len(temp)):
        info.append(temp[j])
        if temp[j][0] == temp[j-1][0]:
            info.remove(temp[j])
    #remplaceJourParMois(info,month)
    return info

def data(name_file:str,year:str,town:list[str]):
    info = []
    for month in months:
        info.extend(extraction_donnes(month,year,town))
    with open(f'data/{name_file}', 'w', encoding='utf8', newline='',) as f:
        thewriter = writer(f)
        header = ['Date', name_file] 
        thewriter.writerow(header)
        thewriter.writerows(info)

if __name__ == "__main__":
    for town in towns:
        name = town[1].split("-")[0]
        for year in years:
            name_file = f"{name}_{year}.csv"
            data(name_file,year,town)
