# 🖍️ Real-Time Collaborative Whiteboard

A real-time multi-user whiteboard web application built with Django Channels and WebSockets. Users can draw together on a shared canvas, save snapshots, and see updates live across connected clients.



## 🚀 Features

- 🎨 Real-time collaborative drawing
- 📌 Snapshot saving and loading (per room)
- 🧽 Clear canvas for all users
- ↩️ Undo / Redo functionality
- ✏️ Multiple drawing tools (colors, pen size, eraser)
- 🕓 Snapshot history & versioning
- 🖱️ Show user cursors in real-time
- 📐 Responsive canvas with window resize handling
- ⏳ Loading indicators for save/load actions

---

## 🛠 Tech Stack

- **Frontend:** JavaScript, HTML5 Canvas, WebSocket API
- **Backend:** Python, Django, Django Channels
- **Real-Time Layer:** Redis (as channel layer)
- **ASGI Server:** Daphne
- **Hosting:** Render
- **Others:** Whitenoise, REST API (for snapshots), CSRF protection

---

## 📦 Installation (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/Sudhir4500/Whiteboard.git
cd Whiteboard

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows



pip install -r requirements.txt



4. Start Redis Server (locally)
Make sure Redis is installed and running. You can use Docker:

docker run -p 6379:6379 redis
Or install it directly from https://redis.io/



python manage.py migrate
python manage.py runserver

