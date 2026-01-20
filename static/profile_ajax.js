$(document).ready(function(){
    console.log('Profile ajax loaded successfully.');

    $('#save_student_btn').click(function(event){
        event.preventDefault();
        console.log(`Save Button Clicked.`);

        // Get form values
        let student_id = $('#student_id').val();
        let student_name = $('#student_name').val();
        let email = $('#email').val();
        let age = $('#age').val();
        let profile_image = $('#profile_image')[0].files[0]; // Get file object
        let csrf_token = $('input[name=csrfmiddlewaretoken]').val();

        // Create FormData object for file upload
        let formData = new FormData();
        formData.append('student_id', student_id);
        formData.append('student_name', student_name);
        formData.append('email', email);
        formData.append('age', age);
        if (profile_image) {
            formData.append('profile_image', profile_image);
        }
        formData.append('csrfmiddlewaretoken', csrf_token);

        // Show loading state
        $('#save_student_btn').text('Saving...').prop('disabled', true);

        $.ajax({
            url: `/student/add/`,
            method: 'POST',
            data: formData,
            processData: false,  // Important for file upload
            contentType: false,  // Important for file upload
            success: function(response){
                console.log('Success:', response);
                
                // Show success message
                $('#acknowledge').text(response.message)
                    .css('color', 'green')
                    .fadeIn();

                // Redirect to student list page after 1 second
                setTimeout(function(){
                    window.location.href = response.redirect_url;
                }, 1000);
            },
            error: function(err){
                console.log('Error:', err);
                let errorMsg = err.responseJSON?.message || 'An Error Occurred';

                // Show error message
                $('#acknowledge').text(errorMsg)
                    .css('color', 'red')
                    .fadeIn().delay(3000).fadeOut();

                // Reset button
                $('#save_student_btn').text('Save').prop('disabled', false);
            }
        });

    });
});