$(document).ready(function() {
    
    let $navLink = $('.nav-link');//creates jquery object containing all buttons

    $navLink.each(function() {
        $(this).on('click', function(evt) {
            evt.preventDefault();
            let href = $(this).attr('href');

            let $main = $("#index_main");

            $.ajax({
				type: 'GET',
				url: './nav.json',
				dataType: 'json',
				success: function (data) {
                    let html = data[href];
                    $main.html('');
					$main.html(html);
				},
				error:   function (xhr, status, err) {
					alert('something went wrong' + xhr.status + err);
				}
			});
        });
    });
    
    $('#coordinate_submit').on('click', function(evt) {
        evt.preventDefault();
        let $lat = $('#lat');
        let $long = $('#long');
        let lat = $lat.val();
        lat = lat.replace(/\s/g,'');
        let long = $long.val();
        long = long.replace(/\s/g,'');
        lat = parseFloat(lat);
        long = parseFloat(long);

        if (lat.length == '' || long.length == '') {
            alert('Please enter a value for both latitude and longitude!');
        }
        else if (isNaN(lat) || isNaN(long)) {
            alert('Please enter number values for lat and long!');
            $lat.val('');
            $long.val('');
        }
        else if (!isNaN(lat) && !isNaN(long)) {
            $lat.val(lat);
            $long.val(long);
            $('#coordinate_form').submit();
        }


    });

    $('#state_submit').on('click', function(evt) {
        evt.preventDefault();
        let $state = $('#state');
        let state = $state.val();
        state.replace(/\s/g,'');

        if (state.length == '') {
            alert('please enter a value');
        }
        else if (!isNaN(state)) {
            alert('State names do not include numbers!');
        }
        else {
            $state.val(state);
            $('#state_form').submit();
        }
    });

    $('#county_submit').on('click', function(evt) {
        evt.preventDefault();
        let $county = $('#county');
        let county = $county.val();
        county = county.replace(/\s/g,'');

        if (county.length == '') {
            alert('Please enter a value!');
        }
        else if (!isNaN(county)) {
            alert('county name shouldn\'t contain numbers');
        }
        else {
            $county.val(county);
            $('#county_form').submit();
        }
    });
});