const request = require('request');

function getCharacters (movieId) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  // request to the url
  request(url, function (err, res, body) {
    if (err || res.statusCode !== 200) {
      console.log('Error:', err);
    } else {
      const charactersUrls = JSON.parse(body).characters;
      charactersUrls.forEach((character) => {
        request(character, function (err, res, body) {
          if (err || res.statusCode !== 200) {
            console.log('Error:', err);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
      });
    }
  });
}

// getting the movie id from the command line

const movieId = process.argv[2];
if (movieId) {
  getCharacters(movieId);
} else {
  console.log('Please provide a movie id');
}
