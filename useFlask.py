from flask import Flask, url_for

app = Flask(__name__)


# @app.route('/')
@app.route('/index')
def hello():
    return "Привет, Яндекс!"


@app.route('/name/<nm>')
def name(nm):
    with open('index1.html','r') as file:
        txt = file.read()
        return txt.replace("Python", nm)


@app.route('/image_sample')
def image():
    return '''
    <h1>картинка</h1>
    <img src="{}" alt="здесь должна была быть картинка, 
    но не нашлась">'''.format(url_for('static', filename='img/rihana.jpg'))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')