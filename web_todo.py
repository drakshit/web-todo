
import streamlit as st

from modules import functions

todos = functions.file_operation('r', filename='todos.txt')

def add_todo():
    _todo = st.session_state['new_todo']
    if len(_todo) > 0:
        todos.append(_todo + '\n')
        functions.file_operation('w', todos)
        st.session_state.new_todo = ''
    else:
        print("Please enter a todo item!")

st.title("My ToDo App")
st.subheader("This is my ToDo app")
st.write("This app is to increase your productivity")

st.text_input(label="Enter a new ToDo", placeholder="Your ToDo", on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.file_operation('w', todos)
        del st.session_state[todo]
        st.rerun()

st.session_state