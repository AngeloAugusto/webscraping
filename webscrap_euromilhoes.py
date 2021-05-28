from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from unidecode import unidecode
import webbrowser
import os
import http.client as http
import xlsxwriter
http.HTTPConnection._http_vsn = 10
http.HTTPConnection._http_vsn_str = 'HTTP/1.0'

url_root="https://www.euro-millions.com/pt/arquivo-de-resultados-"
ultimo_ano="2021"
url=url_root+ultimo_ano

page = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
soup = BeautifulSoup(page.read().decode("utf-8"), "html.parser")

table = soup.find('ul',{ "class" : "year"})

rows  = table.find_all('li')
# anos=[]
# dados=[]
# num1_todos=[]
# num2_todos=[]
# num3_todos=[]
# num4_todos=[]
# num5_todos=[]
# est1_todos=[]
# est2_todos=[]
row = 0
col = 0

workbook_todos = xlsxwriter.Workbook('Desktop\euro_milhoes_bd_v2\euro_milhoes_todos.xlsx')
worksheet_todos = workbook_todos.add_worksheet()

row_excel_todos = 0
row_excel = 0
col = 0

worksheet_todos.write(row_excel_todos, col, 'Data')
worksheet_todos.write(row_excel_todos, col+1, "Numero 1")
worksheet_todos.write(row_excel_todos, col+2, "Numero 2")
worksheet_todos.write(row_excel_todos, col+3, "Numero 3")
worksheet_todos.write(row_excel_todos, col+4, "Numero 4")
worksheet_todos.write(row_excel_todos, col+5, "Numero 5")
worksheet_todos.write(row_excel_todos, col+6, "Estrela 1")
worksheet_todos.write(row_excel_todos, col+7, "Estrela 2")

for row in rows:
    #print(row.get_text())

    # anos.append(row.get_text())

    workbook = xlsxwriter.Workbook('Desktop\euro_milhoes_bd_v2\euro_milhoes_'+row.get_text()+'.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(row_excel, col, 'Data')
    worksheet.write(row_excel, col+1, "Numero 1")
    worksheet.write(row_excel, col+2, "Numero 2")
    worksheet.write(row_excel, col+3, "Numero 3")
    worksheet.write(row_excel, col+4, "Numero 4")
    worksheet.write(row_excel, col+5, "Numero 5")
    worksheet.write(row_excel, col+6, "Estrela 1")
    worksheet.write(row_excel, col+7, "Estrela 2")
    
    url=url_root+row.get_text()
    page = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    soup = BeautifulSoup(page.read().decode("utf-8"), "html.parser")

    table = soup.find('div',{ "class" : "container"})

    row2 = table.find_all('div',{ "class" : "archives"})

    for row in row2:

        row_excel=row_excel+1
        row_excel_todos=row_excel_todos+1

        linha=str(row.get_text()).replace("\n"," ").replace("de 20", " de 20")\
            .replace("a1", "a 1").replace("a2", "a 2").replace("a3", "a 3")\
            .replace("a4", "a 4").replace("a5", "a 5").replace("a6", "a 6")\
            .replace("a7", "a 7").replace("a8", "a 8").replace("a9", "a 9")\
            .replace("o1", "o 1").replace("o2", "o 2").replace("o3", "o 3")\
            .replace("o4", "o 4").replace("o5", "o 5").replace("o6", "o 6")\
            .replace("o7", "o 7").replace("o8", "o 8").replace("o9", "o 9")\
            .replace("  ", " ")
        
        linha2=linha.split(" ")
        dia=linha2[0]+" "+linha2[1]+" "+linha2[2]+" "+linha2[3]+" "+linha2[4]+" "+linha2[5]+" "+linha2[6]
        num1=linha2[7]
        # num1_todos.append(num1)
        num2=linha2[8]
        # num2_todos.append(num2)
        num3=linha2[9]
        # num3_todos.append(num3)
        num4=linha2[10]
        # num4_todos.append(num4)
        num5=linha2[11]
        # num5_todos.append(num5)
        est1=linha2[12]
        # est1_todos.append(est1)
        est2=linha2[13]
        # est2_todos.append(est2)

        # dados.append(dia+";"+num1+";"+num2+";"+num3+";"+num4+";"+num5+";"+est1+";"+est2)
        print(dia+" "+"num1: "+num1 +" num2: "+num2+" num3: "+num3+" num4: "+num4+" num5: "+num5+" est1: "+est1+" est2: "+est2)
        worksheet_todos.write(row_excel_todos, col, dia)
        worksheet_todos.write(row_excel_todos, col+1, num1)
        worksheet_todos.write(row_excel_todos, col+2, num2)
        worksheet_todos.write(row_excel_todos, col+3, num3)
        worksheet_todos.write(row_excel_todos, col+4, num4)
        worksheet_todos.write(row_excel_todos, col+5, num5)
        worksheet_todos.write(row_excel_todos, col+6, est1)
        worksheet_todos.write(row_excel_todos, col+7, est2)

        worksheet.write(row_excel, col, dia)
        worksheet.write(row_excel, col+1, num1)
        worksheet.write(row_excel, col+2, num2)
        worksheet.write(row_excel, col+3, num3)
        worksheet.write(row_excel, col+4, num4)
        worksheet.write(row_excel, col+5, num5)
        worksheet.write(row_excel, col+6, est1)
        worksheet.write(row_excel, col+7, est2)

    workbook.close()
workbook_todos.close()
