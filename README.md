# 🌿 Leaf Disease Detection System

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg?style=flat&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-AI%20Inference-orange.svg?style=flat)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat)](LICENSE)

An AI-powered **Plant Leaf Disease Detection System** built using **FastAPI** and **Streamlit**.

This application allows users to upload a plant leaf image and get:
- Disease name
- Disease category
- Confidence score
- Symptoms
- Possible causes
- Treatment recommendations

---

## 🚀 Live Demo

**Live Link**
https://sameersingh18.github.io/Plant-Leaf-Disease-Detection/

**FastAPI Backend**  
https://leaf-diseases-detect.vercel.app/

---

## 🧠 How It Works

1. User uploads a plant leaf image  
2. Image is sent to FastAPI backend  
3. AI model (Groq API) analyzes the image  
4. Disease detection result is generated  
5. Streamlit displays results in a premium dark UI  

---

## ✨ Features

- 🌱 AI-based plant leaf disease detection  
- 📷 Image upload with preview  
- 🦠 Disease name & type  
- 📊 Confidence percentage  
- 📋 Symptoms & causes  
- 💊 Treatment recommendations  
- 🌑 Premium dark UI  
- ☁️ Cloud deployed  

---

## 🏗️ Project Structure

```
plants-leaf-disease/
│
├── main.py # Streamlit frontend
├── app.py # FastAPI backend
├── utils.py # Image utilities
├── Leaf Disease/
│ └── main.py # AI detection logic
├── test_api.py # API testing
├── requirements.txt
├── .env.example
├── Media/
└── README.md
```
---
## 🛠️ Tech Stack

**Frontend**
- Streamlit
- Custom CSS (Dark Theme)

**Backend**
- FastAPI
- Groq API
- Python

**Deployment**
- Streamlit Cloud
- Vercel

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here 
```
---

## ▶️ Run Locally

1️⃣ Clone the Repository
```
git clone https://github.com/Divy-Gupta/plants-leaf-disease.git
cd plants-leaf-disease
```

2️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Run FastAPI Backend
```
uvicorn app:app --reload
```

API Docs:
```
http://localhost:8000/docs
```

5️⃣ Run Streamlit Frontend
```
streamlit run main.py
```

App runs at:
```
http://localhost:8501
```
---
## 🔐 Notes

 - Groq API credits are used only when detection is triggered

 - Streamlit deployment itself does not consume API credits

 - .env file should never be pushed to GitHub

---
## 👨‍💻 Author

 - Sameer Singh
 - B.Tech (AI & ML)
 - GitHub: https://github.com/SameerSingh18
---
## 📜 License

- This project is licensed under the MIT License.

---
<div align="center">
⭐ Star this repository if you found it useful!
</div>

