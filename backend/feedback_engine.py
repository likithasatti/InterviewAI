import ollama

def evaluate_answer(question, answer):

    prompt = f"""
You are an AI interview evaluator.

Question: {question}
Answer: {answer}

Return ONLY JSON:

{{
  "score": 0-10,
  "feedback": "short improvement tips"
}}
"""

    response = ollama.chat(
        model='llama3.2',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['message']['content']