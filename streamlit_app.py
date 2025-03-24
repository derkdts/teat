import streamlit as st
 

def page_one():
  st.header("Страница с чек-листом по городам")
  # Ваш код для чек-листа по городам здесь...
  checklist_items = {
  "checkbox_A": "A, B - Алматы",
  "checkbox_Z": "Z - Астана",
  "checkbox_X": "Х - Шымкент",
  "checkbox_D": "D - Актобе",
  "checkbox_R": "R - Актау",
  "checkbox_U": "U - Семей",
  "checkbox_F": "F - Усть-Каменогорск",
  "checkbox_S": "S - Павлодар",
  "checkbox_C": "C - Кокшетау",
  "checkbox_M": "M - Караганда",
  "checkbox_P": "P - Костанай",
  "checkbox_H": "H - Тараз",
  "checkbox_T": "T - Петропавловск"
  }
 

if 'checkbox_states' not in st.session_state:
  st.session_state.checkbox_states = {key: False for key in checklist_items}
 

def reset_progress():
  st.session_state.checkbox_states = {key: False for key in checklist_items}
 

st.button("Сбросить прогресс", on_click=reset_progress)
 

cols = st.columns(3)
for i, (key, label) in enumerate(checklist_items.items()):
  col_num = i % 3
  st.session_state.checkbox_states[key] = cols[col_num].checkbox(label, key=key, value=st.session_state.checkbox_states[key])
 

completed_count = sum(st.session_state.checkbox_states.values())
total_count = len(checklist_items)
 

progress_percent = int((completed_count / total_count) * 100)
st.progress(progress_percent)
st.write(f"Выполнено: {progress_percent}% ({completed_count}/{total_count})")
 

if completed_count == total_count:
  st.success("Поздравляем! Все пункты выполнены!")
 

def page_two():
  st.header("To-Do List")
 

  # Initialize session state for tasks
if 'tasks' not in st.session_state:
  st.session_state.tasks = []
 

  # Function to add a task
def add_task():
  task = st.session_state.new_task
  st.session_state.tasks.append(task)
  st.session_state.new_task = ""  # Clear the input
 

  # Input for new task
st.text_input("Новая задача:", key="new_task", on_change=add_task)
 

  # Display tasks with checkboxes
for i, task in enumerate(st.session_state.tasks):
  checkbox_key = f"task_{i}"
  st.checkbox(task, key=checkbox_key)
 

def main():
  st.sidebar.title("Навигация")
  page = st.sidebar.selectbox("Выберите страницу", ["Чек-лист по городам", "To-Do List"])
 

if page == "Чек-лист по городам":
  page_one()
elif page == "To-Do List":
  page_two()
 

if __name__ == "__main__":
  main()
