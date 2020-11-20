console.log('register working')

const usernameField=document.querySelector('#usernameField');

usernameField.addEventListener("keyup", () =>{
    console.log('777');
    const usernameVal = e.target.value;
    if (usernameVal.lenght > 0){
        fetch('', {
            body: JSON.stringify({ username: usernameVal}),
            method: "POST",
        }) 
            .then((res)=>res.json())   
            .then((data) =>{
                console.log("data", data)
            });
    }
});