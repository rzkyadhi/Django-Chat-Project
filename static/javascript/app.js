$(document).on('submit','#message-form',function(e){
    e.preventDefault();

    $.ajax({
      type:'POST',
      url:'/send',
      data:{
          username:$('#Username').val(),
          room_id:$('#RoomCode').val(),
          content:$('#content').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(data){
         //alert(data)
      }
    });
    document.getElementById('content').value = ''
  });