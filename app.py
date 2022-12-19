import streamlit as st

# UI
st.title('Home page')
st.markdown("# title 1")
st.markdown("## title 1.1")
st.markdown("# title 2")
st.write('lets write some streamlit')
st.sidebar.markdown("# Homepage")

# assign some variable
from src.model import Model
import src.global_data as DATA
DATA.globalmodel = Model()

# display some variable
from dotenv import dotenv_values
env = dotenv_values(".env") 
st.write("variable from .env file : " + env['some_variable'] )

