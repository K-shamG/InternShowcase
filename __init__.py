from flask import Flask, render_template

app = Flask(__name__)

@app_route('/')
def homepage():
    return render_template('index.html')

@app_route('/india.html')
def india():
    return render_templates('india.html')

@app_route('/about.html')
def about():
    return render_template('about.html')


if name == '__main__':
    app.run()
