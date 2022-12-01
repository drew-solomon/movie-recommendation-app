[![imdb_scraper](https://github.com/drew-solomon/movie-rec-dash-app/actions/workflows/imdb_scraper.yml/badge.svg)](https://github.com/drew-solomon/movie-rec-dash-app/actions/workflows/imdb_scraper.yml)

# Movie Recommendation Dash App
This live data project contains a Dash app that recommends movies from daily updating IMDb movie data and an accompanying BI dashboard to visualize the movie trends. 
_(Final Project for DATA 1050 - Data Engineering @ Brown University Fall 2021)_

> Run the app from the shared Gitpod [workspace](https://bit.ly/movie-recommendation-app) following the quick [setup](#setup) below.

## Table of Contents
* [Project Description](#project-description)
* [Methods](#methods-used)
* [Technologies Used](#technologies-used)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Deliverables](#deliverables)
* [Contributing Members](#contributing-members)
* [Acknowledgements](#acknowledgements)


## Project Description

- Movie recommendation systems can save us time and effort finding great movies and help us explore our tastes using machine learning. 
- As a final project for DATA1050, I built a Dash app to recommend movies from daily updating IMDb movie data, using basic content-based filtering to recommend similar movies to ones the user picks interactively. 
- As a live data project, the workflow scrapes movie data daily from [IMDb Top 1000 Movies (by User Rating)](https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating) to a Supabase (postgres) database using Github Actions.
- To visualize trends in the live movie data, I created an accompanying Preset dashboard querying the scraped data in SQL.
- The simple Dash app - formatted using flexbox and CSS - has a dropdown menu of movies to choose from (all top 1000) and a slider for the desired number of recommendations, and outputs a table of movie recommendations by similarity (with embedded links to their IMDb pages).

## Methods Used
- Web scraping
- Interactive web application
- EDA
- ETL
- Interactive dashboard visualization (BI)
- SQL database

## Technologies Used
- Plotly Dash 
- Supabase (PostgreSQL database)
- Apache Preset (BI)
- Python
- CSS
- BeautifulSoup
- Github Actions
- Gitpod

## Screenshots


#### Movie Rec Dash App


|![Dash-app-example.png](https://i.postimg.cc/Xq6XrpH6/Dash-app-example.png)
|:--:|
|*Dash app example with dropdown menu of web-scraped top movies, slider for number of recommendations, and recommendations with links.*|

#### Movie Trends Dashboard (BI)
|![Movie-trends-dashboard-example.jpg](https://i.postimg.cc/QddCKLbC/Movie-trends-dashboard-example.jpg)]
|:--:|
|*Interactive dashboard for IMDb top 1000 movies, scraped daily. Illustrates key numbers and trends in the top movies - e.g. top movies and directors as well as the distribution of ratings, genres, and release years.*|

## Setup

To run the movie recommendation Dash app, follow the following three steps:

1. Open my shared Gitpod [workspace](https://bit.ly/movie-recommendation-app). 


2. Run the following commands in the Terminal (within the workspace):
    ```
    sh run.sh
    python app.py
    ```

3. Click _“Open Browser”_ on the pop-up below:
![Screenshot-2022-11-29-at-23-52-18.png](https://i.postimg.cc/J0qLqnqX/Screenshot-2022-11-29-at-23-52-18.png)


Then, pick any movie you like from the dropdown menu (sorted A-Z) and select the number of recommendations you want using the slider. Enjoy!


## Featured Deliverables
- Movie recommendation Dash [app](https://bit.ly/movie-recommendation-app)
- Live interactive _IMDb Top 1000 Movies_ [dashboard](https://8d8e0f5b.us2a.app.preset.io:443/r/2)

## Contributing Members
- [Drew Solomon](https://github.com/drew-solomon) (me)




## Acknowledgements
- This project data was sourced from [IMDb's Top 1000 Movies (by User Rating)](https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating) (scraped daily using BeautifulSoup to a Supabase database, scheduled with Github Actions).
- Many thanks to Professor Sam Watson for an excellent class!
