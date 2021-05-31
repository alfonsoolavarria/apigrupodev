
// animaciones de entrada

    let card = $(".card");

    window.onload = function(){
        formulario.show('drop','slow');
    }

    // cargar datos




    let nombre = $("#Nombre").val();
    let apellido = $("#Apellido").val();
    let numerotelefonico = $("#Numerotelefonico").val();
        // let email = $("#Email").val();

        // mostrar datos en caja



            var data_user = {

                phone: $(".liNombre").text(),
                direction: $(".liApellido").text(),
                localphone: $(".liNumero").text(),


            };

        // volver a formulario


            // enviar metodo post
        $("#enviar").click(function(e){
          e.preventDefault();
          console.log("----???",data_user);
            $.ajax({
                url:'/account/',
                type: 'POST',
                data: data_user,

                beforeSend:function(){
                    card.hide('blind','fast');
                },
                success:function(response){
                    console.log(response);


                    card.show('blind','fast');
                    $("#verificacion").html("<b>"+'Datos Enviados Correctamente!'+"</b>");
                    $("#verificacion").css('color','green');
                    $("#enviar").hide('fade','fast');
                },
                error:function(){
                    alert("Error del servidor Vuelva a intentarlo");
                    // location.reload();
                }
            });
        });
