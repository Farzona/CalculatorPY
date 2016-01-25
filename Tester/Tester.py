from flask import Flask, render_template, url_for
app = Flask(__name__,)
  
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=['POST'])
def check():
    return render_template("check.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=3333)