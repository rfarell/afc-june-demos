import streamlit as st
import inspect
import textwrap
import time
import numpy as np
from utils import show_code

st.set_page_config(page_title="Video Demos", page_icon="📈")
st.markdown("# Video Demos")
st.sidebar.header("Video Demos")
st.write()

st.video('https://www.youtube.com/watch?v=sxsnwkKISWE') 