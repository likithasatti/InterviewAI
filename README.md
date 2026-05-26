**AI Interview Assistant**
**Project Overview**

AI Interview Assistant is an AI-powered web application developed to help students and job seekers prepare for interviews in a smarter and more personalized way. The main objective of this project is to generate interview questions automatically based on the user’s uploaded resume. Instead of practicing common interview questions, users can receive questions related to their own skills, projects, education, and technical knowledge mentioned in the resume.

This project is designed using a full-stack architecture with a FastAPI backend and a Streamlit frontend. The backend handles resume processing, text extraction, and AI-based question generation, while the frontend provides a simple and interactive user interface for users to upload resumes and view generated questions.
 
The application uses Large Language Models (LLMs) through Ollama, such as Llama 3 and TinyLlama, to generate intelligent interview questions dynamically. This makes the system more interactive and realistic compared to traditional interview preparation platforms. The generated questions help users practice technical, project-based, and HR interview scenarios.

The project also includes additional features like a login and registration system, dashboard interface, and dark mode support to improve user experience and usability. The dashboard helps users organize and access the generated interview content easily.

**Key Features**
Resume Upload in PDF format
AI-generated interview questions
Personalized question generation
Login and Registration system
Dashboard interface
Dark mode support
FastAPI backend integration
Streamlit frontend interface

**Technologies Used**
Python
FastAPI
Streamlit
Ollama
Llama 3 / TinyLlama
Git & GitHub
Learning Outcomes

**This project helped in understanding**
Full-stack web application development
Frontend and backend integration
API development using FastAPI
AI model integration with applications
Resume parsing and text extraction
GitHub version control
User interface development using Streamlit

**How to Run the Project**
Step 1 — Open Project Folder
Open terminal inside the project folder:
InterviewAI
Step 2 — Activate Virtual Environment
venv\Scripts\activate
Step 3 — Run Backend
uvicorn main:app --reload
Backend runs on:
http://127.0.0.1:8000
Swagger API Docs:
http://127.0.0.1:8000/docs
Step 4 — Open New Terminal
Move to frontend folder:
cd frontend
Run Streamlit app:
streamlit run app.py
Step 5 — Use the Application
Upload resume in PDF format
AI generates interview questions
Practice interview preparation interactively

**Workflow of the project**
Resume Upload
↓
Extract Resume Text 
↓
AI Generates Questions
↓
User Answers
↓
AI Evaluates Answers
↓
Feedback + Score
