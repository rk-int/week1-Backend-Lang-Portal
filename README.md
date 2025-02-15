# week1-Backend-Lang-Portal
Gen AI bootcamp Week 1 Back end lang portal

# Lang Portal Backend

## 📌 Overview
The **Lang Portal Backend** is a FastAPI-based backend system for a language learning school. It acts as:
- An inventory of vocabulary words
- A Learning Record Store (LRS) to track study sessions and word reviews
- A launchpad for learning applications

## 🚀 Tech Stack
- **Framework:** FastAPI
- **Database:** SQLite3
- **ORM:** SQLAlchemy
- **Python Version:** 3.x

## 📂 Project Structure
```
lang-portal-backend/
│── app/
│   ├── database.py  # Database connection
│   ├── models.py    # SQLAlchemy models
│   ├── routes/      # API route handlers
│   ├── schemas.py   # Pydantic models
│   ├── main.py      # Entry point
│── .gitignore
│── requirements.txt
│── README.md
```

## 🔧 Installation

### 1️⃣ Clone the repository
```sh
git clone https://github.com/YOUR_USERNAME/lang-portal-backend.git
cd lang-portal-backend
```

### 2️⃣ Create and activate a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI app
```sh
uvicorn app.main:app --reload
```

## 📖 API Endpoints

### 🌐 Words
- `GET /words` - Get a paginated list of words

### 🌍 Groups
- `GET /groups` - Get a paginated list of word groups
- `GET /groups/{id}` - Get words from a specific group

### 📚 Study Sessions
- `POST /study_sessions` - Create a new study session
- `POST /study_sessions/{id}/review` - Log a word review

## 🛠 Deployment
- Can be deployed on **Render, Railway, or DigitalOcean**.
- Use **Docker** for containerized deployment.

## 🤝 Contribution
1. Fork the repo
2. Create a new branch (`feature-xyz`)
3. Commit and push
4. Submit a pull request

## 📜 License
MIT License. See `LICENSE` for details.

---

