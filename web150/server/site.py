from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask_wtf import FlaskForm
import wtforms
from promomaker import make_promo
from random import randint

app = Flask(__name__)

FLAG = "flag{burg3r5_4nd_c0k3_fr0m_j4cqu3_fr35c0}"
app.config['SECRET_KEY'] = '76ft23fr&F61'
app.config['WTF_CSRF_CHECK_DEFAULT'] = False


class SchemeForm(FlaskForm):
    cheeseburger = wtforms.BooleanField('🧀Чизбургер')
    hamburger = wtforms.BooleanField('🍔Гамбургер')
    shrimpburger = wtforms.BooleanField('🦐Шримпбургер')
    big_king = wtforms.BooleanField('👑Биг Кинг')
    roll = wtforms.BooleanField('🌯Ролл')
    potato_fri = wtforms.BooleanField('🍟Картошка фри')
    potato_country = wtforms.BooleanField('🍿Картошка по-деревенски')
    nuggets = wtforms.BooleanField('🍘Наггетсы')
    chicken = wtforms.BooleanField('🐔Курочка')
    icecream = wtforms.BooleanField('🍦Мороженое')
    coke = wtforms.BooleanField('🥤Кола')
    lipton = wtforms.BooleanField('🍷Липтон')
    mirinda = wtforms.BooleanField('🍹Миринда')

    submit = wtforms.SubmitField('Take')

SchemeForm.WTF_CSRF_CHECK_DEFAULT = False

def check_if_any_choosen(form: SchemeForm):
    return any([form.cheeseburger.data, form.hamburger.data, form.shrimpburger.data, form.big_king.data, form.roll.data,
                form.potato_fri.data, form.potato_country.data, form.nuggets.data, form.chicken.data, form.icecream.data,
                form.coke.data, form.lipton.data, form.mirinda.data])


def check_if_order_correct(form: SchemeForm):
    if all([form.big_king.data, form.mirinda.data, form.coke.data, form.roll.data, form.chicken.data, form.icecream.data, form.potato_fri.data]):
        if not any([form.shrimpburger.data, form.hamburger.data, form.cheeseburger.data, form.potato_country.data, form.nuggets.data, form.lipton.data]):
            return True
        return False
    return False


@app.route('/web150', methods=['GET', 'POST'])
def main():
    form = SchemeForm()
    if request.method == "POST":
        chance = randint(1, 10)
        if check_if_any_choosen(form):
            promocode = "Твой пацанский промик: "
            if check_if_order_correct(form):
                promocode += FLAG
            else:
                if chance < 8:
                    promocode += make_promo()
                else:
                    promocode += "Этот промик почти на выкате, вейтни немного)"
        else:
            promocode = "🚚До промика на воздух мы еще не доехали, бро😎"
        return render_template('promo.html', promocode=promocode)
    return render_template('CXEMbl.html', form=form)


if __name__ == "__main__":
    app.run()
