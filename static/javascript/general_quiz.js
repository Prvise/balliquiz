  const navbar = document.querySelector("nav");
  navbar.style.pointerEvents = "none";
  navbar.style.opacity = "0";
  //timer function
 let timeLeft = 60; // total time for the game
let gameOver = false;
let gameTimer;
const tickSound = document.getElementById("tickSound");
const dingSound = document.getElementById("dingSound");


// Start the global timer once when game begins
function startGameTimer() {
    document.querySelector("#countdown").innerText = timeLeft;
    document.querySelector("#countdown").style.color = "green";

    gameTimer = setInterval(() => {
        timeLeft--;
        document.querySelector("#countdown").innerText = timeLeft;
        tickSound.currentTime = 0;
        tickSound.play();

        // change color when low
        if (timeLeft <= 10) {
            document.querySelector("#countdown").style.color = "red";
        }

        // stop game when time runs out
        if (timeLeft <= 0) {
            clearInterval(gameTimer);
             //stop ticksound
              tickSound.currentTime = 0;
              tickSound.pause();
            //play dingsound
              dingSound.currentTime = 0;
              dingSound.play()
            endGame();
        }
    }, 1000);
}

function endGame() {
    gameOver = true;
    document.querySelector("#question").innerHTML = `<h1> Time's up!</h1>`;
    document.querySelector("#response").innerHTML =
        `<div style="color:yellow;"><h2>Game Over! Final Score: ${points}</h2></div>`;
    document.querySelector("input").disabled = true; // disable input
    document.querySelector("#response").innerHTML += `<button class="btn btn-primary" onclick="window.location.reload()">Play Again</button>`;
    document.querySelector("#response").innerHTML += `<form action="/points" method="post" style="margin-top: 10px"><button name="points" value=${points} class="btn btn-primary">Quit Game</button></form>`;

}



  const input = document.querySelector("input");
  const questionEl = document.querySelector("#question");
  const responseEl = document.querySelector("#response");

  const trivia = window.question

  let points = 0;
  let currentAnswer = null; // track current answer

  input.addEventListener("keypress", async function(event) {
    if (gameOver) return;

    if (event.key === "Enter" && currentAnswer) {
      const userAnswer = input.value.trim().toLowerCase();
      if (userAnswer === currentAnswer.toLowerCase()) {
        points += 3;
        responseEl.innerHTML = `<div style="color:green;"><h3>Correct! Points: ${points}</h3></div>`;
      } else {
        responseEl.innerHTML = `<div style="color:red;"><h3>Incorrect! The correct answer was: ${currentAnswer}</h3></div>`;
      }
      input.value = ""; // clear input

      await retrieve();
    }
  });


  if (trivia) {
    displayQuestion(trivia);
    startGameTimer();
  }


  function displayQuestion(triviaObj) {
    if (gameOver) return;
    const entries = Object.entries(triviaObj);
    const [answer, question] = entries[0];
    currentAnswer = answer;
    questionEl.innerHTML = `<h1>${question}</h1>`;
  }

  async function retrieve() {
    try {
      const response = await fetch("/retrieve?q=general");
      const newTrivia = await response.json();
      displayQuestion(newTrivia);
    } catch (error) {
      console.error("Error fetching new trivia:", error);
      responseEl.innerHTML = `<div style="color:red;">Error fetching new question. Please try again.</div>`;
    }
  }
