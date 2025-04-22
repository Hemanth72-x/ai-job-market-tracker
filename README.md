# 🧠 AI Job Market Tracker 🗺️  
### Track, analyze, and visualize AI jobs — all from your browser. Built with 🔥 Streamlit, 📊 Pandas, ☁️ Docker.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?style=flat&logo=streamlit)
![Dockerized](https://img.shields.io/badge/Containerized-Docker-blue?style=flat&logo=docker)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python)

---

## 🚀 What Is This?

This project helps you explore the **AI job market** with:

- 🎯 Filters by Job Title, Company, and Location  
- 🔍 Search functionality over job descriptions  
- ☁️ Word Cloud generation  
- 🗺️ Simulated city-level map visualization  
- 📦 Packaged and portable with Docker

All powered by **Python + Streamlit** and built from scratch.

---

## 📸 Demo

![image](https://github.com/user-attachments/assets/08c48d53-77d3-4e35-8b9d-f49ee90ead3c)




---

## 🛠 Features

- ✅ Dropdown filters (Title, Company, Location)
- ✅ Keyword search inside job summaries
- ✅ Auto-generated Word Cloud
- ✅ Map view with simulated coordinates
- ✅ Fully Dockerized with a simple `docker run`
- ✅ Clean UI with Streamlit’s wide layout

---

## 🧰 Tech Stack

| Layer         | Tools                       |
|---------------|-----------------------------|
| Language      | Python 3.9+                 |
| Dashboard     | Streamlit                   |
| Data          | Pandas, CSV                 |
| Visuals       | Matplotlib, WordCloud       |
| Container     | Docker                      |

---

## 💻 Run Locally

### 1️⃣ Clone the repo

```bash
git clone https://github.com/Hemanth72-x/ai-job-market-tracker.git
cd ai-job-market-tracker

Step 2:
python3 -m venv venv
source venv/bin/activate

Step 3:
pip install -r requirements.txt

Step 4:
streamlit run app/dashboard.py

Run with Docker:
docker build -t ai-job-tracker .
docker run -p 8501:8501 ai-job-tracker

