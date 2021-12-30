import csv 

with open("movies.csv", encoding = "utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    headers = data[0]
    all_movies = data[1:]
    print(len(all_movies))

headers.append("posterlink")
print(headers)

with open("movie_links.csv", encoding = "utf8") as f:
    reader = csv.reader(f)
    data1 = list(reader)
    all_movies_link = data1[1:]
    print(len(all_movies_link))

with open("final.csv", "a+", newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
                
for i in all_movies:
   poster_found = any( i[8] in j for j in all_movies_link)
   print(poster_found)
   if poster_found:
       for k in all_movies_link:
           if i[8] == k[0]:
               i.append(k[1])
               if len(i)==28:
                    with open("final.csv", "a+", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerows(i)