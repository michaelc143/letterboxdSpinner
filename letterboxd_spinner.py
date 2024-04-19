"""Python script to randomly select a movie from a Letterboxd user's watchlist."""
import random
import requests
from bs4 import BeautifulSoup

def get_watchlist(username):
    """Get the watchlist of a Letterboxd user."""
    url = f'https://letterboxd.com/{username}/watchlist/'
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find_all('li', class_='poster-container')
    movie_titles = [movie.find('img')['alt'] for movie in movies]
    return movie_titles

def select_random_movie(watchlist):
    """Randomly select a movie from a Letterboxd user's watchlist."""
    return random.choice(watchlist)

if __name__ == "__main__":
    selected_username = input("Enter Letterboxd username: ")
    selected_watchlist = get_watchlist(selected_username)
    if selected_watchlist:
        random_movie = select_random_movie(selected_watchlist)
        print(f"Randomly selected movie from {selected_username}'s watchlist: {random_movie}")
    else:
        print("No watchlist found for this user.")
