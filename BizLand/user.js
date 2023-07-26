
var USERNAME = "mishal"
function allcontent(){
    $.ajax({
        url: "http://localhost:8001/" + 'getactivepackages/',
        type: "GET",
        success: function (data) {
            document.getElementById("insidethis").innerHTML = ""
            document.querySelectorAll("#alllist li a").forEach((e)=>{e.classList.remove("active")})
            document.getElementById("allcontent").classList.add("active")
            for (i in data){

                let carddetails = `<div style="cursor:pointer" class="col-md-6 col-lg-3 d-flex align-items-stretch mb-5"> \
                        <div style="width: -webkit-fill-available;" class="icon-box" data-aos="fade-up" data-aos-delay="100"> \
                        <div class="icon"><i class="bx bxl-dribbble"></i></div> \
                        <h4 class="title"><a href="">${data[i].package.name}</a></h4> \
                        <h5 class="description">${data[i].package.destination}</h5> \
                        <p class="description">Start date: ${data[i].start_date}</p> \
                        <p class="description">End date: ${data[i].end_date}</p> \
                        <p class="description">Last date of Booking: ${data[i].last_date_of_booking}</p> \
                        <p class="description">Vacancies: ${data[i].vacancies}/${data[i].package.no_of_people}</p> \
                        <div class="pricing"><a href="#" style="background: seagreen;" onclick="apply('${data[i].package.name}')" class="btn-buy">Apply</a><div>
                        </div> \
                        </div>`
                let wrapper= document.createElement('div');
                wrapper.innerHTML = carddetails
                document.getElementById("insidethis").appendChild(wrapper.firstChild)
                
            }
        }
    });
}

function mycontent(){
    let x = this
    $.ajax({
        url: "http://localhost:8001/" + 'getactivepackages/?user='+USERNAME,
        type: "GET",
        success: function (data) {
            document.getElementById("insidethis").innerHTML = ""
            document.querySelectorAll("#alllist li a").forEach((e)=>{e.classList.remove("active")})
            document.getElementById("mycontent").classList.add("active")
            for (i in data){

                let carddetails = `<div style="cursor:pointer" class="col-md-6 col-lg-3 d-flex align-items-stretch mb-5"> \
                        <div style="width: -webkit-fill-available;" class="icon-box" data-aos="fade-up" data-aos-delay="100"> \
                        <div class="icon"><i class="bx bxl-dribbble"></i></div> \
                        <h4 class="title"><a href="">${data[i].package.name}</a></h4> \
                        <h5 class="description">${data[i].package.destination}</h5> \
                        <p class="description">Start date: ${data[i].start_date}</p> \
                        <p class="description">End date: ${data[i].end_date}</p> \
                        <p class="description">Last date of Booking: ${data[i].last_date_of_booking}</p> \
                        <p class="description">Vacancies: ${data[i].vacancies}/${data[i].package.no_of_people}</p> \
                        <div class="pricing"><a href="#" style="background: maroon;" onclick="cancel('${data[i].package.name}')" class="btn-buy">Cancel</a><div>
                        </div> \
                        </div>`
                let wrapper= document.createElement('div');
                wrapper.innerHTML = carddetails
                document.getElementById("insidethis").appendChild(wrapper.firstChild)
                
            }
        }
    });
}

function apply(packagename){
    let x = this
    $.ajax({
        url: "http://localhost:8001/applypackage/",
        type: "POST",
        data: {username:USERNAME, activepackage:packagename},
        success: function (data) {
            alert(data)
        },
        error: function(e, x, y){
            alert(e.responseText)
        } 
    });
}

function cancel(packagename){
    let x = this
    $.ajax({
        url: "http://localhost:8001/cancelpackage/",
        type: "POST",
        data: {username:USERNAME, activepackage:packagename},
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


