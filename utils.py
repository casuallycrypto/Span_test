import sys
from collections import defaultdict

# Common function to read input from file or stdin
def read_input(source='file'):
    final_outcome = defaultdict(int)  # Use defaultdict for automatic handling of new teams
    if source == 'file':
        file_name = input("Enter the filename: ")
        try:
            with open(file_name, "r") as current_file:
                for line in current_file:
                    process_line(line, final_outcome)
        except FileNotFoundError:
            print("This file does not exist")
    elif source == 'stdin':
        for line in sys.stdin:
            process_line(line, final_outcome)
    
    display_ranking(final_outcome)

# Process a single line of input, splitting teams and calling sorting
def process_line(line, final_outcome):
    if line.strip():
        teams = [team.strip() for team in line.rstrip().split(',')]
        sorting(teams, final_outcome)

# Sorting logic for each pair of teams
def sorting(teams, final_outcome):
    team1, team2 = teams[0].split(), teams[1].split()
    team_names = [team1[0], team2[0]]
    team_scores = [int(team1[1]), int(team2[1])]
    
    decision(team_scores, team_names, final_outcome)

# Decision logic to update scores based on match outcome
def decision(team_scores, team_names, final_outcome):
    if team_scores[0] > team_scores[1]:
        final_outcome[team_names[0]] += 3
        final_outcome[team_names[1]] += 0
    elif team_scores[0] < team_scores[1]:
        final_outcome[team_names[1]] += 3
        final_outcome[team_names[0]] += 0
    else:  # Draw
        final_outcome[team_names[0]] += 1
        final_outcome[team_names[1]] += 1

# Display the rankings sorted by points and name
def display_ranking(final_outcome):
    for count, (team, points) in enumerate(sorted(final_outcome.items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{count}. {team}, {points} pts")

# Run the program based on file input or manual stdin input
if __name__ == '__main__':
    source = input("Enter 'file' for file input or 'stdin' for manual input: ").strip()
    read_input(source)
