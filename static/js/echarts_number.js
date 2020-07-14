$(document).ready(function(){
      $.ajax({
           type: "GET",
           url: "http://localhost:5000/redis",
           dataType: "json",
           success: function(data){
                document.getElementById("cookie-number").innerHTML = data["cookie_number"];
                document.getElementById("cookie-expire").innerHTML = data["cookie_expire"];
                document.getElementById("name-to-url").innerHTML = data["name_to_url"];
                document.getElementById("relationship").innerHTML = data["relationship"];
           }
      });
});
