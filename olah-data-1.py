import pandas as pd

# membuat DataFrame dari Dictionary
data = {
    'Name': ['John', 'Jane', 'Bob', 'Emma'],
    'Age': [23, 31, 20, 27],
    'Work':['Teacher', 'Designer', 'Doctor', 'Lecturer']
}

df = pd.DataFrame(data)
print(df) # nampilin datanya jadi kek table tanpa border