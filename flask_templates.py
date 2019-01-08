import os
ABSPATH = os.path.abspath('.')

from flask import Flask, render_template
app = Flask(__name__, template_folder=ABSPATH+'/html')

@app.route('/hello/<name>')
def throw_webpage(name):
    return render_template('hello.html', name=name)

@app.route('/marks/<int:score>')
def throw_webpage_marks(score):
    return render_template('marks.html', marks=score)

if __name__ == '__main__':
    app.run(debug=True)