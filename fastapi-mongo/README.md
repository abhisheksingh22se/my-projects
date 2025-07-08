# 🏥 FastAPI MongoDB - Hospital Patient API

This is a backend API service for storing and retrieving hospital patient information using **FastAPI** and **MongoDB**. It is containerized with **Docker**, supports environment-based configuration, and is CI/CD-ready for deployment in cloud platforms like AWS.

---

## 🚀 Features

- Create and retrieve patient records
- Built with FastAPI for high-performance REST APIs
- MongoDB for document-based data storage
- Uses Pydantic v2 for data validation
- Environment variable support using `.env`
- Fully containerized using Docker
- Ready for DevOps workflows and CI/CD

---

## 📁 Project Structure
```none
fastapi-mongo/
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI app routes
│ ├── models.py # Pydantic models
│ ├── database.py # MongoDB connection
│
├── .env # MongoDB connection string
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🛠️ Setup Instructions

### 🔧 Local Setup (With Virtual Environment)

```bash
git clone git@github.com:abhisheksingh22se/my-project.git
cd my-project/fastapi-mongo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload 
```
Visit: http://127.0.0.1:8000


## 🧪 API Endpoints

| Method | Endpoint       | Description                 |
|--------|----------------|-----------------------------|
| GET    | `/`            | Welcome message             |
| POST   | `/patients`    | Create new patient entry    |
| GET    | `/patients`    | Get all patient entries     |

Use Swagger UI to interact with the API:  
👉 [`http://localhost:8000/docs`](http://localhost:8000/docs)

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:
MONGO_URL=mongodb://admin:password@localhost:27017

Update this to match your MongoDB connection string — whether it's local, in Docker, or hosted.

---

## 🐳 Docker Usage

### Build and Run

```bash
docker build -t fastapi-mongo .
docker run -d -p 8000:8000 --env-file .env fastapi-mongo
```

## 📦 Requirements
Install all dependencies:

bash
Copy
Edit
pip install -r requirements.txt

## 🧰 Tech Stack

FastAPI – API framework
MongoDB – NoSQL database
Uvicorn – ASGI server
Pydantic v2 – Data validation
Docker – Containerization
python-dotenv – Environment variable management