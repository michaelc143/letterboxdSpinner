"""Python script to randomly select a movie from a Letterboxd user's watchlist."""
import random
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
