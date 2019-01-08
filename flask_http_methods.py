import os
ABSPATH = os.path.abspath('.')

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, template_folder=ABSPATH+'/html')

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name.title()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))

#@app.route('/loginbypass/<user>')
#def loginbypass(user):
#    return redirect(url_for('success',name=user))
    
@app.route('/')
def user_page():
    return render_template('flask_3.html')
    
if __name__ == '__main__':
    app.run(debug = True)