import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# st.title("This is the title")

# st.header("This is the header")
# st.subheader("Subheader")
# st.write("This is regular text")

# somelist= [1,2,3]
# st.write(somelist)


# df = pd.DataFrame(
#     np.random.randn(50, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(df) 

# st.image("https://g.foolcdn.com/image/?url=https%3A%2F%2Fmedia.ycharts.com%2Fcharts%2F8cf10687757fae4d91fccc8da5af2c7c.png&w=700")

st.sidebar.title("Option")
option = st.sidebar.selectbox('Which Dashboard',("Charts", "Patterns"))
st.header(option)

if option == "Charts":
  st.subheader("Charts Dashboard")
  symbol =st.sidebar.text_input("Symbol", value="TSLA", max_chars=5)
  st.image(f"https://finviz.com/chart.ashx?t={symbol}&p=w&tas=0")
  st.header(symbol)
  tickerdata = yf.Ticker(symbol)
  tickerdf = tickerdata.history(period="max")
  st.line_chart(tickerdf.Close)
  st.line_chart(tickerdf.Volume)

  # financials
  hodl = tickerdata.institutional_holders
  recom= tickerdata.recommendations
  finan =tickerdata.financials
  balance = tickerdata.balance_sheet
  maj = tickerdata.major_holders
  st.header(hodl)
  st.header(maj)
  st.text(recom)
  st.text(balance)
  st.header(finan)







if option == "Patterns":
  st.subheader("Patterns dashboard")

