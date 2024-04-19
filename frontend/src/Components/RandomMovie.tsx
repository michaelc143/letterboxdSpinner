// src/components/RandomMovie.tsx

import { useState, ChangeEvent, FormEvent } from 'react';

const RandomMovie: React.FC = () => {
  const [username, setUsername] = useState<string>('');
  const [randomMovie, setRandomMovie] = useState<string | null>(null);

  const handleUsernameChange = (event: ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handleFormSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const response = await fetch(`http://localhost:5000/random_movie?username=${username}`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setRandomMovie(data.random_movie);
    } catch (error) {
      console.error('Error fetching random movie:', error);
    }
  };

  return (
    <div>
      <h2>Random Movie</h2>
      <form onSubmit={handleFormSubmit}>
        <label>
          Username:
          <input type="text" value={username} onChange={handleUsernameChange} />
        </label>
        <button type="submit">Get Random Movie</button>
      </form>
      {randomMovie && <p>{randomMovie}</p>}
    </div>
  );
};

export default RandomMovie;
