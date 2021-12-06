const target = document.getElementById('target');
const target_value = parseInt(target.getAttribute('data-target'));

const records = document.querySelectorAll(".quantity");

for (let record of records) {
    let icon = record.parentElement.children[2]
    if (parseInt(record.innerText) < target_value) {
        icon.setAttribute("class", "fas fa-times-circle fa-2x has-text-danger")
    } else {
        icon.setAttribute("class", "fas fa-check-square fa-2x has-text-success")
    }

}
