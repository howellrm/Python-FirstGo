#pypoll assignment week 3

#import dependencies 
import os
import pandas as pd
import numpy as np
import csv

# Establish the root path, data path and export output path
elec_1 = os.path.join("raw_data", "election_data_1.csv")
elec_2 = os.path.join("raw_data", "election_data_2.csv")

#print(elec_1)
#print(elec_2)

#Iterate through the listdir results
elec_df= []
for file in elec_1:
     if file.endswith(".csv"):
         elec_df.append(os.path.join(elec_1, file))

for file in elec_df:
    df = file
    df_pd = pd.read_csv(df)

    # Total votes cast
    total_votes = df_pd["Candidate"].count()
    #print(total_votes)


    # Make a dataframe of the candidates and the votes cast for each candidate
    can_votes = df_pd["Candidate"].value_counts()
    can_votes_df = pd.DataFrame(can_votes)
    can_votes_df.columns=["Votes"]
    #print(can_votes)


    # Make a list of the candidates and votes cast
    can_list = can_votes_df.index.tolist()
    vote_list = can_votes_df.iloc[:, 0].tolist()
    #print(vote_list)

    # Get the percentage of votes per candidate 
    per_votes = ((vote_list/total_votes)*100).round(1)
    per_list = list(map("{}%".format, per_votes))
    #print(per_list)

    # Make a dataframe of the voting results
    res_df = pd.DataFrame({
        "Candidate": can_list,
        "Number of Votes": vote_list,
        "Percentage of Votes": per_list
    })

    #Index by number of votes to pull the winner of the election
    winner_df = res_df.set_index("Number of Votes")
    winner_votes = max(vote_list)
    winner = winner_df.loc[winner_votes].Candidate

    print(
        f"Election Results for Election Data 1 - {elec_1}\n"
        f"-----------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------------------------\n" 
        f"{res_df.to_string(index=False)}\n"
        f"-----------------------------------------\n" 
        f"Winner: {winner}\n"
    ) 

# for file in elec_2:
#      if file.endswith(".csv"):
#          elec_df.append(os.path.join(elec_2, file))

# for file in elec_2:
#     df2 = elec_2
#     df_pd2 = pd.read_csv(df)

    # Total votes cast
#     total_votes2 = df_pd2["Candidate"].count()

#     # Make a dataframe of the candidates and the votes cast for each candidate
#     can_votes2 = df_pd2["Candidate"].value_counts()
#     can_votes_df2 = pd.DataFrame(can_votes2)
#     can_votes_df2.columns=["Votes"]

#     # Make a list of the candidates and votes cast
#     can_list2 = can_votes_df2.index.tolist()
#     vote_list2 = can_votes_df2.iloc[:, 0].tolist()

#     # Get the percentage of votes per candidate 
#     per_votes2 = ((vote_list2/total_votes2)*100).round(1)
#     per_list2 = list(map("{}%".format, per_votes2))

#     # Make a dataframe of the voting results
#     res_df2 = pd.DataFrame({
#         "Candidate": can_list2,
#         "Number of Votes": vote_list2,
#         "Percentage of Votes": per_list2
#     })

#     # Index by number of votes to pull the winner of the election
#     winner_df2 = res_df2.set_index("Number of Votes")
#     winner_votes2 = max(vote_list2)
#     winner2 = winner_df2.loc[winner_votes2].Candidate

    # print(
    #     f"Election Results for Election Data 2 - {elec_2}\n"
    #     f"-----------------------------------------\n"
    #     f"Total Votes: {total_votes2}\n"
    #     f"-----------------------------------------\n" 
    #     f"{res_df2.to_string(index=False)}\n"
    #     f"-----------------------------------------\n" 
    #     f"Winner: {winner2}\n"
    # )


#     # Grab the filename from the original path.
#     # The _, gets rid of the path. The , _ gets rid of the .csv.
#     # _, filename = os.path.split(file)
#     # filename, _ = filename.split(".csv")

#     # Print the analysis to the terminal.
    

    

# #     # Export a text file with the results.
# #     text_path = os.path.join(output_path, filename + ".txt")
# #     with open(text_path, "w") as text_file:
# #         text_file.write(
# #             f"Election Results - {filename}\n"
# #             f"-----------------------------------------\n"
#             f"Total Votes: {tot_votes}\n"
#             f"-----------------------------------------\n" 
#             f"{results_df.to_string(index=False)}\n"
#             f"-----------------------------------------\n" 
#             f"Winner: {winner}\n"
# #         )