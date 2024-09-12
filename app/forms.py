from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

from .models import Category
from . import app


def get_categories():
    with app.app_context():
        categories = Category.query.all()
    return [(category.id, category.title) for category in categories]


class NewsForm(FlaskForm):
    title = StringField('Название',
                       validators=[DataRequired(message="Поле не должно быть пустым!"),
                                   Length(max=255, message='Введите заголовок длиной до 255 символов')])
    text = TextAreaField('Текст',
                         validators=[DataRequired(message="Поле не должно быть пустым!")])
    category = SelectField(choices=get_categories())
    submit = SubmitField('Добавить')