# ⚽ Ball IQuiz  

![Flask](https://img.shields.io/badge/Framework-Flask-blue?logo=flask)
![Python](https://img.shields.io/badge/Language-Python-yellow?logo=python)
![JavaScript](https://img.shields.io/badge/Frontend-JavaScript-orange?logo=javascript)
![Bootstrap](https://img.shields.io/badge/Design-Bootstrap-purple?logo=bootstrap)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Completed-success)

###  Web-App link  
[Check the App here](https://balliquiz-1.onrender.com/)

---

## 📘 Table of Contents  
- [Project Overview](#-project-overview)  
- [How It Works](#-how-it-works)  
- [Files and Key Components](#-files-and-key-components)  
- [Data Source](#-data-source)  
- [Design Choices & Challenges](#-design-choices--challenges)  
- [Integration with AI](#-integration-with-ai)  
- [Key Features](#-key-features)  
- [Lessons Learned](#-lessons-learned)  
- [Tech Stack](#-tech-stack)  
- [Setup & Installation](#-setup--installation)  
- [Conclusion](#-conclusion)  
- [Author](#-author)

---

## 🧠 Project Overview  
**Ball IQuiz** is a web-based football trivia game designed as my **CS50x final project**.  

The game allows users to test their football knowledge by answering data-driven trivia questions under a time limit.  
This project reflects the knowledge I aquired through my self taught journey and showcases my ability to combine **backend and frontend development**, apply real-world **data querying**, and create a **dynamic, user-friendly experience** using modern web technologies.  

---

## ⚙️ How It Works  
- Users **register or log in** with a secure account. 
- Upon login in users get to pick from a variaty of **game modes** 
- A **countdown timer** starts as soon as the quiz begins.  
- Players answer a series of **random football-related questions**.  
- **Points are awarded** for each correct answer.  
- Scores are saved to a local **SQLite database**, allowing future retrieval.  

Each session uses randomized questions, ensuring a fresh and challenging experience every time.

---

## 📁 Files and Key Components  

### `app.py`  
The **main Flask file** that powers the application.  
It handles:
- User authentication and session management.  
- Password hashing via `Werkzeug`.  
- Routing between pages.  
- Interaction between frontend (HTML/JS) and the SQLite database.  

User accounts and scores are stored in `accounts.db`, with passwords hashed for security.

---

### Frontend  
Built using:
- **HTML & CSS** for structure and styling.  
- **Bootstrap** for a responsive design that adapts to all screen sizes.  
- **JavaScript** for game logic, timers, user interaction, and dynamic content updates.  

I learned to integrate **Jinja templating syntax** with JavaScript to pass Flask variables directly into client-side logic — a challenge that significantly improved my understanding of web data flow.

---

### `questions.py`  
This module:
- Handles all **data processing** logic.
- Retrieves question data from the football dataset `statistics.db` using SQL queries.  
- Randomizes question selection via Python’s `random` module.  
- Verifies answers and communicates results back to Flask routes.  


---

## 📊 Data Source  
The trivia questions are based on authentic football statistics from  
[**salimt/football-datasets**](https://github.com/salimt/football-datasets).  

It includes detailed information on:
- Player profiles and market values  
- Performance metrics and injury histories  
- National and club competitions  

Using this dataset allowed me to apply real SQL querying skills to extract and organize meaningful quiz questions for my app.

---

## 💡 Design Choices & Challenges  
As someone new to programming, building a **full-stack web app** was both exciting and challenging.  

Some key challenges and takeaways:  
- **Integrating JavaScript and Jinja syntax:** I learned how server-side data can dynamically update client-side scripts.  
- **Responsive design:** Bootstrap helped me ensure that the app looks clean on both mobile and desktop devices.  
- **Timer logic:** Managing countdown timers and sound effects while new questions loaded required careful asynchronous control.  
- **Performance optimization:** I discovered how preloading audio, caching, and file structure affect performance — and how to fix it.  

Every challenge deepened my understanding of **web architecture**, **data handling**, and **asynchronous logic**.

---

## 🤖 Integration with AI  
Throughout the project, I actively used **ChatGPT (OpenAI)** as a collaborative learning tool.  

It helped me:
- Understand complex Flask and JavaScript interactions.  
- Debug efficiently and learn best practices.  
- Explore alternative solutions when I hit obstacles.  
- Improve my technical writing, code organization, and documentation.  

This experience strengthened my ability to **learn quickly**, **communicate effectively**, and **use AI tools responsibly** to accelerate problem-solving — an increasingly valuable skill in modern development environments.

---

## 🧩 Key Features  
✅ User authentication and session tracking  
✅ Football data integrated via SQL queries  
✅ Randomized question selection  
✅ Countdown timer with sound effects  
✅ Responsive layout and animations via Bootstrap  
✅ Real-time feedback for correct/incorrect answers  
✅ Secure password hashing and session management  

---

## 🧠 Lessons Learned  
Through **Ball IQuiz**, I developed foundational and transferable skills, including:
- Building RESTful web apps with **Flask**  
- Writing and querying SQL databases  
- Managing client-server communication via **JSON**  
- Frontend interactivity using **JavaScript**  
- Styling and responsive design using **CSS & Bootstrap**  
- Debugging and improving code performance  
- Collaborating effectively with **AI tools** to solve technical challenges  

This project taught me not just how to code, but how to **think like a developer**.

---

## 🧰 Tech Stack  

| Category | Tools / Technologies |
|-----------|----------------------|
| **Backend** | Flask (Python), Flask-Session, Werkzeug, cs50 |
| **Frontend** | HTML, CSS, Bootstrap, JavaScript |
| **Database** | SQLite (via CS50 SQL module) |
| **Libraries** | random, functools |
| **Other Tools** | Git, GitHub Codespaces, ChatGPT (for AI collaboration) |

---

## 🏁 Conclusion  
**Ball IQuiz** is more than a football game — it’s a reflection of my growth as a self-taught developer.  
In just six months, I went from no coding experience to building a complete full-stack web application.

I plan on learning more and aquiring more skill sets with time and hopefully find myself in a tech environment that will allow me to grow more

> “I may be new to coding, but I’m not new to hard work and problem-solving.”  
>  
> — *Praise Ndumiso*

---

## 👨‍💻 Author  

**Praise Ndumiso**  
📍 Ratanda, Heidelberg, South Africa  
💼 Aspiring Software Engineer  
💡 Passionate about technology, problem-solving, and continuous learning  

## ⚙️ Setup & Installation  

Follow these steps to set up and run **Ball IQuiz** locally:

### 1️⃣ Clone the Repository  
```bash
git clone [https://github.com/Prvise/balliquiz.git]
cd balliquiz
2️⃣ Create a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
3️⃣ Install Dependencies
Make sure your requirements.txt file is in the root directory, then run:

bash
Copy code
pip install -r requirements.txt
4️⃣ Set Up the Database
unzip statistics.db && unzip accounts.db
Create the accounts.db and statistics.db file and initialize the required tables if not already present:

bash
Copy code
python
>>> from cs50 import SQL
>>> db = SQL("sqlite:///accounts.db")
>>> # Example: db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, hash TEXT, score INTEGER)")
>>> exit()
5️⃣ Run the Application
bash
Copy code
flask run
6️⃣ Access the App
Open your browser and visit:
👉 http://127.0.0.1:5000
