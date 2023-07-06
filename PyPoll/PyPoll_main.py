# Import packages
import os
import csv

# Create and store filepath
election_csv = os.path.join("","Resources","election_data.csv")

# Col names as empty lists, no pandas
ballot = []
county = []
candidate = []

# Open and read csv, with open
with open(election_csv) as election_csv_file:
    election_read = csv.reader(election_csv_file, delimiter = ",")
    # create a version without headers so the frequency check doesn't count the header
    header = next(election_read)
    # after head skip loop through remaining rows
    headless_election = [row for row in election_read]
    # append column heads to row[num]
    for row in headless_election:
        # append ballot list, 0
        ballot.append(row[0])
        # append county list, 1
        county.append(row[1])
        # append candidate list, 2
        candidate.append(row[2])
        
observations = 0 
for number in ballot:
    observations += 1

# we want a dictionary of lists, key values will be unique names from headless_elections
unique_dict = {}
for name in candidate:
    # if a name is already present in unique dictionary, frequency of name + 1
    if name in unique_dict:
        unique_dict[name] += 1
    # otherwise name is added to unique dictionary, with frequency start = 1
    else:
        unique_dict[name] = 1

# id for unique dictionary keys, list iteration limit by length
unique_key = list(unique_dict.keys())
# id for unique dictionary frequency adjunct
unique_frequency = list(unique_dict.values())
# id total sum of unique values for percentage calculation
sum_unique_frequency = sum(unique_frequency)

# id candidate with highest votes
highest_freq = max(unique_frequency)
# match highest number of votes to the candidate name in dictionary
highest_name = [name for name, count in unique_dict.items() if count == highest_freq]

# the end is nigh
print(f"Election Results")
print(f"-"*45)
print(f"Total Votes: ", observations)
print(f"-"*45)
# no function, so loop goes here
# print iteration for length in unique dictionary 
for i in range(len(unique_frequency)):
    # iteration var setup, candidate name, candidate vote frequency, percentage calc
    key_names = unique_key[i]
    frequency_names = unique_frequency[i]
    # need to add rounding; it's literally round, rounding % to 2 places
    percent_calc = round((frequency_names/sum_unique_frequency)*100,2)
    print(f"Candidate:", key_names, ":", percent_calc,"%", "(", frequency_names,")")

print(f"-"*45)
print(f"Election Winner: ", str(highest_name))