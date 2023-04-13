import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 1267315308 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  tab = np.array([[x_success, x_cnt - x_success], [y_success, y_cnt - y_success]])
  p_v = st.chi2_contingency(table, correction=False)[1]
  if (p_v < 0.02):
    return True
  else:
    return False
