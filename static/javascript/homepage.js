console.log("js.active")
const observer = new IntersectionObserver((entries) =>{
    entries.forEach((entry)=>
    {
        if(entry.isIntersecting)
        {
            console.log(entry.target)
            entry.target.classList.add("show")
        }
        else
        {
            entry.target.classList.remove("show")
        }
    })
}, {})


const sectionElements = document.querySelectorAll(".mb-3")
sectionElements.forEach(el => observer.observe(el))


function showAlertModal(title, message) {
  // Update modal content
  document.getElementById("modalTitle").innerText = title;
  document.getElementById("modalBody").innerText = message;

  // Initialize and show the modal
  const modal = new bootstrap.Modal(document.getElementById("alertModal"));
  modal.show();

  }

  const generalPlayButton = document.querySelector("#generalPlayButton")
  const startButton = document.querySelector("#startButton")
  const guessPlayButton = document.querySelector("#guessPlayButton")
  const bestOfPlayButton = document.querySelector("#bestOfPlayButton")

  generalPlayButton.addEventListener("click", () => {
      let rules = `You have 60 seconds to answer a set of questions.
        Each correct answer earns you 3 point!

        A countdown will immediately start after you select a team and every question there in will be asked based on the team you have chosen.`
        showAlertModal("Rules!", rules)

      startButton.addEventListener("click",() => {
      window.location.href = "/general_quiz";
  });
  });

    guessPlayButton.addEventListener("click", () => {
      let rules = `You have 60 seconds to figure out the name of a player/ manager based on statistic hints.

        A countdown will immediately begin as soon as you press start.
        Each correct answer earns you 6 points

        2 points will be deducted for every questition answered incorrectly`
        showAlertModal("Rules!", rules)
      startButton.addEventListener("click",() => {
      window.location.href = "/guess";
  });
  });


    bestOfPlayButton.addEventListener("click", () => {
      let rules = `You have 60 seconds to figure out an answer from a set of different stat based questions. Questions are asked based on team performance from a random competition and season.

        A countdown will immediately begin as soon as you press start.
        Each correct answer earns you 6 points

        2 points will be deducted for every questition answered incorrectly`
        showAlertModal("Rules!", rules)

      startButton.addEventListener("click",() => {
      window.location.href = "/bestOf";
  });
  });
