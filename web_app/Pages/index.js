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
                    if (href !== 'choromap') {
                        let html = data[href];
                        $main.html('');
                        $main.html(html);
                    }
                    else if (href == 'choromap') {
                        $main.load('./choromap.html')
                    }
				},
				error:   function (xhr, status, err) {
					alert('something went wrong' + xhr.status + err);
				}
			});
        });
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
            $state.val('');
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
            $county.val('');
        }
        else {
            $county.val(county);
            $('#county_form').submit();
        }
    });

    $('#aqi_submit').on('click', function(evt) {
        evt.preventDefault();
        let $aqi = $('#aqi');
        let aqi = $aqi.val();
        aqi = aqi.replace(/\s/g,'');

        if (aqi.length == '') {
            alert('Please enter a value!');
        }
        else if (isNaN(aqi)) {
            alert('AQI value should be numeric!');
            $aqi.val('');
        }
        else {
            $aqi.val(aqi);
            $('#aqi_form').submit();
        }
    });
});