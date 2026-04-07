# HealthMate AI

> Your Personal AI-Powered Health Companion

HealthMate AI is a smart, interactive health assistant that helps users monitor their health, receive personalized recommendations, and interact with an AI chatbot for real-time guidance.

# Overview

HealthMate AI combines data analysis, machine learning, and AI-powered conversations to provide a complete health tracking and advisory platform.

Whether you're tracking your fitness goals, analyzing your BMI, or asking health-related questions, HealthMate AI delivers intelligent and user-friendly solutions.

# Features

## AI Chatbot (Groq Powered)

* Real-time health conversations
* Powered by LLaMA 3.1 via Groq API
* Provides safe and general health advice

###  Health Analysis

* BMI calculation
* Health score evaluation
* Personalized recommendations

###  Disease Prediction

* Predicts possible diseases based on symptoms
* Simple ML-based classification

###  Diet Recommendation

* Goal-based diet plans
* Supports weight loss, gain, and maintenance

###  Workout Planner

* Personalized workout suggestions
* Based on user goals

###  Health History

* Stores past health records
* Track progress over time

###  Dashboard

* Visualize health metrics
* Interactive charts and trends

---

## Tech Stack

| Category      | Technology           |
| ------------- | -------------------- |
| Frontend      | Streamlit            |
| Backend       | Python               |
| AI            | Groq API (LLaMA 3.1) |
| Database      | SQLite               |
| Data Handling | Pandas               |
| Visualization | Plotly               |


##  Project Structure

HealthMate/
│
├── Pages/
│   ├── chatbot.py
│   ├── health_analysis.py
│   ├── dashboard.py
│   ├── history.py
│   ├── profile.py
│   └── reminders.py
│
├── app.py
├── database.py
├── diet_recommender.py
├── model.py
├── risk_predictor.py
├── workout_planner.py
├── style.css
├── users.db
├── .env (excluded)
└── README.md
```


## Getting Started

### Clone the Repository

```
git clone https://github.com/priyamaan924/HealthMate.git
cd HealthMate
```

---

###  Install Dependencies

```
pip install -r requirements.txt
```

---

###  Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

###  Run the App

```
streamlit run app.py
```

---

## Screenshots

> *(Add screenshots here later for better presentation)*

Example:

```
/screenshots/dashboard.png
/screenshots/chatbot.png
```

---

##  Deployment

You can deploy this app using:

* Streamlit Community Cloud
* Render

---

##  Future Improvements

* Smart reminders & notifications
* PDF health report generation
* Personalized AI using user data
* Mobile-friendly UI
* Live deployment

---

## Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## License

This project is open-source and available under the MIT License.

---

##  Author

**Priya**
🔗 GitHub: https://github.com/priyamaan924

---

# Support

If you like this project, please consider giving it a ⭐ on GitHub!
