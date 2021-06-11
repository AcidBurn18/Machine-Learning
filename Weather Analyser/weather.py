import streamlit as st
import pandas as pd
['Temperature (C)', 'Apparent Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Wind Bearing (degrees)', 'Visibility (km)', 'Loud Cover', 'Pressure (millibars)']]
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from sklearn.metrics import mean_absolute_error
st.write("""

Weather Prediciton""")

st.sidebar.header("User Input")
def user_input():
  temperature=st.sidebar.slider('Temperature in Celcius',-10,49.8,20.0)
  app_temperature=st.sidebar.slider('Apparent Temperature (C)',-10,49.8,20.0)
  humidity=st.sidebar.slider('Humidity in %',0,1,0.51)
  wind_speed=st.sidebar.slider('Wind Speed in Km/h',5,80,16)
  wind_bearing=st.sidebar.slider('Wind bearing',0,360,235)
  visibility=st.sidebar.slider('Visibility',0,30,15)
  loud_cover=st.sidebar.slider('Loud Cover',0,0,0)
  pressure=st.sidebar.slider('Pressure(millibar)',998,1050,1001.01)
  data={'Temperature':temperature,
        'Apparent Temperature':app_temperature,
        'Humidty':humidity,
        'Wind Speed':wind_speed,
        'Wind Bearing':wind_bearing,
        'Visibility':Visibility,
        'Loud Cover':loud_cover,
        'Pressure':pressure}
  f=pd.DataFrame(data,index[0])
  return f

def main():

  df=pd.read_csv('weatherHistory.csv',parse_dates=['Formatted Date'])
  df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
  df = df.set_index('Formatted Date')

  le=preprocessing.LabelEncoder()
  df['Summary']=le.fit_transform(df['Daily Summary'])

  unique_summary=df['Summary'].unique()
  unique_daily_summary=df['Daily Summary'].unique()
  weather_map={unique_summary[i]:unique_daily_summary[i] for i in range(len(unique_summary))}

  summary=df.pop('Daily Summary')
  summary.fillna('Dilemma')

  data_columns = ['Summary','Temperature (C)', 'Apparent Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Wind Bearing (degrees)', 'Visibility (km)', 'Loud Cover', 'Pressure (millibars)']
  df_monthly_mean = df[data_columns].resample('MS').mean()
  df_monthly_mean.reset_index(inplace=True)

  summary1=pd.DataFrame(summary)

  col_y=df_monthly_mean[['Summary']]
  col_x_=df_monthly_mean[['Temperature (C)', 'Apparent Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Wind Bearing (degrees)', 'Visibility (km)', 'Loud Cover', 'Pressure (millibars)']]

  x_train,x_test,y_train,y_test=train_test_split(col_x_,col_y,test_size=0.20,random_state=True)

  regression = LinearRegression()
  regression.fit(x_train, y_train)

  pred_y = regression.predict(x_test)

  prediction = pd.DataFrame({'P summary': [k for k in pred_y],'Actual summ':[j for j in y_test['Summary']]})

  call=user_input()
  st.subheader('Input Data')
  st.write(call)
  t=numpy.array(call.values)
  for i in range(8):
    temp.append(t[0][i])
  g=regression.predict([temp])
  #f=[33,31,0.51,13,250,16,0.0,1001.25]
  #fg=[-1.677942,	-4.173708,	0.834610,	8.894211,	161.018817,	7.894064,	0.0,	1021.204960]
 # g=regression.predict([fg])
  if (int(g)>max(unique_summary)):
    out=weather_map[max(unique_summary)]

  else:
    out=weather_map[int(g)]
  st.subheader("Prediction")
  st.write(out)
if __name__== '__main__':
  main()