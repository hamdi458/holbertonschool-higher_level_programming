$(document).ready(function(){
    $.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data){
        jQuery.each(data.results, function(key,value) {
            $('UL#list_movies').append('<li>'+value.title +'</li>');
          });
})
});