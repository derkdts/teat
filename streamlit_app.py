 import streamlit as st
 

 def main():
  st.title("Чек-лист по городам")
 

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
  "checkbox_T": "Т - Петропавловск"
  }
 

  if 'checkbox_states' not in st.session_state:
  st.session_state.checkbox_states = {key: False for key in checklist_items}
 

  cols = st.columns(3) 
  i = 0
  for key, label in checklist_items.items():
  col_num = i % 3 
  st.session_state.checkbox_states[key] = cols[col_num].checkbox(label, key=key)
  i+=1
 

  completed_count = sum(st.session_state.checkbox_states.values())
 

  if completed_count == len(checklist_items):
  st.success("Поздравляем! Все пункты выполнены!")
  if st.button("Сбросить прогресс"):
  st.session_state.checkbox_states = {key: False for key in checklist_items}
  st.rerun() 

 if __name__ == "__main__":
  main()
