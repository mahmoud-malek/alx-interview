#!/usr/bin/node
const request = require('request');

// Function to fetch a URL and return the result as a Promise
function fetchCharacterData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(new Error(`Error fetching character data: ${error}`));
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

// Function to get characters from a movie based on the movie ID
async function getCharacters (movieId) {
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  // First, request the movie data
  request(movieUrl, async (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error(`Error fetching movie data: ${error}`);
      return;
    }

    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Fetch each character's data in sequence to maintain the order
    for (const url of characterUrls) {
      try {
        const characterName = await fetchCharacterData(url);
        console.log(characterName);
      } catch (error) {
        console.error(error);
      }
    }
  });
}

// Get the movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command line argument.');
  process.exit(1);
}

// Fetch and print characters from the movie in order
getCharacters(movieId);
