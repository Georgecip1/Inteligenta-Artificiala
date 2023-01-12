import requests
from bs4 import BeautifulSoup
import pandas as pd


req = requests.get('https://www.turistinfo.ro/busteni/cazare-hoteluri-vile-pensiuni-busteni.html')
soup = BeautifulSoup(req.text, "html.parser")
cazare = []
for nume in soup.find_all('span',{'itemprop' : 'name'}):
    cazare.append(nume.text.strip())
    
cazare = list(filter(lambda k: 'Cazare' not in k, cazare))


recenzii = []
for rating in soup.find_all('div', {'class' : 'ucrecenzii valign-wrapper'}):
    recenzii.append(rating.text.strip())
recenzii = [elem.replace("question_answer \xa0 ", '') for elem in recenzii]

pret = []
for p in soup.find_all('div', {'itemprop' : 'priceRange' }):
    pret.append(p.text)
    
# d = {'Nume Hotel': cazare, 'Recenzii': recenzii, 'Pret': pret}


    f = open("output_cazari.txt", "w", encoding="utf-8")
zip(cazare, recenzii, pret)
for (a,b,c) in zip(cazare, recenzii, pret):
    # print (a ,b ,c)
    f.write("Nume Cazare: " + str(a) + "\n")
    f.write("Recenzii: " + str(b) + "\n")
    f.write("Pret: " + str(c) + "\n")
    f.write("\n")



