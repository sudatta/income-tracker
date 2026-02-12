from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Optional
from models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=80)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            from app import t
            raise ValidationError(t("username_taken"))


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class JournalEntryForm(FlaskForm):
    date = DateField("Date", validators=[DataRequired()], default=date.today)
    expenses = FloatField("Expenses", validators=[Optional()], default=0.0)
    income = FloatField("Income", validators=[Optional()], default=0.0)
    withdrawals = FloatField("Withdrawals", validators=[Optional()], default=0.0)
    notes = TextAreaField("Notes", validators=[Optional()])
