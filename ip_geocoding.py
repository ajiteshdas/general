import requests
import lxml.html as html
import pandas as pd

ip_data = ['xx.xx.xx.xx.', 'xx.xx.xx.xx',....]

latitude = []
longitude = []
city = []
ip_addr = []

for i in ip_data:
  url = 'http://api.ipstack.com/'+'?access_key=[API_KEY]&format=1'
  page = requests.get(url)
  
  ip_addr.append(i)
  
  lat = page.json()['latitude']
  latitude.append(lat)
  
  long = page.json()['longitude']
  longitude.append(long)
  
  cities = page.json()['city']
  city.append(cities)
  
data_dict = {'IP address':ip_addr,'City':city,'Latitude':latitude,'Longitude':longitude}
dataFrame = pd.DataFrame(data_dict)
dataframe.to_csv('ip_data.csv')
