from flask import Flask

app = Flask(__name__)

@app_route('/')
def homepage():
    return render_template('index.html')

if name == '__main__':
    app.run()
