import { useState, ChangeEvent } from 'react';

interface Movie {
	image: string;
	title: string;
}

const RandomMovie: React.FC = () => {
  const [username, setUsername] = useState<string>('');
  const [movies, setMovies] = useState<Movie[]>([]);
  const [randomMovie, setRandomMovie] = useState<Movie | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleUsernameChange = (event: ChangeEvent<HTMLInputElement>) => {
	setUsername(event.target.value);
  };

  const handleAllMoviesClick = async () => {
	try {
		const response = await fetch(`http://localhost:5000/all_movies?username=${username}`);
		if (!response.ok) {
		throw new Error('Network response was not ok');
		}
		const data = await response.json();
		setMovies(data.movies);
		setRandomMovie(null);
		setError(null);
	} catch (error) {
		console.error('Error fetching movies:', error);
		setMovies([]);
		setError('Error fetching movies. Please try again.');
	}
  };

  const handleRandomMovieClick = async () => {
	try {
		const response = await fetch(`http://localhost:5000/random_movie?username=${username}`);
		if (!response.ok) {
		throw new Error('Network response was not ok');
		}
		const data = await response.json();
		setRandomMovie(data.random_movie);
		setMovies([]);
		setError(null);
	} catch (error) {
		console.error('Error fetching random movie:', error);
		setRandomMovie(null);
		setError('Error fetching random movie. Please try again.');
	}
  };

  return (
	<div>
		<h2>Watchlist Movies</h2>
		<form onSubmit={(e) => e.preventDefault()}>
			<label>
				Username:
			<input type="text" value={username} onChange={handleUsernameChange} />
			</label>
		</form>
		<button onClick={handleAllMoviesClick}>Get All Movies</button>
		<button onClick={handleRandomMovieClick}>Get Random Movie</button>
		{error && <p>{error}</p>}
		{randomMovie && 
		<>
			<p>Random movie: {randomMovie.title}</p>
			<img src={randomMovie.image}/>
		</>}
		{movies.length > 0 && (
		<div>
			<h3>All Movies</h3>
			<ul>
				{movies.map((movie, index) => (
					<li key={index}>{movie.title}</li>
				))}
			</ul>
		</div>
		)}
	</div>
  );
};

export default RandomMovie;
