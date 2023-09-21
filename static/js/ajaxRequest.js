$(document).ready(function() {
  // Function to update the content of the container div
  function Packages() {
    $.ajax({
      url: '/get_objects/',
      type: 'GET',
      dataType: 'json',
      success: function(response) {
          console.log(response);
          $('.packages .container').empty();
                
          // Add each object to the container div
          response.forEach(function(object) {
            let box = $('<div></div>').addClass('box');
            let image = $('<img></img>').attr('src', object.image);
            let content = $('<div></div>').addClass('content');
            let title = $(`<h3>${object.location}</h3>`);
            let icon = $('<i></i>').addClass('fas fa-map-marker-alt');
            icon.css('margin-right', '10px');
            let description = $('<p></p>').html(object.description);
            let price = $('<div></div>').html('$' + object.price + ' <span>' + `$` + object.last_price + '</span>');
            price.addClass("price");
            const bookingURL = "{% url 'booking' %}";
            let link = $(`<a>${'Check now'}</a>`).attr('href', 'booking/');
            link.addClass("btn");
            $(content).prepend(link);
            $(content).prepend(price);
            $(content).prepend(description);
            $(title).prepend(icon);
            $(content).prepend(title);
            $(box).prepend(content);
            $(box).prepend(image);
            $('.packages .container').append(box);
          });
        // },
        // error: function(xhr, status, error) {
        //   alert('error');
        // }
      }});
    }
    
    Packages();
    setInterval(function() {
        Packages();
    }, 1000);
  });