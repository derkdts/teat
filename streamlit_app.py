import streamlit as st
import streamlit.components.v1 as components
 

def main():
  st.title("Чек-лист по городам")
 

  # Добавляем JavaScript для изменения заголовка страницы
components.html(
"""
<script>
document.title = 'Чек-лист по городам';
</script>
""",
height=0,
)
 

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
  for key in st.session_state.checkbox_states:
   st.session_state.checkbox_states[key] = False
 

  st.button("Сбросить прогресс", on_click=reset_progress)
 

cols = st.columns(3)
i = 0
for key, label in checklist_items.items():
  col_num = i % 3
  st.session_state.checkbox_states[key] = cols[col_num].checkbox(label, key=key, value=st.session_state.checkbox_states[key])
  i+=1
 

  completed_count = sum(st.session_state.checkbox_states.values())
  total_count = len(checklist_items)
 

  progress_percent = int((completed_count / total_count) * 100)
  st.progress(progress_percent)
  st.write(f"Выполнено: {progress_percent}% ({completed_count}/{total_count})")
 

if completed_count == total_count:
  st.success("Поздравляем! Все пункты выполнены!")
 

if __name__ == "__main__":
  main()
