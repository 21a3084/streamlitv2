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
date_month = st.sidebar.slider('date(month)',1,12)
date_date = st.sidebar.slider('date(date)',1,31)
'date:',date_month,'月',date_date,'日'

expander1 = st.selectbox('どの端末で遊びたいのか？',('','コンピューター','スマホ'))
st.write(expander1,'で遊びたい') 
if expander1=='コンピューター':
  expander2 = st.selectbox('オンラインゲームそれどもオフラインゲーム？',(' ','オンラインゲーム','オフラインゲーム'))
  st.write(expander2,'を選んだ')
  if expander2=='オンラインゲーム':
    st.write('へー、じゃ自分で探してｗ')
  if expander2=='オフラインゲーム':
    st.write('steam,epicとかこれらのストアがおすすめだよ')
if expander1=='スマホ':
   expander2 = st.selectbox('オンラインゲームそれどもオフラインゲーム？',(' ','オンラインゲーム','オフラインゲーム'))
   st.write(expander2,'を選んだ')
   if expander2=='オンラインゲーム':
    st.write('MiHoYo最高！！！')
   if expander2=='オフラインゲーム':
    st.write('mincraft，Don`t Straveとかのゲームがおすすめだよ(オンラインでもできるよ)')
