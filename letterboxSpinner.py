import requests
from bs4 import BeautifulSoup
import random

def get_watchlist(username):
    url = f'https://letterboxd.com/{username}/watchlist/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find_all('li', class_='poster-container')
    movie_titles = [movie.find('img')['alt'] for movie in movies]
    return movie_titles

def select_random_movie(watchlist):
    return random.choice(watchlist)

if __name__ == "__main__":
    username = input("Enter Letterboxd username: ")
    watchlist = get_watchlist(username)
    if watchlist:
        random_movie = select_random_movie(watchlist)
        print(f"Randomly selected movie from {username}'s watchlist: {random_movie}")
    else:
        print("No watchlist found for this user.")
