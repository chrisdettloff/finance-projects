import numpy as np
import pandas as pd
import math
import requests
import xlsxwriter
from secrets import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv('sp_500_stocks.csv')
print(stocks)