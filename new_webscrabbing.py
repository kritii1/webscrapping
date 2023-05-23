import requests
from bs4 import BeautifulSoup
import pandas as pd

page=requests.get('https://www.name.edu.np/results/')
soup=BeautifulSoup(page.content,'html.parser')

print(soup)

title_exam=[]
result_date=[]
result_check=[]

for item in soup.find_all("h4"):
    title_exam.append(item.text)
print(title_exam)

for item in soup.find_all("div",attrs={'class':'resultdate'}):
    result_date.append(item.text)

for items in soup.find_all("ahref:https://www.name.edu.np/results/result/247",attrs={'class':'result-title mt10'}):
    result_check.append(item.text)



data={"title_exam":title_exam,"result_date":result_date,"result_check":result_check}

data_table=pd.DataFrame(data)
print(data_table)
data_table.to_excel("resultdata.xlsx")
