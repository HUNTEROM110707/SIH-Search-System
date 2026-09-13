# 🔐 CaseVault — Secure Legal Document Search System

> **Smart India Hackathon 2026 — SIH26190**

A secure backend system for searching and managing metadata of legal, investigation, and case-related documents using **FastAPI, PostgreSQL, and REST APIs**.

---

## 🚀 Project Overview

CaseVault is designed to help authorized police, investigation, and judicial users quickly search case documents using structured metadata such as:

* FIR Number
* Case Number
* Officer Name
* Document Type
* Legal Section
* Document Date

The backend provides a fast and structured REST API connected to a PostgreSQL database.

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │   CaseVault Frontend │
                    │      (Vercel)        │
                    └──────────┬───────────┘
                               │
                               │ REST API
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    │       (Render)       │
                    └──────────┬───────────┘
                               │
                               │ SQLAlchemy
                               ▼
                    ┌──────────────────────┐
                    │ PostgreSQL Database  │
                    │        (Neon)        │
                    └──────────────────────┘
```

---

## ✨ Features

* 🔎 Metadata-based document search
* 📄 FIR and case number search
* 👮 Officer-based search
* 📑 Document type filtering
* ⚖️ Legal section filtering
* 📅 Document date filtering
* 🗄️ PostgreSQL database integration
* ⚡ FastAPI REST API
* 🌐 CORS support for frontend integration
* ☁️ Cloud deployment using Render
* 🔐 Environment-variable based database configuration

---

## 🛠️ Tech Stack

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Backend programming        |
| FastAPI    | REST API framework         |
| SQLAlchemy | Database connectivity      |
| PostgreSQL | Document metadata database |
| Neon       | Cloud PostgreSQL hosting   |
| Render     | Backend deployment         |
| GitHub     | Version control            |
| Vercel     | Frontend deployment        |

---

## 📂 Project Structure

```text
SIH-Search-System/
│
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignored files and secrets
└── README.md            # Project documentation
```

---

## 🔌 API

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "SIH Document Search API is working!"
}
```

### Search Documents

```http
GET /documents/search
```

### Available Search Parameters

| Parameter       | Description             | Example        |
| --------------- | ----------------------- | -------------- |
| `fir_number`    | Search by FIR number    | `FIR001`       |
| `case_number`   | Search by case number   | `CASE101`      |
| `officer_name`  | Search by officer       | `Rahul Sharma` |
| `document_type` | Search by document type | `FIR`          |
| `section`       | Search by legal section | `IPC 302`      |
| `document_date` | Search by document date | `2026-01-10`   |

### Example

```http
GET /documents/search?fir_number=FIR001
```

Example response:

```json
{
  "results": [
    {
      "id": 1,
      "fir_number": "FIR001",
      "case_number": "CASE101",
      "officer_name": "Rahul Sharma",
      "document_type": "FIR",
      "document_date": "2026-01-10",
      "section": "IPC 302",
      "file_path": "/docs/fir001.pdf"
    }
  ]
}
```

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/HUNTEROM110707/SIH-Search-System.git
cd SIH-Search-System
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=YOUR_POSTGRESQL_CONNECTION_STRING
```

> Never commit `.env` or database credentials to GitHub.

### 5. Start the API

```powershell
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## ☁️ Deployment

The backend is deployed using:

**GitHub → Render → Neon PostgreSQL**

Live API:

```text
https://sih-search-api.onrender.com
```

API documentation:

```text
https://sih-search-api.onrender.com/docs
```

---

## 🔒 Security

The project follows basic secure-development practices:

* Database credentials are stored using environment variables.
* `.env` is excluded through `.gitignore`.
* Parameterized SQL queries are used.
* Database access is handled through SQLAlchemy.
* CORS is configured for frontend communication.

> This project is a hackathon prototype and should undergo additional security hardening before production use with real legal or investigative data.

---

## 👨‍💻 Team Role

### Member 4 — Search & Metadata

Responsibilities:

* PostgreSQL database design
* Document metadata schema
* Search API development
* Search filters
* FastAPI backend
* Neon database integration
* Render deployment
* Frontend API integration support

---

## 🎯 SIH Problem Statement

**SIH26190 — Secure Digital Legal / Investigation Document Management**

The system aims to provide secure, structured, and efficient access to legal and investigation-related documents while maintaining appropriate access controls and auditability.

---

## 📌 Project Status

| Component                     | Status         |
| ----------------------------- | -------------- |
| FastAPI Backend               | ✅ Complete     |
| PostgreSQL Database           | ✅ Complete     |
| Search API                    | ✅ Complete     |
| Search Filters                | ✅ Complete     |
| Neon Deployment               | ✅ Complete     |
| Render Deployment             | ✅ Complete     |
| Frontend Integration          | 🔄 In Progress |
| Production Security Hardening | 🔄 Planned     |

---

## 📜 License

This project was developed as part of **Smart India Hackathon 2026**.
