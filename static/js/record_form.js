const quantityInput = document.querySelector('input')
const saveButton = document.getElementById('save')

if (quantityInput.value !== '') {
    saveButton.setAttribute("type", "submit")
}

quantityInput.addEventListener('input', (e) => {
    if (e.target.value === '') {
        saveButton.removeAttribute("type")
    }
    if (e.target.value !== '') {
        saveButton.setAttribute("type", "submit")
    }
})