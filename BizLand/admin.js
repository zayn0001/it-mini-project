var USERNAME = "jasar"
function allcontent(endpoint){
    $.ajax({
        url: "http://localhost:8001/" + 'getactivepackages/' +"?admin=" + USERNAME,
        type: "GET",
        success: function (data) {
            document.getElementById("insidethis").innerHTML = ""
            document.querySelectorAll("#alllist li a").forEach((e)=>{e.classList.remove("active")})
            document.getElementById("allcontent").classList.add("active")
            for (i in data){

                let carddetails = `<div style="cursor:pointer" class="col-md-6 col-lg-3 d-flex align-items-stretch mb-5"> \
                        <div style="width: -webkit-fill-available;" class="icon-box" data-aos="fade-up" data-aos-delay="100"> \
                        <div onclick="myactivepackage('${data[i].package.name}');" class="icon"><i class="bx bxl-dribbble"></i></div> \
                        <h4 onclick="myactivepackage('${data[i].package.name}');" class="title"><a href="">${data[i].package.name}</a></h4> \
                        <h5 onclick="myactivepackage('${data[i].package.name}');" class="description">${data[i].package.destination}</h5> \
                        <p onclick="myactivepackage('${data[i].package.name}');" class="description">Start date: ${data[i].start_date}</p> \
                        <p onclick="myactivepackage('${data[i].package.name}');" class="description">End date: ${data[i].end_date}</p> \
                        <p onclick="myactivepackage('${data[i].package.name}');" class="description">Last date of Booking: ${data[i].last_date_of_booking}</p> \
                        <p onclick="myactivepackage('${data[i].package.name}');" class="description">Vacancies: ${data[i].vacancies}/${data[i].package.no_of_people}</p> \
                        <div class="pricing"><a href="#" style="background: maroon;margin-top: 1rem;" onclick="deactivate('${data[i].package.name}')" class="btn-buy">Deactivate</a><div> \
                        </div> \
                        </div>`
                let wrapper= document.createElement('div');
                wrapper.innerHTML = carddetails
                document.getElementById("insidethis").appendChild(wrapper.firstChild)
                
            }
        }
    });
}

function myactivepackage(packagename){
    $.ajax({
        url: "http://localhost:8001/" + 'getparticipants/' +"?package=" + packagename,
        type: "GET",
        success: function (data) {
            document.getElementById("insidethis").innerHTML = "<h2>Participants<h2>"
            document.querySelectorAll("#alllist li a").forEach((e)=>{e.classList.remove("active")})
            document.getElementById("allcontent").classList.add("active")
            for (i in data){
                let carddetails = `<div style="cursor:pointer" class="col-md-6 col-lg-3 d-flex align-items-stretch mb-5"> \
                        <div style="width: -webkit-fill-available;" class="icon-box" data-aos="fade-up" data-aos-delay="100"> \
                        <div class="icon"><i class="bx bxl-dribbble"></i></div> \
                        <h4 class="title"><a href="">${data[i].username}</a></h4> \
                        <h5 class="description">${data[i].first_name} ${data[i].last_name}</h5> \
                        <p class="description">${data[i].email}</p> \
                        <p class="description">${data[i].phone}</p> \
                        <div class="pricing"><a href="#" style="background: maroon;" onclick="reject('${data[i].username}','${packagename}')" class="btn-buy">Reject</a><div>
                        </div> \
                        </div>`
                let wrapper= document.createElement('div');
                wrapper.innerHTML = carddetails
                document.getElementById("insidethis").appendChild(wrapper.firstChild)
                
            }
        }
    });
}

