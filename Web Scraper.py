print ('''
       =======================
       a. Retrieve data
       b. Create the graph
       c. Display the matrix
       d. Save to Excel file
       e. Exit
       =======================
       ''')
import xlsxwriter
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import numpy as np
while True:
    choice=input('Please enter your option ')
    if choice=='a':
        page = requests.get("https://classiccars.com/listings/find/1974-2022?ps=30")
        soup = BeautifulSoup(page.content, "html.parser")
        elems = soup.find_all("div", class_="search-result-item w100 featured")
        for i in elems:
            title = i.find("div", class_="dark mrg-b-sm b fs-20 w100 height-rw h-sri-car-title")
            price = i.find("div", class_="b fs-18 mrg-b-sri-price green")
            print(title.text, price.text)
    if choice=='b':
        page = requests.get("https://classiccars.com/listings/find/1974-2022?ps=30")
        soup = BeautifulSoup(page.content, "html.parser")
        elems = soup.find_all("div", class_="search-result-item w100 featured")
        title_list=[]
        price_list=[]
        for i in elems:
            title = i.find("div", class_="dark mrg-b-sm b fs-20 w100 height-rw h-sri-car-title")
            price = i.find("div", class_="b fs-18 mrg-b-sri-price green")
            title_list.append(title.text)
            num = price.text.replace(",", "")
            num = num.replace("$", "")
            num = num.split(" ")[0]
            price_list.append(int (num))
        fig, ax = plt.subplots(figsize=(20, 8))
        ax.barh(title_list, price_list)
        ax.invert_yaxis()
        plt.show()
    if choice=='c':
        page = requests.get("https://classiccars.com/listings/find/1974-2022?ps=30")
        soup = BeautifulSoup(page.content, "html.parser")
        elems = soup.find_all("div", class_="search-result-item w100 featured")
        title_list=[]
        price_list=[]
        for i in elems:
            title = i.find("div", class_="dark mrg-b-sm b fs-20 w100 height-rw h-sri-car-title")
            price = i.find("div", class_="b fs-18 mrg-b-sri-price green")
            title_list.append(title.text)
            num = price.text.replace(",", "")
            num = num.replace("$", "")
            num = num.split(" ")[0]
            price_list.append(int (num))
        matrix = np.array([title_list,price_list])
        for i in range(len(title_list)):
            print(matrix[0][i], matrix[1][i], sep=" ")
    if choice=='d':
        page = requests.get("https://classiccars.com/listings/find/1974-2022?ps=30")
        soup = BeautifulSoup(page.content, "html.parser")
        elems = soup.find_all("div", class_="search-result-item w100 featured")
        title_list=[]
        price_list=[]
        for i in elems:
            title = i.find("div", class_="dark mrg-b-sm b fs-20 w100 height-rw h-sri-car-title")
            price = i.find("div", class_="b fs-18 mrg-b-sri-price green")
            title_list.append(title.text)
            num = price.text.replace(",", "")
            num = num.replace("$", "")
            num = num.split(" ")[0]
            price_list.append(int (num))
        workbook = xlsxwriter.Workbook('Excel.xlsx')
        worksheet = workbook.add_worksheet("Excel")
        row = 0
        col = 0
        for name, price in zip(title_list, price_list):
            worksheet.write(row, col, name)
            worksheet.write(row, col + 1, price)
            row += 1
        workbook.close()
    if choice=='e':
        break