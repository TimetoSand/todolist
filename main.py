from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from datetime import datetime
import os
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class TodoList(db.Model):
    id = Column(Integer, primary_key=True)
    listItem = Column(String, nullable=False, unique=True)


db.create_all()


class ListForm(FlaskForm):
    listItem = StringField(" ", render_kw={"placeholder": "New Item"})
    submit = SubmitField("+")


class JukeForm(FlaskForm):
    check = BooleanField(" ")


today = datetime.today()
day = today.strftime('%A')
date = today.strftime("%d %B %Y")

if day == "Sunday":
    db.session.query(TodoList).delete()
    db.session.commit()


@app.route("/", methods=["GET", "POST"])
def home():
    listen = TodoList.query.all()
    form_j = JukeForm()
    form = ListForm()
    if form.validate_on_submit():
        new_item = TodoList(
            listItem=request.form.get('listItem')
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect("/")
    return render_template("list.html", day=day, date=date, form=form, form_j=form_j, list=listen)


if __name__ == "__main__":
    app.run(debug=True)

# TODO: get day
# TODO:create as form todo list
# TODO: add database
