function createAccount(){
    var errorLink = document.getElementById('invalid-inputs')
    if(document.getElementById('tos-checkbox').checked == true){
        var firstName=document.getElementById('first-name-input').value;
        var lastName=document.getElementById('last-name-input').value;
        var email=document.getElementById('email-input').value;
        var password=document.getElementById('password-input').value;
        if(firstName != '' && lastName != '' && email != '' && password != ''){
            if(password == document.getElementById('confirm-password-input').value) {
                errorLink.style.backgroundColor='#91ffa0'
                errorLink.innerHTML="Account creation successful, click here to return to login";
                errorLink.href='login';

                var fullName=firstName + " " + lastName;
                console.log(fullName);
                //Create Account in Database or something
            }
            else{
                errorLink.innerHTML='Passwords do not match';
            }
        }
        else {
            errorLink.innerHTML='Please complete all of the fields.';
        }
    }
    else{
        errorLink.innerHTML='You must agree to our terms of service to use our product.'
    }
}