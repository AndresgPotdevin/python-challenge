import os
import csv
total_votes = 0
candidates_list = []
vote_counts = []

election_data_csv = os.path.join("election_data.csv")
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)

    for line in csvreader:

        total_votes = total_votes + 1

        candidate = line[2]

        if candidate in candidates_list:
            candidate_index = candidates_list.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:
            candidates_list.append(candidate)
            vote_counts.append(1)

    percentage = []
    max_votes = vote_counts[0]
    max_index = 0

    for count in range(len(candidates_list)):
        vote_percentage = vote_counts[count]/total_votes*100
        percentage.append(vote_percentage)

        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count

    winner = candidates_list[max_index]

print('Election Results')
print('--------------------------')
print(f"Total Votes: {total_votes}")
for count in range(len(candidates_list)):
    print(f"{candidates_list[count]}: {percentage[count]}% ({vote_counts[count]})")
print('--------------------------')
print(f"Winner: {winner}")
print('--------------------------')

write_file = f"PyPoll.txt"
filewriter = open(write_file, mode = 'w')
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {total_votes}\n")
for count in range(len(candidates_list)):
    filewriter.write(f"{candidates_list[count]}: {percentage[count]}% ({vote_counts[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")
filewriter.close()
