$(document).ready(function() {
    alert("ready");//alert to show that document is ready
    let $submit = $('button');//creates jquery object containing all buttons
    

    $submit.each(function() {//runs function for each button
        $(this).on('click', function(evt) {//adds event listener for mouse click event
            evt.preventDefault();//prevents default action of submit button which submits the form
            alert("click");//alert to show that a submit button has been clicked
        });
    });
});