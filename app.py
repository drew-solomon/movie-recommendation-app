import dash
from dash import dash_table
from dash import dcc # dash core components
from dash.dependencies import Input, Output, State
from dash import html
import numpy as np
import pandas as pd
import movie_rec # movie recommender functions

# read csv of scraped movies dataframe
movies_df = pd.read_csv('movies_df.csv')

print(movies_df.head())

app = dash.Dash(__name__)

#  dropdown menu for movies
app.layout = html.Div([
    dcc.Dropdown(
        id='movie-dropdown',
        options=[{'label': i, 'value': i} for i in list(movies_df['movie'])],
        placeholder="Pick any movie you liked!",
    ),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in movies_df.columns],
        data= movies_df.to_dict('records'),
    )
])


# callback function to update movie recs table based on selected movie
@app.callback(
    Output('table', 'columns'),
    Output('table', 'data'),
    Input('movie-dropdown', 'value'),
	)
def update_output(input_movie):
    # get dataframe of k most similar movie recs
    movie_recs_df = movie_rec.get_k_most_similar_movies(input_movie, 10)

    # convert df to dict
    movie_recs_dict = movie_recs_df.to_dict('records')

    # movie rec columns
    movie_recs_columns = [{"name": i, "id": i} for i in movie_recs_df.columns]

    return movie_recs_columns, movie_recs_dict
	

app.run_server(debug=True, host="0.0.0.0")
