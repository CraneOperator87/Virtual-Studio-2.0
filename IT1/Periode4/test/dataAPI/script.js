//Hente elementer fra HTML
const quizContainer = document.querySelector("#quiz");
const quizCategory = document.querySelector("#category");
const resultContainer = document.querySelector("#result");
const submitButton = document.querySelector("#submit");
const retryButton = document.querySelector("#retry");
const newButton = document.querySelector("#new");

//Initialisere status på Quiz
let currentQuestion = 0;
let score = 0;
let incorrectAnswers = [];

//Viser en spørsmål av gangen til bruker

function displayQuestion() {
  const questionData = quizData[currentQuestion];
  const options = questionData.options;

  const questionElement = document.createElement("article");
  questionElement.className = "question";
  questionElement.innerHTML = questionData.question;

  const optionsElement = document.createElement("div");
  optionsElement.className = "options";

  for (let i = 0; i < options.length; i++) {
    const option = document.createElement("label");
    option.className = "option";

    const radio = document.createElement("input");
    radio.type = "radio";
    radio.name = "quiz";
    radio.value = options[i];

    const optionText = document.createTextNode(options[i]);

    option.appendChild(radio);
    option.appendChild(optionText);
    optionsElement.appendChild(option);
  }

  quizContainer.innerHTML = ""; //fjerne forrige spørsmål og legge en ny spørsmål
  quizContainer.appendChild(questionElement);
  quizContainer.appendChild(optionsElement);
}

/*Kalles når bruker klikker på "Send Svar". 
  Sjekker om riktig svar ble valgt og oppdaterer score og liste over feil svar
  Hvis vi har nådd siste spørsmål, viser resultat
  */
function checkAnswer() {
  const selectedOption = document.querySelector('input[name="quiz"]:checked');
  if (selectedOption) {
    const answer = selectedOption.value;
    if (answer === quizData[currentQuestion].answer) {
      score++;
    } else {
      incorrectAnswers.push({
        question: quizData[currentQuestion].question,
        incorrectAnswer: answer,
        correctAnswer: quizData[currentQuestion].answer,
      });
    }
    //Henter neste spørsmål, hvis det er noe spørsmål igjen.
    currentQuestion++;
    selectedOption.checked = false;
    if (currentQuestion < quizData.length) {
      displayQuestion();
    } else {
      displayResult();
    }
  }
}

//Viser Antall riktig spørsmål
function displayResult() {
  quizContainer.style.display = "none";
  submitButton.style.display = "none";
  retryButton.style.display = "inline-block";
  newButton.style.display = "inline-block";
  resultContainer.innerHTML = `You scored ${score} out of ${quizData.length}!`;
}

function newQuiz(retry) {
  currentQuestion = 0;
  score = 0;
  incorrectAnswers = [];
  quizContainer.style.display = "block";
  submitButton.style.display = "inline-block";
  retryButton.style.display = "none";
  newButton.style.display = "none";
  resultContainer.innerHTML = "";
  if (retry) {
    displayQuestion();
  } else {
    startQuiz();
  }
}

submitButton.addEventListener("click", checkAnswer);
retryButton.addEventListener("click", function () {
  newQuiz(true);
});
newButton.addEventListener("click", function () {
  newQuiz(false);
});

//Henter quiz data from API
async function getQuizData(url) {
  const response = await fetch(url);
  if (response.status != 200) {
    //gi tilbakemelding til bruker
    alert("Feil når jeg hentet spørsmålene");
    return [];
  }

  const data = await response.json();
  const quizData = [];

  for (result of data.results) {
    quizData.push({
      question: result.question,
      options: [...result.incorrect_answers, result.correct_answer].sort(
        () => Math.random() - 0.5
      ), // Randomize options
      answer: result.correct_answer,
    });
    quizCategory.innerHTML = result.category;
  }
  return quizData;
}

//Henter spørsmålene fra Quiz-database-API
async function startQuiz() {
  const categorier = [16, 18, 21, 24, 26];
  category = String(categorier[Math.floor(Math.random() * 4)]);
  quizData = await getQuizData(
    `https://opentdb.com/api.php?amount=5&category=${category}&difficulty=easy`
  );
  if (quizData.length > 0) {
    displayQuestion();
  }
}

startQuiz();
