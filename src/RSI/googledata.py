import pandas
import requests
import io

stock = 'GOOG'
startdate = 'Jul 08, 2021'
enddate = 'Aug 08, 2021'

rooturl = 'http://www.google.com/finance/historical?q='
query = stock + '&startdate=' + startdate +'&enddate=' + enddate + '&output=csv'

url = rooturl + query
response = requests.get(url)
df = pandas.read_csv(io.StringIO(response.content.decode('utf-8')))

print(df)