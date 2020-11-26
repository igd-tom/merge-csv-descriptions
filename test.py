
import pandas as pd


# _priceList1 = ['1']*10
# _priceList2 = ['2']*10
# _priceList3 = ['3']*10
# _type = ['per_item']*10
# _currencyCode = ['GBP']*10
# _roundingType = ['no_rounding']*10

# print(_type)

s = pd.Series(['null_charm'])

s= s.repeat(10)

print(s)