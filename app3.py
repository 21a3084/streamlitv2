#%%writefile app.py
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("ゲーム推薦！！！")

st.write('自分の好きなゲームを選ぼう！！')


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(  ' ^_^   まもなく...')
  bar.progress(i+1)
  time.sleep(0.001)
  if(i==50):
    latest_iteration.write(f'Iteration{i+1}')
    'Done!!!!!!!'
    
left_column,right_column =st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('???')
    time.sleep(1)
    right_column.write('何が用？')
    time.sleep(1)
    right_column.write('???')
condition = st.sidebar.slider('100',0,100,50)
'100',condition

expander1 = st.selectbox('どの端末で遊びたいのか？',('コンピューター','スマホ'))
st.write(expender1,'で遊びたい ') 
if st.checkbox('check'):
      
      expander1=st.expander('checkじゃないよ、チェック！！！') 
expander2 = st.expander('チェックabaac')
expander2.write('はい？なんで俺を押すの？')
expander3 = st.expander('チェック')
expander3.write('問い合わせ3の内容を書く')
