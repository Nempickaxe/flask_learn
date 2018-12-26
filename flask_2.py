from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def get_admin():
    return 'Hello admin'

@app.route('/guest/<guest>')
def get_guest(guest):
    return 'Hello Mr %s'%guest

@app.route('/user/<name>')
def get_anyone(name):
    if name=='admin':
        return redirect(url_for('get_admin'))
    else:
        return redirect(url_for('get_guest', guest=name))
        
if __name__ == '__main__':
    app.run(debug=True)