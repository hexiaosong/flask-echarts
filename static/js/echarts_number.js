$(document).ready(function(){
      $.ajax({
           type: "GET",
           url: "http://192.168.34.10:5000/number",
           dataType: "json",
           success: function(data){
                document.getElementById("cookie-number").innerHTML = data["cookie_number"];
                document.getElementById("cookie-expire").innerHTML = data["cookie_expire"];
                document.getElementById("name-to-url").innerHTML = data["name_to_url"];
                document.getElementById("relationship").innerHTML = data["relationship"];
                document.getElementById("num1").innerHTML = data["num1"];
                document.getElementById("num2").innerHTML = data["num2"];
                document.getElementById("num3").innerHTML = data["num3"];
                document.getElementById("num4").innerHTML = data["num4"];
                document.getElementById("num5").innerHTML = data["num5"];
                document.getElementById("num6").innerHTML = data["num6"];
                document.getElementById("num7").innerHTML = data["num7"];
                document.getElementById("num8").innerHTML = data["num8"];
           }
      });
});
