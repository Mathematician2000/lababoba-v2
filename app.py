import streamlit as st

st.set_page_config(
    page_title='ЛабаБоба! v2',
    page_icon=(
        'https://raw.githubusercontent.com/Mathematician2000/'
        'lababoba-v2/master/icon.png'
    ),
)


from model import (
    DEFAULT_MAX_LEN, HEIGHT, MIN_LEN, MAX_CHARS, MAX_LEN, MODEL,
)
from utils import set_background


set_background(
    'https://raw.githubusercontent.com/Mathematician2000/'
    'lababoba-v2/master/background.png'
)


st.title('ЛабаБоба v2 приветствует Вас!')
st.markdown(r'''
Даже не делайте вид, что не узнали меня.
Это же я, **ЛабаБоба**! Вернее *лучшая* версия
[оного](https://share.streamlit.io/mathematician2000/lababoba/app.py)
 (моё почтение).

Нет, я не лаборатория и к таверне не имею никакого отношения.
Да, я знаком с [Балабобой](https://yandex.ru/lab/yalm), мы родственники.
Ещё вопросы?

Если нет, то бегите скорее и *потрансформируйте* уже что-нибудь уже!
''')


prompt = st.text_area(
    'Начните текст, а ЛабаБоба продолжит:',
    'Что делать, если нечем заняться? Можно, например',
    height=HEIGHT,
    max_chars=MAX_CHARS,
    help='Не тормози, вводи текст и жми кнопку :)',
    placeholder='А текст кто писать будет, Боб, что ли?',
).lstrip()

max_length = st.slider(
    'Максимальная длина выходного текста (в словах)',
    MIN_LEN,
    MAX_LEN,
    DEFAULT_MAX_LEN,
    help='Обычный слайдер длины текста, что такого?',
)

button = st.button('Налабабобить')


MODEL.clear_output()
if button:
    try:
        if prompt:
            MODEL.run_model(
                prompt,
                max_length=max_length,
            )
    except Exception as err:
        st.exception(
            'OMG WHAT THE HELL IS GOING ON HERE '
            f'JUST LOOK AT THIS MADNESS:\n{err}'
        )

st.markdown(MODEL.get_last_output())

st.markdown('_' * 10)
st.markdown('by [Mathematician2000](https://gitlab.com/Mathematician2000)')
