import ollama
import json
import re

def generate_questions(resume_text):

    prompt = f"""
You are an interview question generator.

Generate EXACTLY 5 short questions based on the resume.

Return STRICT JSON ARRAY ONLY:

["Question 1", "Question 2", "Question 3", "Question 4", "Question 5"]

NO explanation. NO markdown.

Resume:
{resume_text}
"""

    response = ollama.chat(
        model='llama3.2',
        messages=[{'role': 'user', 'content': prompt}]
    )

    content = response['message']['content']

    # remove junk formatting
    content = content.replace("```json", "").replace("```", "").strip()

    try:
        questions = json.loads(content)

        if isinstance(questions, list) and len(questions) > 0:
            return [str(q).strip() for q in questions]

    except:
        pass

    # fallback: extract lines properly
    lines = re.findall(r'(Q?\d*\.?\s*.+)', content)

    return [l.strip() for l in lines if l.strip()][:5]