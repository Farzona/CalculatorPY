from flask import Flask, render_template, url_for, request
app = Flask(__name__,)
  
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=['POST'])
def check():
    points = 0

    if request.form != None:
        question1 = request.form.get('question1')
        if question1 == '1':
            points = points + 1
        
        question2 = request.form.get('question2')
        if question2 == '1':
            points = points + 1

        question3 = request.form.get('question3')
        if question3 == '1':
            points = points + 1
        
        question4 = request.form.get('question4')
        if question4 == '1':
            points = points + 1

        question5 = request.form.get('question5')
        if question5 == '2':
            points = points + 1
    
    return render_template("check.html", result=points)
   
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=3333)