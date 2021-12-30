import pandas as pd 
import csv
import numpy as np

df = pd.read_csv("movies.csv")
C = df["vote_average"].mean()
m = df["vote_count"].quantile(0.9)

qmovies= df.copy().loc[df["vote_count"]>=m]
def weightRating(x,m=m,c=C):
  v=x["vote_count"]
  R=x["vote_average"]
  return (v/(v+m)*R)+(m/(m+v)*c)
qmovies["score"]=qmovies.apply(weightRating,axis=1)

output = qmovies[["title_x","vote_count","vote_average","score"]]
print(output)