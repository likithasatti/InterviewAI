AI Interview Assistant Project Overview
1. Introduction

AI Interview Assistant is an AI-powered web application designed to help students and job seekers prepare for interviews in a smarter and more personalized way.

The system automatically generates interview questions based on the user’s uploaded resume. Instead of practicing common questions, users receive personalized technical, project-based, and HR questions related to their own resume content.

2. Project Objective

The main objective of this project is to:

Automate interview preparation
Generate AI-based interview questions
Evaluate user answers
Provide feedback and scoring
Improve interview confidence and communication skills
3. System Architecture
Frontend
Built using Streamlit
Provides user interface for:
Login/Register
Resume Upload
Interview Session
Results Dashboard
Backend
Built using FastAPI
Handles:
Resume processing
API endpoints
AI integration
Answer evaluation
AI Model
Uses Ollama
Models used:
Llama 3
TinyLlama
4. Key Features
Resume Upload
Upload resume in PDF format
Extracts resume text automatically
AI Question Generation
Generates personalized interview questions
Includes technical and HR questions
Interview Mode
Users answer AI-generated questions
Interactive interview experience
AI Evaluation
AI evaluates user answers
Generates score and feedback
Dashboard Interface
Clean and user-friendly interface
Displays interview results
Login & Registration
User authentication system
Secure access to application
5. Technologies Used
Technology	Purpose
Python	Core programming language
FastAPI	Backend framework
Streamlit	Frontend framework
Ollama	AI model integration
Llama 3	Question generation
Git & GitHub	Version control
6. Workflow of the Project
Resume Upload
      ↓
Extract Resume Text
      ↓
AI Generates Questions
      ↓
User Answers Questions
      ↓
AI Evaluates Answers
      ↓
Feedback + Score
7. Learning Outcomes

This project helped in understanding:

Full-stack web development
Frontend and backend integration
REST API development
AI model integration
Resume parsing techniques
Streamlit UI development
FastAPI backend development
GitHub version control
8. How to Run the Project
Step 1 — Open Project Folder
InterviewAI
Step 2 — Activate Virtual Environment
venv\Scripts\activate
Step 3 — Run Backend Server
uvicorn main:app --reload

Backend URL:

http://127.0.0.1:8000

Swagger API Documentation:

http://127.0.0.1:8000/docs
Step 4 — Run Frontend

Open a new terminal:

cd frontend

Run Streamlit application:

streamlit run app.py
Step 5 — Use the Application
Login/Register
Upload Resume
Generate Questions
Answer Questions
View Feedback & Score
9. Future Enhancements
Database integration using MySQL
Voice-based interview system
AI speech analysis
Interview performance analytics
Cloud deployment
Multi-user support
