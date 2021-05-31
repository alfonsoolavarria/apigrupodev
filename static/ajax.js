$(document).ready(function() {

  $("#loginForm").on( "click", function(e) {
    e.preventDefault();
    console.log("llegue",$("#test1").val());
    console.log($("#test1").val());
    data = {
      "phone":$("#test1").val(),
      "direction":$("#test2").val(),
      "localphone":$("#test3").val(),

    }

    $.post('/account/',data).done(function (result) {

      console.log('----post----');
    }).fail(function(error) {
      console.log();
    });


  });/*fin funcion onclik*/


  $("#loginForm2").on( "click", function(e) {
    e.preventDefault();
    $.get('/account/?flag=true',{}).done(function (result) {
      console.log('-GET--',result);
      $(".hola").css({"visibility":"visible"})

      for (var i = 0; i < result.message.length; i++) {
        console.log(result.message[i].phone);
        $(".hola").append("<input type='text' name='' id='p1"+i+"' value='"+result.message[i].phone+"' > <input type='text' name='' id='' value='"+result.message[i].id+"' > <input type='text' name='' id='' value='"+result.message[i].direccion+"' > <br>")
      }



    }).fail(function(error) {
      console.log();
    });
  });/*fin funcion onclik*/

  $("#loginForm3").on( "click", function(e) {
    e.preventDefault();
    var data = {"phone":$("#p11").val(),"id":9}

    $.ajax({
      url: '/account/',
      type: 'PUT',
      data: data,
      success: function(result) {
        console.log('--put----');
      }
    });
  });/*fin funcion onclik*/



});
