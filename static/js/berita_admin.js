$("#friend-form").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var serializedData = $(this).serialize();
    $.ajax({
      type : 'POST',
      url : "/berita/",
      data : serializedData,
      success : show_all(),
    })
})

function show_all(){
  $("#friend-form").trigger('reset');
  $("#create").hide()
  $("#show").show()
    $.get("/berita/json", function(data){
        $("#container").html("")
        for(let i = 0; i < data.length; i++){
            let d = new Date(data[i].fields.date.substring(0,10));
            const date = d.toDateString()
            $("#container").append(`<div class="card bg-primary text-primary-content w-full">
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
  <a class="btn btn-error" onclick="deleteBerita(${data[i].pk})">Delete</a>
</div>
</div>`)
        }
    })
}

$(document).ready(function(){
      show_all();
  });

function show_filter(filter){
  $("#create").hide()
  $("#show").show()
    $.get(`/berita/json`, function(data){
        $("#container").html("")
        for(let i = 0; i < data.length; i++){
            if(data[i].fields.category == filter){
            let d = new Date(data[i].fields.date.substring(0,10));
            const date = d.toDateString()
            $("#container").append(`<div class="card bg-primary text-primary-content w-full">
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
  <a class="btn btn-error" onclick="deleteBerita(${data[i].pk})">Delete</a>
</div>
</div>`)}
        }
    })
}

function deleteBerita(id){
    $.ajax({
      url: `/berita/delete/${id}`,
      type: "DELETE",
      headers: {
        "X-CSRFToken": getCookie("csrftoken")
      },
    success: function(){
        show_all();
    },
  })}


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

function createBerita(){
$("#show").hide()
$("#create").show()
}

function update(){
    $.ajax({
      url: "/berita/",
      method: "POST",
      headers: {
        "X-CSRFToken": getCookie("csrftoken")
      },
      dataType    : 'json', // what type of data do we expect back from the server
    success: function(){
        show_all();
    },
  })}