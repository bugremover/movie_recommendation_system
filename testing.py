import pickle

with open('artificats/movie_list.pkl', 'rb') as file:
    movies = pickle.load(file)
    
print(type(movies))
print(movies.head())
