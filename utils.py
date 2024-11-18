import sys 

#read_file function takes in a file name, reads it if it exists and then returns the required sorted output
def read_file():
    final_outcome = {}
    file_name = input()
    try:
        file = open(file_name, "r")
        for line in file:
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
    scores = []
    names = []
    for team in teams:
        if team.split(" ")[0] == "":
            team = team.lstrip()
        else:
            team = team
        team_name = team.split(" ")[0]
        names.append(team_name)
        team_points = int(team.split(" ")[1])
        scores.append(team_points)
    return decision(scores, names, final_outcome)

#decision takes the outcomes and appends the score W=3, D=1, L=0
def decision(scores,names, final_outcome):
    if len(scores) == 1:
        return 
    if scores[0] > scores[1]:
        if names[0] in final_outcome.keys():
            final_outcome[names[0]] = final_outcome.get(names[0]) + 3
        else:
            final_outcome[names[0]] = 3
        if names[1] in final_outcome.keys():
            final_outcome[names[1]] = final_outcome.get(names[1]) + 0
        else:
            final_outcome[names[1]] = 0
    if scores[0] < scores[1]:
        if names[1] in final_outcome.keys():
            final_outcome[names[1]] = final_outcome.get(names[1]) + 3
        else:
            final_outcome[names[1]] = 3 
        if names[0] in final_outcome.keys():
            final_outcome[names[0]] = final_outcome.get(names[0]) + 0
        else:
            final_outcome[names[0]] = 0
    if scores[0] == scores[1]:
         if names[0] in final_outcome.keys():
            final_outcome[names[0]] = final_outcome.get(names[0]) + 1
         else:
             final_outcome[names[0]] = 1
        
         if names[1] in final_outcome.keys():
             final_outcome[names[1]] = final_outcome.get(names[1]) + 1
         else:
             final_outcome[names[1]] = 1
       
    return final_outcome
        