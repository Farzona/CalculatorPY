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

    return render_template("check.html", result=points)
   
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=3333)