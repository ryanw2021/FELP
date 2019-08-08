function credentialsSubmitted() {
    document.getElementById('invalid-inputs').innerHTML='';
    var submittedEmail = document.getElementById('email-input').value;
    var submittedPassword = document.getElementById('password-input').value;
    if(submittedEmail != "" && submittedPassword != "") {
        console.log(submittedEmail);
        console.log(submittedPassword);
    }
    else {
        document.getElementById('invalid-inputs').innerHTML='Please enter a valid username and password.';
    }
}