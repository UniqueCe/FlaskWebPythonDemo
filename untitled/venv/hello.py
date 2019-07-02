
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# 数据库
import os
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'Help Me!'

# 数据库
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 表单
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('提交')


# 数据模型 Role和User
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username




@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name '
                  '看起来你已经改变了你的名字')

        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',
                           current_time=datetime.utcnow(),
                           form=form,
                           name=session.get('name'))


@app.route('/user')
def user():
    return render_template('user.html',
                           current_time=datetime.utcnow(),
                           name="User")

@app.route('/user/<name>')
def username(name):
    return render_template('user.html',
                           current_time=datetime.utcnow(),
                           name=name)

@app.route('/YX')
def YX():
    return '<h1>hello, 闫总! 好骚呀~ </h1>'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',
                           current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_sever_error(e):
    return render_template('500.html',
                           current_time=datetime.utcnow()), 500




if __name__ == '__main__':
    print('...')
    app.run()
    print(db)
