#  HealthMate AI

> AI-powered health assistant for analysis, prediction, and smart recommendations

---

##  Overview

HealthMate AI is a Streamlit-based web application that helps users monitor their health, analyze key metrics like BMI, predict possible diseases, and receive personalized diet and workout recommendations.

It also includes an AI chatbot powered by Groq for real-time health guidance.

---

##  Features

###  Health Analysis

* BMI calculation
* Health score evaluation
* Calorie recommendations

###  Disease Prediction

* Predict diseases based on symptoms
* Uses dataset (`disease_data.csv`)

###  Diet Recommendation

* Goal-based diet suggestions
* Supports weight loss, gain, and maintenance

###  Workout Planner

* Personalized workout suggestions
* Based on user health goals

###  Health History Tracking

* Stores user data in SQLite database
* View previous health records

###  AI Health Chatbot

* Powered by Groq API
* Provides real-time health advice

---

##  Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI:** Groq API (LLaMA 3.1)
* **Database:** SQLite
* **Data Processing:** Pandas
* **Visualization:** Plotly

---

##  Project Structure

```
HealthMate/
│
├── Pages/
│   ├── chatbot.py
│   ├── dashboard.py
│   ├── health_analysis.py
│   ├── history.py
│   ├── profile.py
│   └── reminders.py
│
├── app.py
├── database.py
├── diet_recommender.py
├── disease_data.csv
├── model.py
├── risk_predictor.py
├── workout_planner.py
├── style.css
├── users.db
├── .env (not included)
└── README.md
```

---

##  Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/priyamaan924/HealthMate.git
cd HealthMate
```

---

### 2️⃣ Install Dependencies

```
pip install streamlit groq python-dotenv pandas plotly
```

---

### 3️⃣ Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 4️⃣ Run Application

```
streamlit run app.py
```

---

##  Future Improvements

* Personalized AI responses using user health data
* PDF health report generation
* Smart notifications and reminders
* UI/UX improvements
* Deployment for public access

---

##  Author

**Priya**
GitHub: https://github.com/priyamaan924

---

## Support

If you like this project, give it a ⭐ on GitHub!
