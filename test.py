import gspread
from oauth2client.service_account import ServiceAccountCredentials
from collections import Counter
import requests
import urllib.request as urllib2
import os
import time

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("words").worksheet('level A1')
none_images = client.open("words").worksheet('None Images')
scenes = sheet.row_values(1)

for i in range(len(scenes)):
    words = sheet.col_values(i+1)
    del words[0:2]

    image_list = os.listdir("./images")
    # image_words = [name.strip('.jpg') for name in image_list]
    image_words = [os.path.splitext(name)[0] for name in image_list]
    no_images_words = list((Counter(list(dict.fromkeys(words))) - Counter(image_words)).elements())
    print (scenes[i],': ',len(no_images_words))
    none_images.update_cell(1, i+1, scenes[i])
    # for j in range(len(no_images_words)):
    #     time.sleep(1)
    #     none_images.update_cell(j+2, i+1, no_images_words[j])
    for row_num, word in enumerate(no_images_words):
        time.sleep(1)
        none_images.update_cell(row_num+2, i+1, word)