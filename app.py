from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lenses')
def lenses():
    return render_template('lenses.html')

@app.route('/iso')
def iso():
    return render_template('iso.html')

@app.route('/aperture')
def aperture():
    return render_template('aperture.html')

@app.route('/shutter-speed')
def shutter_speed():
    return render_template('shutter_speed.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
