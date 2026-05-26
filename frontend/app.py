import streamlit as st
import requests

st.set_page_config(page_title="AI Interview Assistant", page_icon="🤖")

# ---------------- HEADER ----------------
st.title("🤖 AI Interview Assistant")
st.caption("Resume → AI Questions → Interview → Evaluation → Feedback")


# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"

if "users" not in st.session_state:
    st.session_state.users = {"admin": "1234"}

if "questions" not in st.session_state:
    st.session_state.questions = []

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "results" not in st.session_state:
    st.session_state.results = []


# ---------------- LOGIN ----------------
def login_page():
    st.title("🔐 Login")

    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        if u in st.session_state.users and st.session_state.users[u] == p:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid login")

    if st.button("Go to Register"):
        st.session_state.page = "register"
        st.rerun()


# ---------------- REGISTER ----------------
def register_page():
    st.title("📝 Register")

    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Register"):
        if new_user in st.session_state.users:
            st.warning("User already exists")
        else:
            st.session_state.users[new_user] = new_pass
            st.success("Registration successful! Go to login.")

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()


# ---------------- DASHBOARD ----------------
def dashboard():

    menu = st.sidebar.radio(
        "Menu",
        ["Upload Resume", "Interview", "Results", "Logout"]
    )

    # ---------------- UPLOAD ----------------
    if menu == "Upload Resume":

        st.title("📄 Upload Resume")

        file = st.file_uploader("Upload PDF", type=["pdf"])

        if file:

            try:
                res = requests.post(
                    "http://127.0.0.1:8000/upload-resume/",
                    files={"file": file}
                )

                data = res.json()

                if "questions" in data and data["questions"]:

                    st.session_state.questions = data["questions"]
                    st.session_state.answers = {}
                    st.session_state.results = []

                    st.success("Questions generated successfully!")

                else:
                    st.error(data.get("error", "Failed to generate questions"))

            except Exception as e:
                st.error(f"Backend error: {e}")


    # ---------------- INTERVIEW ----------------
    elif menu == "Interview":

        st.title("🧠 Interview Mode")

        if not st.session_state.questions:
            st.warning("Please upload resume first")
            return

        st.session_state.answers = {}

        for i, q in enumerate(st.session_state.questions):

            st.markdown(f"### Q{i+1}: {q}")

            ans = st.text_area("Your Answer", key=f"ans_{i}")

            st.session_state.answers[q] = ans

        if st.button("Submit Answers"):

            results = []

            for q, a in st.session_state.answers.items():

                if not a.strip():
                    continue

                try:
                    res = requests.post(
                        "http://127.0.0.1:8000/evaluate-answer/",
                        json={"question": q, "answer": a}
                    )

                    results.append(res.json())

                except Exception as e:
                    results.append({"score": 0, "feedback": str(e)})

            st.session_state.results = results
            st.success("Evaluation completed!")


    # ---------------- RESULTS ----------------
    elif menu == "Results":

        st.title("📊 Results")

        if not st.session_state.results:
            st.warning("No results yet")
            return

        for i, r in enumerate(st.session_state.results):

            st.markdown("---")
            st.markdown(f"### Q{i+1}")
            st.markdown(f"**Score:** {r.get('score', 'N/A')}")
            st.markdown(f"**Feedback:** {r.get('feedback', 'No feedback')}")


    # ---------------- LOGOUT ----------------
    elif menu == "Logout":

        st.session_state.logged_in = False
        st.session_state.questions = []
        st.session_state.answers = {}
        st.session_state.results = []
        st.session_state.page = "login"
        st.rerun()


# ---------------- APP FLOW ----------------
if st.session_state.logged_in:
    dashboard()
else:
    if st.session_state.page == "login":
        login_page()
    else:
        register_page()