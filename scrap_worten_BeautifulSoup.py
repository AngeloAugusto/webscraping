from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from unidecode import unidecode
from time import strftime, gmtime
import webbrowser
import os
import http.client as http
http.HTTPConnection._http_vsn = 10
http.HTTPConnection._http_vsn_str = 'HTTP/1.0'

def datahora():
    time = strftime("%d_%m_%Y_%H_%M_%S", gmtime())
    return time

url="https://www.worten.pt/telemoveis-e-pacotes-tv/telemoveis-e-smartphones/como-escolher-telemoveis-e-smartphones"
root_url_brand = "https://www.worten.pt/telemoveis-e-pacotes-tv/telemoveis-e-smartphones/"

#Without this, we get an error
page = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
soup = BeautifulSoup(page.read().decode("utf-8"), "html.parser")

#Search for a ul table with class menu
table = soup.find('ul',{ "class" : "menu"})

#In that table search for li components where the class defined is not included
rows  = table.find_all('li',class_=lambda c: not c or 'w-category-submenu-parent' not in c)

urls=[]
phone_brand=[]
i=0
# Print all occurrences
for row in rows:
    #Dont show the lines where the word Smartphones are in
    if "Smartphones" not in row.get_text():
        i+=1
        phone_brand.append(row.get_text())
        urls.append(root_url_brand+unidecode(str(row.get_text())).replace(" ","-").replace("/","-").lower())
        print(str(i)+") "+row.get_text())

##Test Job#####
#Open all webpages saved in urls[]
#for index in urls:
    #webbrowser.open_new_tab(index)
###############

#Now, we want to get the prices of the brand the user select
index=input("Type the number of the brand you want: ")
url_to_scrap=urls[int(index)-1]+"?page=1"
# print(url_to_scrap) #URL
#webbrowser.open_new(url_to_scrap) #Abrir o link no browser

page = urlopen(Request(url_to_scrap, headers={'User-Agent': 'Mozilla/5.0'}))
soup = BeautifulSoup(page.read().decode("utf-8"), "html.parser")

table = soup.find('ul',{ "class" : "pagination text-center"})
linhas = table.find_all('li',{"class" : "pagination-last"})
ultima_linha=0

for row in linhas:
    ultima_linha=str(row.get_text())
    #print(row.get_text())
        
#Ultima pagina nao defenida
last_line=0
if ultima_linha == 0:
    linhas = table.find_all('li')
    for linha in linhas:
            string_linha=str(linha.get_text()).replace(" ","").replace("\n","").replace("page","").replace("You'reon","").replace("0","")
            if string_linha != "":
                last_line=string_linha
    ultima_linha=last_line
print("Ultima pagina: "+str(ultima_linha).replace(" ","").replace("\n",""))

precos=[]
nome=[]

for pagina in range(1,int(ultima_linha)):
    if pagina == 0:
        continue
    url_to_scrap=url_to_scrap[:-1]+str(pagina)
    print(url_to_scrap)
    page = urlopen(Request(url_to_scrap, headers={'User-Agent': 'Mozilla/5.0'}))
    soup = BeautifulSoup(page.read().decode("utf-8"), "html.parser")

    table = soup.find('div',{ "class" : "w-products-list__wrapper"})
    pre = table.find_all('span',{"class" : 'w-currentPrice iss-current-price'})
    nom = table.find_all('h3',{"class" : 'w-product__title'})

    
    for row in pre:
        precos.append(str(row.get_text())[1:].replace(",","."))
        #print(str(row.get_text())[1:].replace(",",".")+"€")

    for row in nom:
        nome.append(str(row.get_text()))
        #print(str(row.get_text()))
    
tele_num=len(precos)
file_name="./Desktop/"+phone_brand[int(index)-1]+"_"+str(datahora())+".txt"

if os.path.isfile(file_name) is not True:
    f = open(file_name, "x")

f=open(file_name,"w", encoding="utf-8")
for telemovel_num in range(tele_num):
    print("------------------")
    print(nome[telemovel_num])
    print(precos[telemovel_num]+"€")
    f.write(nome[telemovel_num]+";"+precos[telemovel_num]+"€"+"\n")
    print("------------------")
print(tele_num)
f.close()

