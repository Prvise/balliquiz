const navbar = document.querySelector("nav");
navbar.style.pointerEvents = "none";
navbar.style.opacity = "0";


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
