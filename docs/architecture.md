# Sora Architecture

## Overview

Sora follows a modular architecture where each component has a specific responsibility. This makes the application easier to develop, maintain, and scale.

---

# High-Level Architecture

```
User
   │
   ▼
Frontend (React)
   │
   ▼
Backend API (FastAPI)
   │
   ├──────────────┐
   │              │
   ▼              ▼
AI Engine      Database
   │              │
   └──────────────┘
          │
          ▼
     Response to User
```

---

# Components

## 1. Frontend

Responsible for:

* User interface
* Dashboard
* Study sessions
* Flashcards
* Quizzes
* Progress tracking
* Settings

The frontend sends user requests to the backend and displays the results.

---

## 2. Backend

Acts as the brain of the application.

Responsibilities:

* Manage users
* Handle study sessions
* Process API requests
* Store and retrieve data
* Communicate with the AI Engine
* Manage review schedules

---

## 3. AI Engine

The intelligence behind Sora.

Responsibilities:

* Generate Active Recall questions
* Create flashcards
* Summarize notes
* Identify important concepts (80/20)
* Generate quizzes
* Create coding exercises
* Analyze weak topics
* Recommend future study sessions

---

## 4. Database

Stores all application data.

Examples:

* User profiles
* Subjects
* Topics
* Notes
* Flashcards
* Quiz history
* Mistake history
* Review schedule
* Progress data

---

# Study Session Flow

1. Student selects a subject and topic.
2. Student completes a study session.
3. Sora asks the student to explain what they learned.
4. The AI Engine analyzes the notes.
5. Flashcards are generated.
6. Recall questions are created.
7. A practical task is assigned.
8. A review schedule is created.
9. Mistakes are stored for future revision.
10. Progress is updated on the dashboard.

---

# Design Principles

* Modular architecture
* Scalable design
* AI-first learning experience
* Personalized education
* Easy to extend with future features

---

# Future Expansion

The architecture is designed to support future additions such as:

* Voice conversations
* Mobile applications
* AI mentor personalities
* Team study sessions
* Cloud synchronization
* Advanced analytics

```
```

