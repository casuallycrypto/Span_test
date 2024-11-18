import sys 

#read_file function takes in a file name, reads it if it exists and then returns the required sorted output
def read_file():
    final_outcome = {}
    file_name = input()
    try:
        current_file = open(file_name, "r")
        for line in current_file:
            if line == "" or line == "\n":
                break
            else:
                teams = []
                line = line.rstrip()
                line_split = line.split(',')
                for i in line_split:
                    teams.append(i)
            sorting(teams, final_outcome)
        display_ranking(final_outcome)
    except FileNotFoundError:
        print("This file does not exist")

#read_text takes in manually text, sorts it line by line and then returns a the completed ranking table
def read_text():
    final_outcome = {}
    for line in sys.stdin:
        if line == "" or line == "\n":
            break
        else:
            teams = []
            line = line.rstrip()
            line_split = line.split(',')
            for i in line_split:
                teams.append(i)
            sorting(teams, final_outcome)
    display_ranking(final_outcome)

#display_ranking sorts the results by points, and alphabetically in the case where two teams have a draw
def display_ranking(final_outcome):
    count = 1
    for k,v in sorted(final_outcome.items(),key=lambda x:(-x[1],x[0])):
        print("{}. {}, {} pts".format(count,k,v))
        count+=1

def sorting(teams, final_outcome):
    team_scores = []
    team_names = []
    for team in teams:
        if team.split(" ")[0] == "":
            team = team.lstrip()
        else:
            team = team
        team_name = team.split(" ")[0]
        team_names.append(team_name)
        team_points = int(team.split(" ")[1])
        team_scores.append(team_points)
    return decision(team_scores, team_names, final_outcome)

#decision takes the outcomes and appends the score W=3, D=1, L=0
def decision(team_scores,team_names, final_outcome):
    if len(team_scores) == 1:
        return 
    if team_scores[0] > team_scores[1]:
        if team_names[0] in final_outcome.keys():
            final_outcome[team_names[0]] = final_outcome.get(team_names[0]) + 3
        else:
            final_outcome[team_names[0]] = 3
        if team_names[1] in final_outcome.keys():
            final_outcome[team_names[1]] = final_outcome.get(team_names[1]) + 0
        else:
            final_outcome[team_names[1]] = 0
    if team_scores[0] < team_scores[1]:
        if team_names[1] in final_outcome.keys():
            final_outcome[team_names[1]] = final_outcome.get(team_names[1]) + 3
        else:
            final_outcome[team_names[1]] = 3 
        if team_names[0] in final_outcome.keys():
            final_outcome[team_names[0]] = final_outcome.get(team_names[0]) + 0
        else:
            final_outcome[team_names[0]] = 0
    if team_scores[0] == team_scores[1]:
         if team_names[0] in final_outcome.keys():
            final_outcome[team_names[0]] = final_outcome.get(team_names[0]) + 1
         else:
             final_outcome[team_names[0]] = 1
        
         if team_names[1] in final_outcome.keys():
             final_outcome[team_names[1]] = final_outcome.get(team_names[1]) + 1
         else:
             final_outcome[team_names[1]] = 1
       
    return final_outcome
        