import time

import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu


def option_menu_style():
    return option_menu(
        menu_title=None,
        options=["Конституция РФ", "Уголовный кодекс", "Трудовой кодекс"],
        icons=["book", "book", "book"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "nav-link": {
                "font-size": "14px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            }
        },
        # styles={
        #     "container": {"padding": "!important", "background-color": "#fafafa"},
        #     "icon": {"color": "orange", "font-size": "25px"},
        #     "nav-link": {
        #         "font-size": "14px",
        #         "text-align": "left",
        #         "margin": "0px",
        #         "--hover-color": "#eee",
        #     },
        #     "nav-link-selected": {"background-color": "green"},
        # },
    )


def _hide_streamlit_menu():
    hide_menu_style = """
        <style>
        #MainMenu {visibility : hidden; }
        footer {visibility : hidden; }
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)


@st.cache()
def AI_thinking(question: str):
    print(question)
    time.sleep(5)
    return "Сам думай, я не хочу на это отвечать, кожанный ублюдко!" + question


def main():
    img = Image.open('resurses/o5h0mamujPM.jpg')
    st.set_page_config(page_title="FindAnswer App", page_icon=img)
    _hide_streamlit_menu()
    selected_menu = option_menu_style()
    if selected_menu == "Конституция РФ":
        st.write("Вы вбрали Конституцию")
    if selected_menu == "Уголовный кодекс":
        st.write("Вы вбрали Уголовный кодекс")
    if selected_menu == "Трудовой кодекс":
        st.write("Трудовой кодекс")

    question = st.text_area("Введите вопрос", "")
    if st.button("Get Answer", disabled=question == ""):
        answer = AI_thinking(question)
        st.write(f'Ответ на ваш вопрос {answer}')


if __name__ == "__main__":
    main()