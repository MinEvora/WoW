from flask import Flask, render_template

app = Flask("__name__", template_folder="src/template", static_folder="src/static")

@app.route('/')
@app.route ( "/index" )
def index():
    return render_template("index.html")

@app.route('/membros')
def membros():
    return render_template("membros.html")

@app.route('/setlist')
def setlist():
    return render_template("setlist.html")

    
if __name__ == "__main__":
 app.run()