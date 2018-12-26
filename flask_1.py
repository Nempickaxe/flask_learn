from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
   return 'Hello %s!!'%name

@app.route('/dudeness')
def give_party():
    return ', '.join(['Nope'])*3+'!!'

if __name__ == '__main__':
   app.run(debug = True)