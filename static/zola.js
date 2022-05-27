const checkboxes = document.querySelectorAll("#flo");
checkboxes.forEach((btn) => {
btn.addEventListener('change', function(e){
if(e.target.checked){
btn.classList.add("pirlo");
}

})
})

