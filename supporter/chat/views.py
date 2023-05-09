from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai
import json
import os
import dotenv
from pathlib import Path

env_path = Path.cwd()
dotenv.load_dotenv(f"{env_path}/.env.bat")
openai.api_key = os.environ.get("OPENAI_KEY")

url = "https://api.openai.com/v1/engines/{ENGINE_ID}/documents"

file_path = os.path.join(os.getcwd(), 'chat/data/FAQ.json')
with open(file_path, encoding="utf8") as f:
    data = json.load(f)

question_answer_pairs = []
for entry in data:
    question = entry["Question_original"]
    answer = entry["Answer_plain_text"]
    question_answer_pairs.append((question, answer))

@csrf_exempt
def home(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = generate_answer(question)
        return render(request, 'chat/home.html', {'question': question, 'answer': answer})

    return render(request, 'chat/home.html')

def generate_answer(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Question: {question}\nAnswer:",
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    answer = response.choices[0].text.strip()
    return answer
