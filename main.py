from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome()
driver.get('https://www.imdb.com/chart/top/')

movies_list = []
movies_list_2 = []
movies_list_3 = []
movies_update_list = []
select_movies = driver.find_elements(By.XPATH,
                                     "/html//div[@id='__next']/main[@role='main']/div[@role='presentation']/div[@role='presentation']/section//div[@class='ipc-page-grid ipc-page-grid--bias-left']/div/ul[@role='presentation']")
for movie in select_movies:
    movies_list.append(movie.text)

size_movie_list = len(movies_list)

for i in range(size_movie_list):
    value = movies_list[i].split('\n')
    movies_update_list.append(value)

movies_list.clear()
for i in range(0, 462, 6):
    value = movies_update_list[0][i:i + 6]
    movies_list.append(value)

for i in range(467, 1499, 6):
    value = movies_update_list[0][i:i + 6]
    movies_list_2.append(value)


value = movies_update_list[0][462:467]
movies_list_3.append(value)

movies_update_list.clear()
for i in range(len(movies_list)):
    items = {
        "title": movies_list[i][0],
        "year": movies_list[i][1],
        "duration": movies_list[i][2],
        "rate": movies_list[i][3],
        "rating": movies_list[i][4]
    }
    movies_update_list.append(items)

items3 = {
    "title": movies_list_3[0][0],
    "year": movies_list_3[0][1],
    "duration": movies_list_3[0][2],
    "rating": movies_list_3[0][3],
    "rate": movies_list_3[0][4]
}
movies_update_list.append(items3)

for i in range(len(movies_list_2)):
    items2 = {
        "title": movies_list_2[i][0],
        "year": movies_list_2[i][1],
        "duration": movies_list_2[i][2],
        "rate": movies_list_2[i][3],
        "rating": movies_list_2[i][4]

    }
    movies_update_list.append(items2)



df = pd.DataFrame(movies_update_list)
df.to_csv('IMDB_top250.csv', index=False)