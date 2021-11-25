$(document).ready(function() {
    
    let $submit = $('button');//creates jquery object containing all buttons

    $submit.each(function() {
        $(this).on('click', function(evt) {
            evt.preventDefault();
        });
    });
    
    $("#query_submit_1").on('click', function(evt) {
        evt.preventDefault();
        let lat = $("#lat").val();
        lat = lat.replace(/\s/g,'');
        let long = $("#long").val();
        long = long.replace(/\s/g,'');

        if (isNaN(lat) ||isNaN(long)) {
            alert("Please enter number values for lat and long!");
            $("#lat").val("");
            $("#long").val("");
        }
    });
    $("#query_submit_3").on('click', function(evt) {
        evt.preventDefault();
        let zip = $("#zip").val();
        zip = zip.replace(/\s/g,'');

        if (isNaN(zip)) {
            alert("Please enter a number value for zip code!");
            $("#zip").val("");
        }
    });
});