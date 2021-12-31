#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 15:17:50 2021

@author: Danny Boldt

@Websites used for reference:
        -> https://developers.themoviedb.org/3/getting-started/authentication

@use: Wrapper for the movie database(TMDB) API. Running the file with a valid
      API key will write general information regarding movies with the highest
      revenue in the specified year to a csv file called 'TMDB_movie_data.csv'.
      All parameters that can be changed the edit the output data are marked. 
      Instructions to access a unique API key for the TMDB database can be found
      in the link above. 
"""

# Import necessary libraries
import requests, json, csv, os
import requests # to make TMDB API calls
import locale # to format currency as USD
import pandas as pd

# opens access to the POSIX locale database making use more accessible.
locale.setlocale( locale.LC_ALL, '' )

"""
# Input unique API access key on line below.
"""
api_key = '14e84d27b089b58964962c9d8a517fdf'

# Specify primary release year below to choose which year to pull films from.
response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' +  api_key + '&primary_release_year=2021&sort_by=revenue.desc')

# store parsed json response
highest_revenue = response.json() 

# uncomment the next line to ensure json library worked correctly.
# print(highest_revenue)

# create list of names of films with highest revenue
highest_revenue_films = highest_revenue['results']

# define column names for our new dataframe
columns = ['film', 'revenue', 'genres', 'budget', 'popularity', 'original_language']

# create dataframe with same columns as defined above.
df = pd.DataFrame(columns=columns)

# define columns in csv file
csvFile = open('TMDB_movie_data.csv', 'a')
csvwriter = csv.writer(csvFile)
csvwriter.writerow(['film', 'revenue', 'genres', 'budget', 'popularity', 'original_language'])

# for each of the highest revenue films make an api call for that specific movie to gather it's information.
for film in highest_revenue_films:
    
    # call to API to retrieve individual film from list of films with highest revenue. 
    film_revenue = requests.get('https://api.themoviedb.org/3/movie/'+ str(film['id']) +'?api_key='+ api_key+'&language=en-US')
    film_revenue = film_revenue.json()
    
     # store title and revenue in our dataframe
    df.loc[len(df)]=[film['title'], film_revenue['revenue'], film_revenue['genres'], film_revenue['budget'], film_revenue['popularity'], film_revenue['original_language']] 
    
    # create csv file titled 'TMDB_movie_data.csv'.
    csvFile = open('TMDB_movie_data.csv','a')
    csvwriter = csv.writer(csvFile)
    
    # write each film and some of it's general box office information to csv file.
    csvwriter.writerow([film['title'],film_revenue['revenue'], film_revenue['genres'], film_revenue['budget'], film_revenue['popularity'], film_revenue['original_language']])
 












