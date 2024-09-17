from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/about.html')
def about ():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
