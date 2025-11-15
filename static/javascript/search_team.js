document.addEventListener("DOMContentLoaded", () =>{
    const dingSound = document.getElementById("dingSound");

    if (window.errorAlert){
        dingSound.currentTime = 0;
        dingSound.play();
        showAlertModal("⚠️ Failed to create account!", errorAlert);
    }

});

function showAlertModal(title, message) {
// Update modal content
document.getElementById("modalTitle").innerText = title;
document.getElementById("modalBody").innerText = message;

// Initialize and show the modal
const modal = new bootstrap.Modal(document.getElementById("alertModal"));
modal.show();

}


const navbar = document.querySelector("nav");
navbar.style.pointerEvents = "none";
navbar.style.opacity = "0";
let input = document.querySelector("input")
input.addEventListener("input", async function(){
    let response = await fetch("/search_team?q=" + input.value);
    let teams = await response.json();
    let html = '';
    for (let team of teams){
        html += `<div class="mb-3"> <button style="margin-right: 25px;" type="submit" name="team" value="${team.current_club_name}" class="btn btn-primary">` + team.current_club_name+ '</button> </div>'
    }
    document.querySelector("#teams").innerHTML = html;
});
