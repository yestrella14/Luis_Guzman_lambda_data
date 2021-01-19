"""Lambdata - collection of Data Science helper funcitons"""

# accessing libraries through pipenv
import pandas as pd
import numpy as np

def null_count(df):
  count = df.isnull().sum().sum()
  return int(count)

def abbr_2_st(state_series, abbr_2_st=True):
  abbreviation = {
    'Alabama': 'AL',
    'AL': 'Alabama',
    'Arizona': 'AZ',
    'AZ': 'Arizona',
    'California': 'CA',
    'CA': 'California',
    'Delaware': 'DE',
    'DE': 'Delaware',
    'Ohio': 'OH',
    'OH': 'Ohio'
  }

  for state in state_series:
    abb =print(abbreviation[state])
  return abb
