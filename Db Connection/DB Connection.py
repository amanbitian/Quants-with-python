import sqlalchemy
import pymysql
import pandas as pd
import ssl
import yfinance as yf

# Ignore SSL certificate verification (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context

# pymysql.install_as_MySQLdb()
# ## By invoking pymysql.install_as_MySQLdb(), you make it so that when a package or
# # module attempts to import MySQLdb, it will load pymysql instead, ensuring compatibility with Python 3
# # and allowing the code to work without needing to make changes elsewhere in the codebase.
#
## We need to create 3 schema
indices= ["Nifty50", "RTSI", "Bovespa"]

def schemacreator(index):
    engine=sqlalchemy.create_engine("mysql://root:EgFf5433fhh5EdHG1hCeG6bcfc5Bhaec@viaduct.proxy.rlwy.net:26326/")
    engine.execute(sqlalchemy.schema.CreateSchema(index))
    print("Connected to sql server")

for index in indices:
    schemacreator(index)

###
nifty50=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')[2]

nifty200= pd.read_html('https://en.wikipedia.org/wiki/NIFTY_500')[2] #, skiprows=1)[2]
# rts = pd.read_html('https://en.wikipedia.org/wiki/RTS_Index')[1]
nifty50['Symbol']=nifty50['Symbol'] + ".NS"
nifty50_symbol= nifty50.Symbol.to_list()

# Set the second row as column names
new_header = nifty200.iloc[0]  # Get the second row as the new header
nifty200 = nifty200[1:]  # Skip the first row in the DataFrame
nifty200.columns = new_header
nifty200['Symbol']=nifty200['Symbol'] + ".NS"
nifty200_symbol= nifty200.Symbol.to_list()

print(nifty200.info())
print(nifty200_symbol)

####
c=0
for i in nifty50_symbol:
    if i in(nifty200_symbol):
        # print(f"duplicate {i}")
        c=c+1
print(c)



#
#
# engine=sqlalchemy.create_engine("mysql://root:EgFf5433fhh5EdHG1hCeG6bcfc5Bhaec@viaduct.proxy.rlwy.net:26326/")
# engine.execute(sqlalchemy.schema.CreateSchema("Nifty200"))
# print("Schema created")
#
# # engine=sqlalchemy.create_engine("mysql://root:EgFf5433fhh5EdHG1hCeG6bcfc5Bhaec@viaduct.proxy.rlwy.net:26326/"+"Nifty200")
# for symbol in nifty200_symbol:
#     df= yf.download(nifty200_symbol[0], start="2017-01-01")
#     df=df.reset_index()
#     df.to_sql(symbol, engine)
