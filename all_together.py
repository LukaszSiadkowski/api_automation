import json, csv, requests, ast, collections, time
from csv import writer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

#download data

headers = {
    'accept': 'application/json',
    'apikey': 'xxxxxxxxxxxxxxxxx',
}

with open('output.json', 'w', encoding='utf-8') as outf:
    outf.write('[')
    for page in range(0, 186):
        response = requests.get(f'xxxxxxxxxxxxxx/products?page={page}', headers=headers).text
        outf.write(response)
        if page <185:
            outf.write(',')    
    outf.write(']')

with open('output.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

for p in range (0, 186):
    try:
        employee_data = data[p]['products']
        data_file = open('output.csv', 'a', newline='', encoding='utf-8')
        csv_writer = csv.writer(data_file)
        count = 0
    except KeyError: 
        continue
    
    for emp in employee_data:
       
        if count == 0:
            
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(emp.values())
        
    data_file.close()


df = pd.read_csv(r'xxxxxxxxxxxxxxxxxx\output.csv')


new_df = df.drop(['attributes','xxxxxx', ....................], axis=1)

new_df = new_df[new_df["xxxxxxxx"].str.contains("xxxxxxxx") == False]
new_df = new_df[new_df["xxxxxxxxx"].str.contains("xxxxxxx") == False]

new_df['aaaaaaaaaa']=new_df['Title']


cols_to_be_notna = ['name', 'xxxxxxxxxxx', ................]
for col in cols_to_be_notna:
     new_df[col] = new_df[col].notna()


new_df.columns = ['Title', 'xxxxxxxxxx', ......................]

new_df.drop_duplicates(subset ="Title", keep = 'last', inplace = True)

new_df['zzzzzzzzzzzzzzzz'] = new_df['Variant']
new_df['zzzzzzzzzzzzzzz'] = pd.to_numeric(new_df['zzzzzzzzzzzzzzzzzz'])
new_df['zzzzzzzzzzzzz'] = new_df['zzzzzzzzzzzzzzzzzzzzzz']*1.1
new_df['zzzzzzzzzzzz'] = new_df['zzzzzzzzzzzzzzzzzzzz'].round(decimals=2)




new_df.to_csv('prepared.csv', index=False, encoding='utf-8')

df = pd.read_csv(r'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\output.csv')


crashed = df.drop(['available', 'xxxxxxxxxxxx', ....................], axis=1)


cols_to_be_notna = ['name', 'xxxxxxxxxxx', ................]
for col in cols_to_be_notna:
     crashed[col] = crashed[col].notna()


crashed.columns = ['Title', 'xxxxxxxxxxxx', .............................]

crashed = crashed[crashed["zzzzzz"].str.contains("xxxxxxxx") == False]
crashed = crashed[crashed["zzzzzzzzz"].str.contains("xxxxxxxxx") == False]


crashed['aaaaaaaaa']=crashed['Title']


crashed.drop_duplicates(subset ="Title", keep = 'last', inplace = True)

crashed['zzzzzzzzzz'] = crashed['Variant']


crashed['zzzzzzzzzzzz'] = pd.to_numeric(crashed['zzzzzzzzzzzzzzz'])

crashed['zzzzzzzzzzzzz'] = crashed['zzzzzzzzzzzzzzzzzzzzzzzz']*1.1
crashed['zzzzzzzzzzzzzzzzzzzzz'] = crashed['zzzzzzzzzzzzzzzzzzz'].round(decimals=2)



crashed.to_csv('crashed.csv', index=False, encoding='utf-8')

#importing file
s=Service('xxxxxxxx/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='xxxxxxxxxx'
browser.get(url)
search_query_input = browser.find_element(By.ID, 'pppppppppppppppp')
search_query_input.send_keys('xxxxxxxx')
time.sleep(10)
search_button = browser.find_element(By.CLASS_NAME, 'ui-button.ui-button--primary.ui-button--full-width.ui-button--size-large.captcha__submit')
search_button.click()

time.sleep(5)

search_query_input_2 = browser.find_element(By.ID, 'eeeeeeeeeeeeeeeeeeeee')
search_query_input_2.send_keys('xxxxxxxxxxxxxxxxxxxxxxxx')

time.sleep(10)

search_button_2 = browser.find_element(By.CLASS_NAME, 'ui-button.ui-button--primary.ui-button--full-width.ui-button--size-large.captcha__submit')
search_button_2.click()

time.sleep(5)
url2='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
browser.get(url2)

time.sleep(10)

#importing first file 

like = browser.find_elements(By.CLASS_NAME, 'Polaris-Button__Text_yj3uv')
for x in range(0,len(like)):
    if like[1].is_displayed():
        like[1].click()
        break
        
time.sleep(10)
        
fileInput = browser.find_element(By.XPATH, "//input[@type='file']").send_keys("xxxxxxxxxxxxxxx/crashed.csv")

time.sleep(5)

overwrite = browser.find_element(By.XPATH, '//span[span/input[@name="overwrite"]]')
overwrite.click()

time.sleep(5)

upload = browser.find_elements(By.CLASS_NAME, 'Polaris-Button__Text_yj3uv')
for x in range(0,len(like)):
    if upload[12].is_displayed():
        upload[12].click()
        break
        
time.sleep(5)
     
upload2 = browser.find_elements(By.CLASS_NAME, 'Polaris-Button__Text_yj3uv')
for x in range(0,len(like)):
    if upload2[11].is_displayed():
        upload2[11].click()
        break
        
time.sleep(180)

#second file
like = browser.find_elements(By.CLASS_NAME, 'Polaris-Button__Text_yj3uv')
for x in range(0,len(like)):
    if like[1].is_displayed():
        like[1].click()
        break
        
time.sleep(10)

        
fileInput = browser.find_element(By.XPATH, "//input[@type='file']").send_keys("xxxxxxxxxxxxxxxxxxxxx/prepared.csv")

time.sleep(5)

overwrite = browser.find_element(By.XPATH, '//span[span/input[@name="overwrite"]]')
overwrite.click()

time.sleep(5)


upload = browser.find_elements(By.CLASS_NAME, 'Polaris-Button__Text_yj3uv')
for x in range(0,len(like)):
    if upload[12].is_displayed():
        upload[12].click()
        break
        
time.sleep(5)

        
upload2 = browser.find_elements(By.CLASS_NAME, 'Polaris-Button__Text_yj3uv')
for x in range(0,len(like)):
    if upload2[11].is_displayed():
        upload2[11].click()
        break
        
time.sleep(5)
browser.quit()
