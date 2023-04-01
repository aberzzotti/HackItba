function cargarSelect() {

  $.ajax({
    url:"/barrios",
    type:"GET",
    success: function(response) {
      console.log(response)  
      let tabla = "";
          for (let i = 0; i < response.length; i++) {
          tabla += '<option>' + response[i][0] + '</option>'
      }
      document.getElementById("select").innerHTML += tabla;
    },
    error: function(error){
      console.log(error)
    }
  })

}