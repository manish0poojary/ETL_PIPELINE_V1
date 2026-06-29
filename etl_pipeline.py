import pandas as pd
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import sqlite3

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_name = 'GDP_of_countries'
db_name = 'World_economic.db'
json_path = '/home/manish/Documents/projects/python/etl_pipeline/Countries_by_GDP.json'
attributes = ['Country','GDP_USD_billion']
log_name = 'etl_project_log.txt'

def extract(url):
  plain_html = requests.get(url, timeout=15).text
  data = BeautifulSoup(plain_html,"html.parser")
  all_wiki_tables = data.find_all('table', class_='wikitable')
  table = all_wiki_tables[0].find_all('tr')[2:]
  return table
def transform(data):
  master_list = []
  for row in data:
    cells = row.find_all('td')
    if len(cells)>=4:
      country = cells[0].get_text(strip=True)
      gdp = cells[2].get_text(strip=True)
      if gdp == '—':
        gdp = pd.NA
      else :
        gdp = float(gdp.replace(',',''))
        gdp = round(gdp/1000,2)
      master_list.append({'Country':country,'GDP_USD_billion':gdp})
  df = pd.DataFrame(master_list)
  return df

def load(df):
  conn = sqlite3.connect(db_name)
  df.to_sql(table_name,conn,if_exists='replace',index=False)
  conn.close()
  df.to_json(json_path,orient='records')

def log(message):
  time_format = '%Y-%m-%d %H:%M:%S'
  now = datetime.now()
  start_time = datetime.strftime(now,time_format)
  with open(log_name,mode='a') as file :
    file.write(f'{start_time} {message} \n')


if __name__ == "__main__":
  log("extraction has started ")
  raw_data = extract(url)
  log("extraction has ended")

  log("transforming has started ")
  transformed_data = transform(raw_data)
  log("transforming has ended ")

  log("loading the data has started ")
  load(transformed_data)
  log("loading the data has ended ")
  print(transformed_data)
