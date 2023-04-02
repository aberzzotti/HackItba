
function Enviar(){
  
   let barrio=document.getElementById("barrio").value
   let cant =document.getElementById("cant").value.toString()
   let min =document.getElementById("min").value.toString()
   let max =document.getElementById("max").value.toString()
  alert("Usted se ha registrado exitosamente , pronto le llegará un mail con información")
  $.ajax({
    url:"/mail",
    type:"POST",
    data:{"barrio":barrio,"cant":cant,"min":min,"max":max},
    success: function(response) {
      console.log(response) 

    },
    error: function(error){
      console.log(error)
    }
  })
}
function agregarUsuario(){
  
 alert("Usuario registrado con exitos")
}