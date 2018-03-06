#pypoll assignment week 3

#import dependencies 
import os
from pandas import pandas
import numpy as np
import csv

# Establish the root path, data path and export output path
elec_1 = os.path.join("raw_data", "election_data_1.csv")
elec_2 = os.path.join("raw_data", "election_data_2.csv")

print(elec_1)
print(elec_2)

#Iterate through the listdir results
elec_df= []
for file in elec_1:
     if file.endswith(".csv"):
         elec_df.append(os.path.join(elec_1, file))

#print(elec_df)

for file in elec_df:
    df = file
    df_pd = pandas.read_csv(df)
    #print(df_pd)

    # Total votes cast
    total_votes = df_pd["Candidate"].count()
    print(total_votes)