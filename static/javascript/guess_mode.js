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
              tickSound.pause();
              tickSound.currentTime = 0;
            //play dingsound
              dingSound.currentTime = 0;
              dingSound.play()

              endGame();
        }
    }, 1000);
}

function endGame() {
    gameOver = true;
    answersEl.innerHTML = "";
    document.querySelector("#question").innerHTML = `<h1> ❌Time's up!</h1>`;
    document.querySelector("#response").innerHTML = `<div style="color:yellow;"><h2>Game Over! Final Score: ${points}</h2></div>`;
    document.querySelector("#response").innerHTML += `<button class="btn btn-primary" onclick="window.location.reload()">Play Again</button>`;
    document.querySelector("#response").innerHTML += `<form action="/points" method="post" style="margin-top: 10px"><button name="points" value=${points} class="btn btn-primary">Quit Game</button></form>`;
}



  const input = document.querySelector("input");
  const questionEl = document.querySelector("#question");
  const answersEl = document.querySelector("#answers");
  const responseEl = document.querySelector("#response");

  const trivia = window.trivia
  const possibleAnswers = window.possibleAnswers
  const correctAns = window.correctAns


  let points = 0;
  let currentAnswer = null; // track current answer

  if (trivia) {
    displayQuestion(trivia, possibleAnswers, correctAns);
    startGameTimer();
  }


  function displayQuestion(trivia, questionData, correctAns) {
    if (gameOver) return;
    answersEl.innerHTML = "";
    const question = trivia;
    questionEl.innerHTML = `<h1>${question}</h1>`;

    questionData.forEach(answer => {
      const button = document.createElement("button");
      button.textContent = answer;

      button.addEventListener("click", async function(event){
        if (gameOver) return;
        if ( answer === correctAns){
          points += 6;
          button.classList.add("correct");
          responseEl.innerHTML = `<h3 style="color:green;">Correct! Points: ${points}</h3>`;
        } else {
          points -= 2;
          if (points <= 0){
            points = 0
          }
          button.classList.add("incorrect");
          responseEl.innerHTML = `<h3 style="color:red;">Incorrect! Correct Answer: ${correctAns}. Points: ${points}</h3>`;
        }
        document.querySelectorAll(".answers-grid button").forEach(btn => btn.disabled = true);
        await retrieve()
      });
      answersEl.appendChild(button)
    });

  }






  async function retrieve() {
    try {
      const response = await fetch("/retrieve?q=guess");
      const [newTrivia, newPossibleAns, newAns] = await response.json();
      displayQuestion(newTrivia, newPossibleAns, newAns);
    } catch (error) {
      console.error("Error fetching new trivia:", error);
      responseEl.innerHTML = `<div style="color:red;">Error fetching new question. Please try again.</div>`;
    }
  }
