import requests
import pandas as pd
from bs4 import BeautifulSoup

try:
    # to get data from website
    url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
    response = requests.get(url)

    # To check if the above code was successful.
    # print(response.status_code)
    # print(file.raise_for_status())

    soup = BeautifulSoup(response.content, 'html.parser')

    #   Finding the text inside the title tag
    title = soup.title.string
    print(title)

    info = soup.find('p').get_text()
    print(info)

    # Extracting the tv show elements
    tv_shows = soup.find_all('td', class_='titleColumn')

    # Extracting the rank of the tv show
    rank = [i.get_text(strip=True).split('.')[0] for i in tv_shows]
    print("Rank: ", rank)

    # Getting the title of the tv shows
    show_name = [i.find('a').text for i in tv_shows]
    print("Title: ", show_name)
    print("The number of tv shows are ", len(show_name))

    # Getting the year in which the show was released
    year = [i.find('span').text.strip('()') for i in tv_shows]
    print("Year: ", year)

    # Extracting the ratings given by IMDb
    rating = soup.find_all("td", class_="ratingColumn imdbRating")
    imdb_rating = [i.find('strong').get_text() for i in rating]
    print("IMBd_Rating: ", imdb_rating)

except Exception as e:
    print(e)

df = pd.DataFrame({"Rank": rank, "Title": show_name, "Released_Year": year, "IMDb_Rating": imdb_rating})
print(df)

# Saving the data into a csv file
df.to_csv("IMDb_TV_Show.csv", index = False)

