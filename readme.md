# 🎬 Movie Recommender System

A simple web app that recommends movies based on your favorite movie.
Built using **Flask, Machine Learning, and TMDB API**.

---

## 🚀 Features

* 🎥 Get 4–5 similar movie recommendations
* 🖼️ Movie posters using TMDB API
* ⚡ Fast recommendations using similarity matrix
* 🎨 Clean dark UI

---

## 🛠️ Tech Stack

* Python (Flask)
* Pandas / Pickle (ML model)
* HTML, CSS
* TMDB API (for posters)

---

## 📂 Project Structure

```
project/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Add API Key

Create a `.env` file and add:

```
TMDB_API_KEY=your_api_key_here
```

---

### 4. Run the app

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment (Render)

* Push code to GitHub
* Connect repo to Render
* Add environment variable: `TMDB_API_KEY`
* Start command:

```
gunicorn app:app
```

---

## ⚠️ Notes

* Do not upload `.env` file to GitHub
* Free hosting may be slow on first load

---

## 🙌 Author

Made by **Kartikey Gehra**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
