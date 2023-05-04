const $ = window.$;

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
  (data, resp) => {
    $('div#character').text(data.name);
  });
