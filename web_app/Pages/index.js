$(document).ready(function() {
    
    let $navLink = $('.nav-link');//creates jquery object containing all buttons

    $navLink.each(function() {
        $(this).on('click', function(evt) {
            evt.preventDefault();
            //let page = this.attr('href');
            $.ajax({
				type: "get",
				url: "stats.json",
				dataType: "json",
				success: function (data) {
					let $main = $("index_main");
					$main.html("");

					$main.html(data.stats);
				},
				error:   function (xhr, status, err) {
					alert('something went wrong' + xhr.status + err);
				}
			});
        });
    });
    
    $('#query_submit_1').on('click', function(evt) {
        evt.preventDefault();
        let lat = $('#lat').val();
        lat = lat.replace(/\s/g,'');
        let long = $('#long').val();
        long = long.replace(/\s/g,'');

        if (isNaN(lat) ||isNaN(long)) {
            alert("Please enter number values for lat and long!");
            $('#lat').val("");
            $('#long').val("");
        }
        else if (!isNaN(lat) && !isNaN(long)) {
            if (lat.length == '' || long.length == '') {
                alert("Please enter a value for both lattitude and longitude!");
            }
            
            $('#lat').val(lat);
            $('#long').val(long);
            $('#query_form_1').submit();
        }


    });

    $('#query_submit_2').on('click', function(evt) {
        evt.preventDefault();;
        let city = $('#city').val
        city.replace(/\s/g,'');

        if (!isNaN(city)) {
            alert("City names do not include numbers!");
        }
        else {
            $('#city').val(city);
            $('#query_form_3').submit();
        }
    });

    $('#query_submit_3').on('click', function(evt) {
        evt.preventDefault();
        let zip = $('#zip').val();
        zip = zip.replace(/\s/g,'');

        if (isNaN(zip)) {
            alert("Please enter a number value for zip code!");
            $('#zip').val("");
        }
        else if (!isNaN(zip)) {
            if (zip.length == '') {
                alert("Please enter a value!");
            }
            else if (zip.length < 5 || zip.length > 5) {
                alert("ZIP code should be 5 digits!");
            }
            else {
                $('#zip').val(zip);
                $('#query_form_3').submit();
            }
        }
    });
});