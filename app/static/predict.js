// $('#predict_submit_button').click(function() {
//     $.ajax({
//         url:'/predict_______' + $('#predict_parameters').val(),
//         type: 'GET',
//         success: function (response) {
//             $('#predict_response').innerText = response
//         }
//     });
// });
// <input type="submit" value="Find Optimized Rent!" className="primary">
// function revealMessage() {
//     document.getElementById("hiddenMessage").style.display="block";
// };
document.getElementById('predict_rent').onclick = function(){
    document.getElementById("hiddenMessage").style.display="block";
};

// adapting the above code in Jquery and updating
// $('#predict_rent').click(function(){
//     $.ajax({url: '/features_parameters', type: 'GET', data: {'features_parameters': $('#neighbourhood-group').value}, dataType: 'json'});
// });

// $.ajax({url: '/landing.html', type: 'GET', data: {'features_parameters': $('#neighbourhood-group').value}, dataType: 'json'});