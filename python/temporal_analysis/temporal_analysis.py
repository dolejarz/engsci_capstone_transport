import pandas as pd
import matplotlib.pyplot as plt
#plt.style.use('seaborn')

df_sun_raw = pd.read_csv('/Users/dolejarz/Documents/Engineering Science/4th Year/CIV455/github/engsci_capstone_transport/csv/Trips_Oct_15_2017.csv')

df_tue_raw = pd.read_csv('/Users/dolejarz/Documents/Engineering Science/4th Year/CIV455/github/engsci_capstone_transport/csv/Trips_Oct_17_2017.csv')

def create_trip_time_col(df):
    df['trip_start'] = pd.to_datetime(df['t2'])
    df['trip_end'] = pd.to_datetime(df['Date1'])
    df['trip_start_hour'] = df['trip_start'].dt.hour
    df['trip_time_minutes'] = (df['trip_end']-df['trip_start']).dt.seconds/60.
    return df

df_sun = create_trip_time_col(df_sun_raw)
df_tue = create_trip_time_col(df_tue_raw)

# Getting a bit clever w pivot tables in order to use plt.bar() bc pd.series.hist() sucks
pt_sun = pd.pivot_table(df_sun,index='trip_start_hour',aggfunc='count')['trip_start']
pt_tue = pd.pivot_table(df_tue,index='trip_start_hour',aggfunc='count')['trip_start']

plt.figure(figsize=(12,8))
plt.bar(pt_tue.index-0.4,pt_tue,color='#094c82')
plt.xticks(range(24))
plt.xlim([-0.5,24])
plt.savefig('tues_hist.png')

plt.figure(figsize=(12,8))
plt.bar(pt_sun.index-0.4,pt_sun,color='#094c82')
plt.xticks(range(19))
plt.xlim([-0.5,19])
plt.savefig('sun_hist.png')


    