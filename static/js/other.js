// function searchsongs(){
//     let artist_name=$('#artist_name').val()
//     alert('artist_name')
//     $.ajax({
//         url:"/"+artist_name,
//         type:'GET',
//         datatype:'json',
//         data: {
//             'artist_name':artist_name,
//         },
//         // alert(artist_name)
//         success :function(res){
//             console.log("success")
//             $('#single_song').append(
//                 '<div  class="single-album">'+
//                             '<img src="./media/'{{res.image}}'" alt="">'+
//                             '<div class="album-info">'+
//                                 '<a href="#">'+
//                                     '<h5 id="artist_name">'{{res.song_path}}'</h5>'+
//                                 '</a>'+
//                                 '<p>Second Song</p>'+
//                            ' </div>'+
//                 '</div>'
//             )
//             console.log("completed")
//         },
//     });
// }




function searchsongs(artist_name){
    // var artist_name=document.getElementById('artist_name').innerHTML
    // alert(artist_name)
    $.get("/artist/"+artist_name,function(data,status){
        alert("success")
        $('#single_song').html('');
        // $('#miscellaneous').html('');
        for(var s in data){
            // $('#para').append(s);
            $('#single_song').append(
                '<div class="col-12">'+
                    '<div class="single-song-area mb-30 d-flex flex-wrap align-items-end">'+
                        '<div class="song-play-area">'+
                            '<div class="song-name">'+
                                '<p>'+data[s]+'</p>'+
                            '</div>'+
                            '<audio preload="auto" controls>'+
                                '<source src="/media/'+s+'">'+
                            '</audio>'+
                        '</div>'+
                    '</div>'+
                '</div>'
                
            )

        }
        
    })
  };










  