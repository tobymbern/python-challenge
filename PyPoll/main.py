import csv
from collections import defaultdict

with open('election_data_1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip header row
    election_1 = list(reader)

with open('election_data_2.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip header row
    election_2 = list(reader)


def collect_names(election_data):

    names = {election_data[0][2] : 1} #initiate first candidate and their vote
    for each in election_data:
        exist_count = 0 # helps us run through all the existing dictionary keys and see if we should increment a name
        # or add the current name as a next name in the dictionary
        for key, value in names.items():
            if each[2] == key:
                names[each[2]] += 1
            else:
                exist_count += 1
        if exist_count == len(names): # this adds a new candidate to our dictionary if we haven't seen them before
            names[each[2]] = 1

    return names


def print_results(total_votes, candidate_dict):

    print('')
    print('')
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")

    count = 0

    for key, value in candidate_dict.items():
        print(key + ": " + str(round(value/total_votes*100,1)) + "% (" + str(value) + ")") #rounding is slightly
        # inaccurate, but much prettier

        if count == 0:
            winner = key
            count += 1

        if value > candidate_dict[winner]:
            winner = key

    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")

    return True

num_votes = len(election_1)
candidate_dict_1 = collect_names(election_1)
print_results(num_votes, candidate_dict_1)

num_votes_2 = len(election_2)
candidate_dict_2 = collect_names(election_2)
print_results(num_votes_2, candidate_dict_2)







