
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime



app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)



@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user')
def user():
    return render_template('user.html', current_time=datetime.utcnow(), name="User")

@app.route('/user/<name>')
def username(name):
    return render_template('user.html', current_time=datetime.utcnow(), name=name)

@app.route('/YX')
def YX():
    return '<h1>hello, 闫总! 好骚呀~ </h1>'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_sever_error(e):
    return render_template('500.html', current_time=datetime.utcnow()), 500


if __name__ == '__main__':
    print('...')
    app.run()