function mypackages(){
    $.ajax({
        url: "http://localhost:8001/" + 'getpackages/' +"?admin=" + USERNAME,
        type: "GET",
        success: function (data) {
            document.getElementById("insidethis").innerHTML = ""
            document.querySelectorAll("#alllist li a").forEach((e)=>{e.classList.remove("active")})
            document.getElementById("allcontent").classList.add("active")
            for (i in data){
                let carddetails = `<div style="cursor:pointer" class="col-md-6 col-lg-3 d-flex align-items-stretch mb-5"> \
                        <div style="width: -webkit-fill-available;" class="icon-box" data-aos="fade-up" data-aos-delay="100"> \
                        <div class="icon"><i class="bx bxl-dribbble"></i></div> \
                        <h4 class="title"><a href="">${data[i].name}</a></h4> \
                        <h5 class="description">${data[i].destination}</h5> \
                        <h5 class="description">${data[i].description}</h5> \
                        <p class="description">No. of people: ${data[i].no_of_people}</p> \
                        <p class="description">Cost per head: ${data[i].cost_per_head}</p> \
                        <p class="description">No. of days: ${data[i].no_of_days}</p> \
                        <div class="pricing"><a href="#" style="background: maroon;margin-top: 1rem;" onclick="activate('${data[i].name}')" class="btn-buy">Activate</a><div> \
                        <div class="pricing"><a href="#" style="background: maroon;margin-top: 1rem;" onclick="delete('${data[i].name}')" class="btn-buy">Delete</a><div> \
                        </div> \
                        </div>`
                let wrapper= document.createElement('div');
                wrapper.innerHTML = carddetails
                document.getElementById("insidethis").appendChild(wrapper.firstChild)
                
            }
        }
    });
}
function createpack(){
    let formdetails = `
    <div id="contact" class="contact">
    <form method="post" role="form" id="myform" class="php-email-form">
        <div class="form-group">
        <input type="text" class="form-control" name="name" id="name" placeholder="Name" required="">
        </div>
        <div class="form-group" style="display:none">
        <input type="text" class="form-control" name="admin" id="admin" placeholder="Admin" required="" value=${USERNAME}>
        </div>
        <div class="row">
        <div class="col form-group">
            <input type="number" name="no_of_people" class="form-control" id="no_of_people" placeholder="No. of people" required="">
        </div>
        <div class="col form-group">
            <input type="number" class="form-control" name="no_of_days" id="no_of_days" placeholder="No. of Days" required="">
        </div>
        </div>
        <div class="row">
        <div class="col form-group">
            <input type="text" name="destination" class="form-control" id="destination" placeholder="Destination" required="">
        </div>
        <div class="col form-group">
            <input type="number" class="form-control" name="cost_per_head" id="cost_per_head" placeholder="Cost per head" required="">
        </div>
        </div>
        
        <div class="form-group">
        <textarea class="form-control" name="description" rows="5" placeholder="Description" required=""></textarea>
        </div>
        <div class="my-3">
        <div class="loading">Loading</div>
        <div class="error-message"></div>
        <div class="sent-message">Your message has been sent. Thank you!</div>
        </div>
        <div class="text-center"><button type="submit" >Create</button></div>
    </form>
    </div>`
    document.getElementById("insidethis").innerHTML = formdetails

    $('#myform').submit(function(e){
        e.preventDefault();
        $.ajax({
            url: 'http://localhost:8001/createpackage/',
            type: 'post',
            data:$('#myform').serializeArray(),
            success:function(){
                allcontent()
            }
        });
    });
}

function activate(packagename){
    let formdetails = `
    <div id="contact" class="contact">
    <form method="post" role="form" id="myother" class="php-email-form">

        

        <div class="form-group">
        <input type="text" class="form-control" name="package" id="package" placeholder="Admin" required="" value='${packagename}' readonly="">
        </div>

        <div class="row">
        <div class="col form-group">
            <input type="date" name="start_date" class="form-control" id="start_date" placeholder="Start Date" required="">
        </div>
        <div class="col form-group">
            <input type="date" class="form-control" name="end_date" id="end_date" placeholder="End Date" required="">
        </div>
        </div>

        <div class="form-group">
        <input type="date" class="form-control" name="last_date_of_booking" id="last_date_of_booking" placeholder="Last Date" required="">
        </div>
        
        <div class="my-3">
        <div class="loading">Loading</div>
        <div class="error-message"></div>
        <div class="sent-message">Your message has been sent. Thank you!</div>
        </div>
        <div class="text-center"><button type="submit" >Create</button></div>
    </form>
    </div>`
    document.getElementById("insidethis").innerHTML = formdetails

    $('#myother').submit(function(e){
        e.preventDefault();
        $.ajax({
            url: 'http://localhost:8001/activatepackage/',
            type: 'post',
            data:$('#myother').serializeArray(),
            success:function(){
                allcontent()
            }
        });
    });
}

function deactivate(packagename){
    $.ajax({
        url: 'http://localhost:8001/deactivatepackage/',
        type: 'post',
        data:{package:packagename},
        success:function(){
            allcontent()
            alert("deactivated")
        }
    });
}

function reject(username, packagename){
    let x = this
    $.ajax({
        url: "http://localhost:8001/cancelpackage/",
        type: "POST",
        data: {username:username, activepackage:packagename},
        success: function (data) {
            alert(data)
        },
        error: function(e, x, y){
            alert(e.responseText)
        } 
    });
}
allcontent()
document.querySelector("#username a").innerHTML = USERNAME