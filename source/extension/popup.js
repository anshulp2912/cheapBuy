$(document).ready(function(){
		$.getJSON('http://localhost:5000/fetch',function(data){
			$.each(data,function(index){
					document.write("<p>Description : "+data[index].description+"<br>");
					document.write("URL : "+data[index].url+"<br>");
					document.write("Price : "+data[index].price+"<br>");
					document.write("Site : "+data[index].site+"<br>");
					document.write("<br></p>")
			});
	});
});