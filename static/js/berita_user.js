function show_all(){
    $.get("/berita/json", function(data){
        $("#container").html("")
        for(let i = 0; i < data.length; i++){
            let d = new Date(data[i].fields.date.substring(0,10));
            const date = d.toDateString()
            $("#container").append(`<div class="card bg-primary text-primary-content">
<div class="card-body">
<h2 class="card-title">${data[i].fields.title}</h2>
<ol class="list-disc">
<li>Added : ${date}</li>
<li>Category : ${data[i].fields.category}</li>
<li>Writer : ${data[i].fields.writer}</li>
</ol>
</div>
<div class="card-actions justify-end">
  <a class="btn btn-primary" href="/berita/show/${data[i].pk}">Show More</a>
  
</div>
</div>`)
        }
    })
}

$(document).ready(function(){
      show_all();
  });

function show_filter(filter){
    $.get(`/berita/json`, function(data){
        $("#container").html("")
        for(let i = 0; i < data.length; i++){
            if(data[i].fields.category == filter){
            let d = new Date(data[i].fields.date.substring(0,10));
            const date = d.toDateString()
            $("#container").append(`<div class="card bg-primary text-primary-content">
<div class="card-body">
<h2 class="card-title">${data[i].fields.title}</h2>
<ol class="list-disc">
<li>Added : ${date}</li>
<li>Category : ${data[i].fields.category}</li>
<li>Writer : ${data[i].fields.writer}</li>
</ol>
</div>
<div class="card-actions justify-end">
  <a class="btn btn-primary" href="/berita/show/${data[i].pk}">Show More</a>
  
</div>
</div>`)}
        }
    })
}




function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
