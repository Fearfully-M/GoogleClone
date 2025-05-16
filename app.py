from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def search():
    return render_template("search.html",
    heading = 'Google Clone', 
    title ='Google Clone',
    show_title = True)

@app.route("/advanced")
def advanced_search():
    return render_template("advancedsearch.html",
    heading = 'Advanced Search',
    title = 'Advanced Search',
    show_title = True)


@app.route("/image")
def image_search():
    return render_template("imagesearch.html",
    heading = 'Image Search',
    title = 'Image Search',
    show_title = True)

if __name__ == "__main__":
    app.run(debug=True)
