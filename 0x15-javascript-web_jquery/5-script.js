const $ = window.$;
$('div#add_item').click(function () {
  const d = $('ul.my_list').html() + '<li>Item</li>';

  $('ul.my_list').html(d);
});
