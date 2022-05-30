window.onload = function (){
    const submitBtn = document.getElementById('submitBtn');
    console.log(submitBtn);
    submitBtn.onclick = function() {
        submitBtn.style = "display: none";
        const loader = document.createElement('div');
        loader.classList.add("spinner-border", "text-success", "mb-5", "mt-3")
        loader.innerHTML = `<span class="visually-hidden">Loading...</span>`;
        submitBtn.parentNode.appendChild(loader);
    }
}