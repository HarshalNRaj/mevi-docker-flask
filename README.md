# Mevi Docker Flask

A simple web application built using Python and Flask, demonstrating five different routes.

## Features

- Home page
- About page
- Contact page
- Services page
- Profile page

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Docker

## Project Structure

```text
mevi-docker-flask/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── services.html
│   └── profile.html
└── static/
    └── style.css
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd mevi-docker-flask
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000

## Available Routes

| Route | Description |
|---|---|
| `/` | Home page |
| `/about` | About page |
| `/contact` | Contact page |
| `/services` | Services page |
| `/profile` | Profile page |

## Docker

Docker configuration can be used to build and run the application in a container.

## Author

Harshal N Raj