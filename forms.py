from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class TickerForm(FlaskForm):
  ticker = StringField('Ticker: ',
                      validators=[DataRequired()], render_kw={"placeholder": "Ticker"})
  submit = SubmitField('🔎')
