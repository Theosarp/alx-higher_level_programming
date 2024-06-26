#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number
// matches a given integer

const request = require('request');

const episodeId = process.argv[2];

if (parseInt(episodeId) < 8) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + episodeId;

  request(url, (err, res, body) => {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
}
