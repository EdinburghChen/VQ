import datetime
import sqlite3
from bs4 import BeautifulSoup
import requests
import streamlit as st
import pandas as pd
import random as rd

#streamlit run VehicleDriverQuery.py
# LINE Notify 權杖
token = ''

# 要發送的訊息
message = '\n查詢結果:\n'

# 設定網頁標題
st.title('車輛駕駛查詢')
# 加入網頁文字內容
# 建立文字方塊
txt車牌 = st.text_input(
    label="請輸入車牌：",
    help="請輸入查詢車牌",
    max_chars=7,
)

# 顯示文字方塊的值
#st.write(txt車牌)
#建立資料庫連線
conn=sqlite3.connect("./db/bmdb.db")

try:
  # 建立資料庫連線 SQLite
  cursor=conn.cursor()
  sqlQueryStr="SELECT 車牌,駕駛,姓名代號,建檔日期 FROM '車輛使用人' where 車牌='"+  txt車牌 + "'"
  cursor.execute(sqlQueryStr)

  # 將查詢結果轉換為串列
  results = cursor.fetchall()
  #Close the database connection

  # 檢查查詢結果筆數
  if cursor.fetchall() == []:
    st.write("查無資料")
  conn.close() 

  # 顯示查詢結果
  for result in results:
   st.write("車輛登記駕駛: "+result[1]+"(" + result[2]+")")
  
    
    
except Exception as e:
  st.write("Error: %s" % e)
