import dash
from dash import dash_table
from dash import dcc # dash core components
from dash.dependencies import Input, Output, State
from dash import html
import numpy as np
import pandas as pd
import recommend_movie # movie recommender functions

# read csv of processed movies dataframe
movies_df = pd.read_csv('data/movies_df_proc.csv')

# set marks for slider
marks = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

app = dash.Dash(__name__)

#  dropdown menu for movies
app.layout = html.Div(
    className="main",
    children=[
    html.H2("For You: Movie Recommender",id="title"),
    html.Img(src='https://tritonvoice.co/wp-content/uploads/2019/03/GKKFYsUV3HipHYUtKTrUPeiz.png', style={'height':'60%', 'width':'60%'}),
    html.H3("Find similar movies to the ones you love, from:",id="subtitle"),
    html.A('IMDb Top 1000 Movies (by User Rating)', href='https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating', target="_blank"),
    html.H4("Pick any movie you liked below:",id="pick_movie"),
    dcc.Dropdown(
        id='movie-dropdown',
        className="menu",
        options=[{'label': i, 'value': i} for i in list(movies_df['movie'])],
        value = 'The Dark Knight',
        placeholder="Pick any movie you liked!",
    ),
    html.H4("How many movie recommendations would you like?",id="pick_k"),
    # slider for number of movie recs
    dcc.Slider(
    id='slider',
    className="slider",
    min=1,
    max=10,
    step=1,
    marks=marks,
    value=5, # start with 5 movie recs
    ),
    dash_table.DataTable(
        id='table',
        columns=[],
        data= [],
        style_cell={'textAlign': 'center', 'width':220},
        style_header={'fontWeight': 'bold', 
            'font-family':'sans-serif', 
            'font-size':15,
            },
        style_data={'textAlign': 'center',
        'font-size':14,
        'backgroundColor': 'rgb(265, 265, 240)'},
    ),
    html.H4("Enjoy!",id="enjoy"),
    html.Img(src='https://www.cppng.com/file/download/2020-06/23321-9-popcorn-transparent-background.png', style={'height':'60%', 'width':'60%'}),
    ]
    
)


# callback function to update movie recs table based on selected movie
@app.callback(
    Output('table', 'columns'),
    Output('table', 'data'),
    Input('movie-dropdown', 'value'),
    Input('slider', 'value')
	)
def update_output(input_movie, input_k):
    # get dataframe of k most similar movie recs
    movie_recs_df = recommend_movie.get_k_most_similar_movies(input_movie, input_k)

    # convert df to dict
    movie_recs_dict = movie_recs_df.to_dict('records')

    # movie rec columns
    movie_recs_columns = [{"name": i, "id": i,'type':'text', "presentation":"markdown"} for i in movie_recs_df.columns]

    return movie_recs_columns, movie_recs_dict
	

app.run_server(debug=True, host="0.0.0.0")
