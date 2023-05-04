const $ = window.$;

async $.get('https://fourtonfish.com/hellosalut/?lang=fr',
  	(data, resp) => {
      	$('div#hello').text(data.hello);
  });
