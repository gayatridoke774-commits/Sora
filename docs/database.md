# Sora Database Design

## Overview

The Sora database is designed to support personalized, adaptive learning. It stores user progress, study history, subject-wise performance, mistakes, and learning schedules so that Sora can act as a continuous study companion.

The system is structured so that users can resume learning exactly where they left off and track progress separately for each subject.

---

# 1. Users

Stores basic user information.

**Fields:**

* user_id (Primary Key)
* name
* email
* password_hash
* created_at

---

# 2. Subjects

Each user can have multiple subjects.

**Fields:**

* subject_id (Primary Key)
* user_id (Foreign Key)
* subject_name
* created_at

---

# 3. Topics

Each subject contains multiple topics.

**Fields:**

* topic_id (Primary Key)
* subject_id (Foreign Key)
* topic_name
* status (Not Started / In Progress / Completed)
* difficulty_level

---

# 4. Study Sessions (Core Memory)

This is where Sora remembers what you last did.

**Fields:**

* session_id (Primary Key)
* user_id (Foreign Key)
* subject_id (Foreign Key)
* topic_id (Foreign Key)
* start_time
* end_time
* last_active_point (important for resume feature)
* session_notes
* confidence_level

---

# 5. Learning Progress (Subject-wise Tracking)

Tracks progress separately for each subject.

**Fields:**

* progress_id (Primary Key)
* user_id (Foreign Key)
* subject_id (Foreign Key)
* topics_completed
* topics_remaining
* accuracy_score
* weak_topics

---

# 6. Flashcards

Stores AI-generated revision cards.

**Fields:**

* flashcard_id (Primary Key)
* topic_id (Foreign Key)
* question
* answer
* difficulty
* last_reviewed
* next_review_date

---

# 7. Quiz History

Stores all recall tests.

**Fields:**

* quiz_id (Primary Key)
* topic_id (Foreign Key)
* score
* correct_answers
* wrong_answers
* questions_data
* created_at

---

# 8. Mistake Tracker

Sora remembers what you get wrong.

**Fields:**

* mistake_id (Primary Key)
* user_id (Foreign Key)
* topic_id (Foreign Key)
* mistake_description
* count
* last_seen
* is_mastered

---

# 9. Spaced Repetition Scheduler

Controls revision timing.

**Fields:**

* schedule_id (Primary Key)
* topic_id (Foreign Key)
* next_review_date
* interval_days
* repetition_count

---

# 10. Task / Project Submissions

Mandatory application layer.

**Fields:**

* task_id (Primary Key)
* topic_id (Foreign Key)
* title
* description
* submission_link
* status (Pending / Submitted / Reviewed)
* ai_feedback

---

# 11. Conversation Memory (Sora Personality)

This enables Sora to communicate like a study friend.

**Fields:**

* message_id (Primary Key)
* user_id (Foreign Key)
* sender (User / Sora)
* message_text
* timestamp
* context_type (Study / Reminder / Quiz / Motivation)

---

# Key Design Principles

* Each subject is tracked independently
* Every study session can be resumed
* Mistakes are remembered and revisited
* Learning is adaptive based on performance
* Communication history enables conversational AI behavior
* Data is structured for personalization and long-term learning

---

# Vision

This database is designed not just to store information, but to simulate a learning companion that remembers, adapts, and communicates like a real study partner.

