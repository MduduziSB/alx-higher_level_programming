/*
 * This script  fetches and lists the title for all movies by using this URL:
 * https://swapi-api.alx-tools.com/api/films/?format=json
 */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function(data) {
    const movies = data.results;
    const listMovies = $('#list_movies');

    movies.forEach(function (movie) {
      const movieTitle = $('<li>').text(movie.title);
      listMovies.append(movieTitle);
    });
  }
});
