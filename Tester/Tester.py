import json
from flask import Flask, render_template, url_for, request
app = Flask(__name__,)

def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return 1
    return 0

@app.route("/")
def index():
    questions = json.load(open('questions.json', 'r', encoding='utf-8-sig'))
    return render_template("index.html", questions=questions)

@app.route("/check", methods=['POST'])
def check():
    points = 0

    if request.form != None:
        questions = json.load(open('questions.json', 'r', encoding='utf-8-sig'))

        for index, q in enumerate(questions):
            answer = request.form.get('question' + str(index+1))
            if answer != None:
                points = points + check_answer(int(answer), q.get('correct_answer'))
    
    return render_template("check.html", result=points)
   
if __name__ == "__main__":
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=3333)