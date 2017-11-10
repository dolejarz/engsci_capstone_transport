import pandas as pd
import matplotlib.pyplot as plt

df_subway = pd.read_csv('/Users/dolejarz/Documents/Engineering Science/4th Year/CIV455/github/engsci_capstone_transport/gis/subway_buffer/trips_in_buffer.csv')

df_all = pd.read_csv('/Users/dolejarz/Documents/Engineering Science/4th Year/CIV455/github/engsci_capstone_transport/csv/Trips_Oct_31_2017.csv')

df_subway['tx'] = pd.to_datetime(df_subway['Date'])
df_all['tx'] = pd.to_datetime(df_all['Date'])

df_subway['start_hour'] = df_subway['tx'].dt.hour
df_all['start_hour'] = df_all['tx'].dt.hour

pt_subway = pd.pivot_table(df_subway,index='start_hour',aggfunc='count')
pt_all = pd.pivot_table(df_all,index='start_hour',aggfunc='count')

#series of hourly distribution of trips as a percent of daily total
subway_percent = pt_subway['tx']/float(pt_subway['tx'].sum())
all_percent = pt_all['tx']/float(pt_all['tx'].sum())

plt.figure(figsize=(12,8), dpi=300)
plt.plot(range(24), subway_percent)
plt.plot(range(24), all_percent,color='r')
plt.savefig('subway_vs_all.png')
