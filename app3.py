#%%writefile app.py
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("watashi !")

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(50):
  latest_iteration.text(  ' ^_^   まもなく...')
  bar.progress(i+1)
  time.sleep(0.1)
  if(i==50):
    latest_iteration.text(f'Iteration{i+1}')
'Done!!!!!!!'
left_column,right_column =st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('???')
    time.sleep(1)
    right_column.write('何が用？')
    time.sleep(1)
    right_column.write('???')
expander1 = st.expander('チェック入れてみて')
if st.checkbox('check'):
      expander1.write('checkじゃないよ、チェック！！！') 
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の内容を書く')
condition=st.slider('abaaabaabbbaa',0,100,50)
'abababa:',text
'abaaaba',condition
if st.checkbox('Show Image'):
  img = Image.open('efg.jpg')
  st.image(img,caption='watashi',use_column_width=True)
