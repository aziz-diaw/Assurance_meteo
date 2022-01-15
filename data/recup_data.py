
from calendar import month
from tkinter.ttk import Style
from bs4 import BeautifulSoup
import requests
from csv import writer


#years = ["2017","2018","2019","2020","2021"]
years = ["2019","2020","2021"]
months = ["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
#months = ["janvier"]
towns = ["nice-cote-d-azur"]

def extraction_donnes(month,year,town) -> list[list[str]]:
    url = f"https://www.infoclimat.fr/climatologie-mensuelle/07690/{month}/{year}/{town}.html"
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
            # date2 = removeSpaces(date)
            # print(date.text)
            
        except:
            pass

        try:
            newList = lists.find_all("td")
            newList2 = newList[2].find_all("span")
            precipitation = newList2[1].text
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


def data(name_file:str,year:str,towns:list[str]):
    info = []
    for month in months:
        info.extend(extraction_donnes(month,year,towns[0]))
    with open(f'data/{name_file}.csv', 'w', encoding='utf8', newline='',) as f:
        thewriter = writer(f)
        header = ['Date', "Nice"]
        thewriter.writerow(header)
        thewriter.writerows(info)

if __name__ == "__main__":
    for year in years:
        name_file = f"nice_{year}"
        data(name_file,year,towns)