import streamlit as st
import pandas as pd
import numpy as np
import time
import random

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

# write by magic
st.write('Display by magic:')
df

# write by st.write
st.write('Display by st.write:')
st.write(df)

# st.dataframe
st.write("Display by st.dataframe:")
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

# pandas styler
st.write("Display with pandas styler")
df_styler = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))
)
st.dataframe(df_styler.style.highlight_max(axis=0))

# st.table
st.write("Display by table")
st.table(df_styler)

# line chart
st.write("Draw a line chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a','b','c']
)
st.line_chart(chart_data)

# plot a map
st.write("Draw a map")
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
# st.table(map_data)
st.map(map_data)

# widget
st.write("Display a widget by st.slider")
x = st.slider('x')
st.write(x, 'squared is', x*x)

# st.text_input
st.write("Demo of st.text_input, st.session_state")
st.text_input("Please input your name:", key="name")
st.write("Your name is", st.session_state.name)

# st.checkbox
st.write("Demo of st.checkbox")
if (st.checkbox('Show Data')):
    hide_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a', 'b', 'c']
    )
    hide_data

# st.selectbox
st.write("Demo of st.selectbox")
df = pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [10,20,30,40,50]
})
option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected:', option

# st.sidebar
st.write("Demo of sidebar")
# add a select box to side bar
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', "Home Phone", "Mobile Phone")
)

# add a slider to the side bar
add_slider = st.sidebar.slider(
    'Select a range of values:',
    0.0, 100.0, (25.0, 75.0)
)

# st.expander
st.write("Demo of st.expander")
left_col, right_col = st.columns(2)
# We can use a column as sidebar
left_col.button("Press me!")

# Use 'with' to control expender
with right_col:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")

# progress
'Starting a long computation...'

# add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(random.randint(0,3))

'... and now we\' are done!'
