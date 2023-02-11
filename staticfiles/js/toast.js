
function displayToast(event){
    const toastDiv = document.getElementById("toastDiv")
        console.log(toastDiv)
        toastDiv.style.display = "inline-block"    
}

window.onload = function(){
    const loginCard = document.getElementById("loginCard")
    console.log(loginCard)
    displayToast(event);
}



