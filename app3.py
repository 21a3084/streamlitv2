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
button=left_column.button('ゲーム嫌いな人はここを押してください')
if button:
    right_column.write('???')
    time.sleep(1)
    right_column.write('じゃなんでこのページを開くの？？？？')
    time.sleep(1)
    right_column.write('???')
condition = st.sidebar.slider('100',0,100,50)
'100',condition

expander1 = st.selectbox('どの端末で遊びたいのか？',('コンピューター','スマホ'))
st.write(expander1,'で遊びたい') 
if expander1=='コンピューター':
  expander2 = st.selectbox('オンラインゲームそれどもオフラインゲーム？',('オンラインゲーム','オフラインゲーム'))
  st.write(expander1,'を選んだ')
  if expander2=='オンラインゲーム':
    st.write('へー、じゃ自分で探してｗ')
    break
  if expander2=='オフラインゲーム':
    st.write('steam,epicとかこれらのストアがおすすめだよ')
  
