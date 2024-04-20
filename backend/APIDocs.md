# Letterboxd Watchlist Randomizer API

This is an API written in Python using Flask that allows you to retrieve a random movie or all movies from a user's Letterboxd watchlist.

## Endpoints

* /random_movie (GET): This endpoint returns a random movie from the specified user's watchlist.
  * Parameters:
    * username (required): The username of the Letterboxd user.
  * Response:
    * On success: JSON object containing username and random_movie.
    * On error: JSON object with an error message (e.g., username not provided or watchlist not found).
    * Status code:
      * 200: Success
      * 400: Bad Request (missing username)
      * 404: Not Found (watchlist not found)
* /all_movies (GET): This endpoint returns all movies from the specified user's watchlist.
  * Parameters:
    * username (required): The username of the Letterboxd user.
  * Response:
    * On success: JSON object containing username and a list of movies.
    * On error: JSON object with an error message (e.g., username not provided).
    * Status code:
      * 200: Success
      * 400: Bad Request (missing username)

## Example Usage

### Get a random movie from username "my_username"

curl http://localhost:5000/random_movie?username=my_username

### Get all movies from username "my_username"

curl http://localhost:5000/all_movies?username=my_username

Note: Replace localhost:5000 with the actual URL of your server if running this application elsewhere.

## Implementation Details

This API utilizes the following libraries:

* requests: Used to fetch data from the Letterboxd website.
* BeautifulSoup: Used to parse the HTML content of the watchlist page.
* Flask: Provides the web framework for building the API.
* flask_cors: Enables Cross-Origin Resource Sharing (CORS) for making requests from different domains.

The get_watchlist function scrapes the Letterboxd user's watchlist page using BeautifulSoup and extracts the movie titles. The select_random_movie function randomly selects a movie from the watchlist. Flask routes handle the API requests and return JSON responses.

Disclaimer: This script relies on web scraping, which can be fragile and break if Letterboxd changes their website structure. Consider this for informational purposes only.
