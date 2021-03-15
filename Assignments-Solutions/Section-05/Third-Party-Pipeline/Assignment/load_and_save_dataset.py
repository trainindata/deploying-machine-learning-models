import re
import pandas as pd
import numpy as np



def get_first_cabin(row):
    try:
        return row.split()[0]
    except:
        return np.nan
    


def get_title(passenger):
    line = passenger
    if re.search('Mrs', line):
        return 'Mrs'
    elif re.search('Mr', line):
        return 'Mr'
    elif re.search('Miss', line):
        return 'Miss'
    elif re.search('Master', line):
        return 'Master'
    else:
        return 'Other'


data = pd.read_csv('https://www.openml.org/data/get_csv/16826755/phpMYEkMl')

data = data.replace('?', np.nan)

data['cabin'] = data['cabin'].apply(get_first_cabin)
 
data['title'] = data['name'].apply(get_title)

data['fare'] = data['fare'].astype('float')
data['age'] = data['age'].astype('float')

data.drop(labels=['name','ticket', 'boat', 'body','home.dest'], axis=1, inplace=True)

data.to_csv('titanic.csv', index=False)