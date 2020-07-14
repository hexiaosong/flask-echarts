$(document).ready(function(){
      $.ajax({
           type: "GET",
           url: "http://localhost:5000/number",
           dataType: "json",
           success: function(data){
                document.getElementById("cookie-number").innerHTML = data["cookie_num"];
           }
      });
});
