function sendPostData(){
    const contact_idvalue= document.getElementById("contact_id").value;
    const namevalue = document.getElementById("name").value;
    const fathervalue = document.getElementById("father").value;
    const pincodevalue = document.getElementById("pincode").value;

    const data = {
        contact_id:contact_idvalue,
        name: namevalue,
        father:fathervalue,
        pincode:pincodevalue
    }
    const jsondata=JSON.stringify(data);
//user_post is my api/user/post/ name

fetch("/api/user/post/",{
    method:"POST",
    headers:{
        "Content-Type":"application/json",
        "X-CSRFToken":getCookie("csrftoken")},

    body:jsondata
})
.then(response=> response.json())
.then(result=>{
    console.log("backend response",result);
});
}
function sendPutData(){
    const contact_idvalue= document.getElementById("contact_id").value;
    const namevalue = document.getElementById("name").value;
    const fathervalue= document.getElementById("father").value;
    const pincodevalue= document.getElementById("pincode").value;

    const data={
        contact_id:contact_idvalue,
        name: namevalue,
        father:fathervalue,
        pincode:pincodevalue,
    };
    const transfer = JSON.stringify(data);

    fetch("/api/user/put/",{
        method:"PUT",
        headers:{
            "Content-Type":"application/json",
            "X-CSRFToken":getCookie("csrftoken"),
        },
        body:transfer
    })
    .then(response=> response.json())
    .then(result=>{
        console.log("backend Response",result);
    })
    .catch(error=>{
        console.error("ERROR:",error);
    });

}


