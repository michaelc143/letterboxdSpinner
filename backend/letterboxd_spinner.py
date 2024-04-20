"""Python script to randomly select a movie from a Letterboxd user's watchlist."""
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

def get_watchlist(username):
    """Get the watchlist of a Letterboxd user."""
    url = f'https://letterboxd.com/{username}/watchlist/'

    # Use headless browser (Chrome in this example)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    movies = soup.find_all('li', class_='poster-container')

    watchlist = []
    for movie in movies:
        title = movie.find('img')['alt']
        image = movie.find('img')['src']
        watchlist.append({'title': title, 'image': image})

    driver.quit()
    return watchlist

def get_all_movies(username):
    """Get all movies from a Letterboxd user's watchlist."""
    return get_watchlist(username)

def select_random_movie(watchlist):
    """Randomly select a movie from a Letterboxd user's watchlist."""
    return random.choice(watchlist)

@app.route('/random_movie', methods=['GET'])
def random_movie():
    """Flask route to get a random movie from a Letterboxd user's watchlist."""
    selected_username = request.args.get('username')
    if not selected_username:
        return jsonify({"error": "Username parameter is missing"}), 400

    selected_watchlist = get_watchlist(selected_username)
    if selected_watchlist:
        randomly_selected_movie = select_random_movie(selected_watchlist)
        return jsonify({"username": selected_username, "random_movie": randomly_selected_movie})

    return jsonify({"error": "No watchlist found for this user."}), 404

@app.route('/all_movies', methods=['GET'])
def all_movies():
    """Flask route to get all movies from a Letterboxd user's watchlist."""
    selected_username = request.args.get('username')
    if not selected_username:
        return jsonify({"error": "Username parameter is missing"}), 400

    all_movies = get_all_movies(selected_username)
    return jsonify({"username": selected_username, "movies": all_movies})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
