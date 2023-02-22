import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.subheader('Classic English Breakfast')
streamlit.text('🍞Contains bread,french fries,baked beans,scrambled eggs. Options: Chicken, Ham, Pork')
streamlit.subheader('Good Morning Life :-)')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.header('Lunch Menu')
streamlit.subheader('🥗Continental Bonanza!')
streamlit.text(' Contains Soup, choice of non veg, rice/bread Options: Chicken, fish, beef')
streamlit.header('Dinner Menu')
streamlit.subheader('Light and funnnn')
streamlit.text(' Options: 🥣Soup, Thai noodles, pasta, Chicken rice')
streamlit.header('Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
