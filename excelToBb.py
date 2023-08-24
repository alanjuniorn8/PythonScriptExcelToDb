import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from dotenv import dotenv_values

config = dotenv_values(".env")

url = URL.create(
    drivername=config['DRIVERNAME'],
    username=config['USERNAME'],
    host=config['HOST'],
    database=config['DATABASE'],
    password=config['PASSWORD']
)

engine = create_engine(url)

df = pd.read_excel(config['SHEET'])

with engine.begin() as connection:
  df.to_sql(name=config['TABLE'], con=connection, if_exists='append', index=False)
