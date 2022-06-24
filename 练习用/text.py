'''
Author: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-06-24 21:35:17
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
LastEditTime: 2022-06-24 21:35:18
FilePath: /Python-100-Days/练习用/text.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
prices = {
      'AAPL': 191.88,
      'GOOG': 1186.96,
      'IBM': 149.24,
      'ORCL': 48.44,
      'ACN': 166.89,
      'FB': 208.09,
      'SYMC': 21.29
  }
  # 用股票价格大于100元的股票构造一个新的字典
  prices2 = {key: value for key, value in prices.items() if value > 100}
  print(prices2)