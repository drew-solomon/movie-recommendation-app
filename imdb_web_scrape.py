import re
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
from time import sleep
from random import randint
from time import time
from IPython.core.display import clear_output



# set headers language to English to avoid translated titles
headers = {"Accept-Language": "en-US, en;q=0.5"}

# create lists for scraped data
titles = []
years = []
ratings = []
votes = []
genres = []
directors = []
stars = []
runtimes = []
descriptions = []

# preparing the monitoring of the loop
start_time = time()
requests = 0


# for every start page in increments of 250 from 1-751
for movie_num in [1, 251, 501, 751]:

    # print start page
    print("scraping movies", str(movie_num), "-", str(movie_num+250))

    # get request from IMDb "Top 1000" Movies by Rating URL (set to 250 movies per page)
    response = get('https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=250&start=' + str(movie_num) + '&ref_=adv_nxt', headers = headers)

    # pause the loop for 4-8 seconds
    sleep(randint(4,8))

    # monitor the requests
    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)

    # throw a warning for non-200 status codes
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))

    # break loop if the number of requests is greater than expected
    if requests > 4:
        warn('Number of requests was greater than expected.')
        break

    # parse the request content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # collect all the 250 movie divs from a single page
    movie_divs = soup.find_all('div', class_ = 'lister-item mode-advanced')

    # extract data from each movie div on page
    for movie in movie_divs:
        # get title
        title = movie.h3.a.text
        titles.append(title) 
        # get year
        year = movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
        year = int(re.sub("[^0-9]", "", year.text)) # keep numbers only and convert to integer
        years.append(year)
        # get rating
        rating = float(movie.strong.text)
        ratings.append(rating)
        # get vote count
        vote = movie.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))
        # get genres
        genre_list = movie.find('span', class_ = 'genre').text
        genre_list = genre_list.strip('\n').replace(",","").replace("'","").strip() # remove punctuation and whitespaces
        genres.append(genre_list)
        # get director
        director = movie.findAll('p')[2].find('a').text
        directors.append(director)
        # get stars
        stars_list = [name.text for name in movie.findAll('p')[2].findAll('a')][1:]
        stars_list = ' '.join(stars_list) # convert list to string
        stars.append(stars_list)
        # get runtimes
        runtime = movie.find('span', class_ = 'runtime').text
        runtime  = int(re.sub("[^0-9]", "", runtime)) # keep only the numbers and convert to integer
        runtimes.append(runtime)
        # get descriptions
        description = movie.findAll('p')[1].text.strip('\n')
        descriptions.append(description)


# create pandas dataframe with scraped data
movies_df = pd.DataFrame({
    'movie': titles,
    'year': years,
    'rating': ratings,
    'vote_count': votes,
    'genres': genres,
    'director': directors,
    'stars': stars,
    'runtime': runtimes,
    'description': descriptions
})

# check df info
print(movies_df.info())

# show head of movies df
movies_df.head(20)

# save movies dataframe as .csv
movies_df.to_csv('movies_df.csv')
