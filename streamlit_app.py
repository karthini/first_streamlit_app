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

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
streamlit.header("Fruityvice Fruit Advice!")
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
