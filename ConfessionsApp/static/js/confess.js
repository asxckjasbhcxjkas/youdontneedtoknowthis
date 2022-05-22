window.onload = function (){
    const confessBtn = document.getElementById('confess-btn');
    confessBtn.onclick = function() {
        confessBtn.style = "display: none";
        const loader = document.createElement('div');
        loader.classList.add("spinner-border", "text-success", "mb-5", "mt-3")
        loader.innerHTML = `<span class="visually-hidden">Loading...</span>`;
        confessBtn.parentNode.appendChild(loader);
    }
}