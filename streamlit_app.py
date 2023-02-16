import streamlit;
streamlit.title(' My parents new healthy dinner')
streamlit.header('🙌Breakfast Menu')
streamlit.text('🍌🥝Banana oatmeal')
streamlit.text('🥪🥪Kale egg and avacado')
streamlit.text('🍳🍟🍵Egg omelette with mushroom')

streamlit.header('Build your own fruit smoothie')

import pandas;
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.header('Build your own .m fruit smoothie')
realans = ['', 'abc', 'edf']
streamlit.dataframe(my_fruit_list)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header("Fruityvice Fruit Advice!")
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


