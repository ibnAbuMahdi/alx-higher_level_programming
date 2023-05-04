const $ = window.$;

$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  (data, resp) => {
    data.results.forEach((v, x, a) => {
      const d = $('ul#list_movies').html();
      $('ul#list_movies').html(d + '<li>' + v.title + '</li>');
    });
  });
