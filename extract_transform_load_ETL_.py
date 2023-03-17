import requests
from bs4 import BeautifulSoup
import pandas

COLUMNS = ["Rank", "Major", "Degree Type", "Early Career Pay", "Mid Career Pay", "% High Meaning"]
rank_list = []
major_list = []
degree_type_list = []
early_career_pay_list = []
mid_career_pay_list = []
high_meaning_list = []

page_number = 1
while True:
    url = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page_number}"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    table_rows = soup.find_all(name='tr', class_='data-table__row')
    if not table_rows:
        break
    for row in table_rows:
        data_list = []
        for i in row.find_all(name='td'):
            data_list.append(i.text.split("\n")[0].split(":")[1])
        rank_list.append(data_list[0])
        major_list.append(data_list[1])
        degree_type_list.append(data_list[2])
        early_career_pay_list.append(data_list[3])
        mid_career_pay_list.append(data_list[4])
        high_meaning_list.append(data_list[5])
    page_number += 1

csv_data_list = []
for i in range(len(rank_list)):
    data_dict = {'Rank': rank_list[i], 'Major': major_list[i], 'Degree Type': degree_type_list[i],
                 'Early Career Pay': early_career_pay_list[i], 'Mid Career Pay': mid_career_pay_list[i],
                 '% High Meaning': high_meaning_list[i]}
    csv_data_list.append(data_dict)

df = pandas.DataFrame(csv_data_list, columns=COLUMNS)
df.to_csv("Py Scale.csv", index=False)



