from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def search():
    return render_template("search.html")

@app.route("/advanced")
def advanced_search():
    return render_template("advancedsearch.html")


@app.route("/image")
def image_search():
    return render_template("imagesearch.html")

if __name__ == "__main__":
    app.run(debug=True)
