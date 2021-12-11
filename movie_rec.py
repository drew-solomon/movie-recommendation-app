# This script performs simple content-based filtering 
# by vectorizing movies' text features using a Bag-Of-Words model
# and computing the cosine similarity between the movie vectors.

# The result is a list of the 'k' most similar movies, 
# i.e. the top "k" movie recommendations by similarity.

# Since IMDb ratings are already weighted by vote count
# and min vote count is > 25'000 in this dataset there's
# no need to weight ratings to avoid low vote outliers.

# import data from web scraping
import imdb_web_scrape

# get movies dataframe
movies_df = imdb_web_scrape.movies_df

# import libraries
import pandas as pd
import gdown
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# choose text features for movie vectorization
text_features = ['genres','description','stars','director']

# choose numerical features for movie vectorization
numerical_features = ['year', 'runtime']

# function to combine text features
def combine_features(row):
    combined_row = ''
    for feature in text_features:
      combined_row += row[feature]
    return combined_row

# remove null values in text features
for feature in text_features:
    movie_df[feature] = movie_df[feature].fillna('')

# combine text features
movie_df["combined_features"] = movie_df.apply(combine_features,axis=1)

# function to convert features into movie vectors
def vectorize(data):
  # create count vectorizer (for text features) which removes English stop-words
  cv = CountVectorizer(stop_words='english') 
  # vectorize movie text features (counts occurences of each unique word in word by text sample matrix)
  count_matrix = cv.fit_transform(data["combined_features"])
  # convert text vectors to array
  text_vectors = count_matrix.toarray()
  # get numerical features
  numerical = movie_df[numerical_features].to_numpy()
  # normalize numerical features
  numerical = (numerical - numerical.min(axis=0)) / (numerical.max(axis=0) - numerical.min(axis=0))
  # concatenate text vectors with numerical vectors to create movie vectors
  movie_vectors = np.concatenate((text_vectors, numerical), axis=1)

  # return movie vectors
  return movie_vectors

# function to get the indices of k most similar movies from list of similarity ratings for given movie
def k_largest_indices(sim_list, K):
  # convert similarity ratings for given movie to list of index, value pairs
  similar_movies = list(enumerate(sim_list))
  # sort similar movies by similarity rating
  sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
  # keep only the first k most similar movies indices
  similar_movies_indices = [x[0] for x in sorted_similar_movies[:K]]
 
  # return list of k most similar movies indices
  return similar_movies_indices

# function to return list of k most similar movies from given movie title
def k_most_similar_movies(movie, K):
  # convert movies into movie vectors
  movie_vectors = vectorize(movie_df)
  # compute cosine similarity between movie vectors
  similarity_matrix = cosine_similarity(movie_vectors)
  # get index for given movie title
  movie_index = movie_df[movie_df.movie == movie].index.values[0]
  # get list of similarity ratings for the given movie
  similarity_to_movie = similarity_matrix[movie_index] 
  # get the indices of the k most similar movies
  k_similar_movies = k_largest_indices(similarity_to_movie, K)

  # create list for movie recommendations
  movie_recs = []

  # loop through k most similar movies and add to list of recommended movies
  for index in k_similar_movies:
    # get movie title from index
    movie_title = movie_df[movie_df.index == index]["movie"].values[0]
    # add movie to list of movie names
    movie_recs.append(movie_title)

  # return dataframe of movie recommendations
  return pd.DataFrame({'recommended_movies': movie_recs})

  # example movie recommendation
  k_most_similar_movies('The Dark Knight', 10)