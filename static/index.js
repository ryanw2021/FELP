var events = document.getElementById('events');
var li = document.createElement('li');
li.className = "single_event";
var image = document.createElement('img');
image.src = "https://www.fnasafety.com/wp-content/uploads/2018/10/chipotle-mexican-grill-logo-png-transparent.png";
li.innerHTML = "Chipotle Fundraiser"
var desc = document.createElement('p');
desc.innerHTML = "A description of the event";
desc.className = "description";
var time = document.createElement('p');
time.innerHTML = "Time of the event";
time.className = "time";


li.appendChild(image);
li.appendChild(desc);
li.appendChild(time);

events.appendChild(li)




// var business_name = {business}
// var event_time = {time}
// var event_date = {date}
// var event_description = {description}
// var image_path = {image}


