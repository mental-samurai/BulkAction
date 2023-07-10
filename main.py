# ('/other') - от корня (root)
# ('./other') - от текущей директории
# ('../other') - выйти из текущей директории
# ('other') - в корне (на данном уровне с main.py)
# ('../../other')
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Salam'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
