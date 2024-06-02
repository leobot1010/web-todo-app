import streamlit as st
from functions import get_todos, write_todos

todos = get_todos("todos.txt")

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

st.checkbox("Buy grocery")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Add new todo...")