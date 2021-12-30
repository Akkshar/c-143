import pandas as pd 
import csv

with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
#print(all_movies)
liked_movies = []
unlike_movies = []
DidNot_Match = []
