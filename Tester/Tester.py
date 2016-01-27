import json
from flask import Flask, render_template, url_for, request
app = Flask(__name__,)


@app.route("/")
def index():
    questions = json.load(open('questions.json', 'r', encoding='utf-8-sig'))
    return render_template("index.html", questions=questions)
        
def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return 1
    return 0


@app.route("/check", methods=['POST'])
def check():
    points = 0

    if request.form != None:
        question1 = request.form.get('question1')
        points = points + check_answer(question1, '1')
        
        question2 = request.form.get('question2')
        points = points + check_answer(question2, '1')

        question3 = request.form.get('question3')
        points = points + check_answer(question3, '1')
        
        question4 = request.form.get('question4')
        points = points + check_answer(question4, '1')

        question5 = request.form.get('question5')
        points = points + check_answer(question5, '2')
    
    return render_template("check.html", result=points)
   
if __name__ == "__main__":
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=3333)