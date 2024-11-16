import sys 
import fileinput 
from pathlib import Path

def read_file():
    #target_dir = Path(input())
    #if not target_dir.exists():
       #print("The directory does not exist")
    final = {}
    file_name = input()
    f = open("test.txt", "r")
    for line in f:
        if line == "" or line == "\n":
            break
        else:
            teams = []
            line = line.rstrip()
            line_split = line.split(',')
            for i in line_split:
                teams.append(i)
                sorting(teams, final)
    print(final)


def read_text():
     #sys.stdin reads the escape char vs input()
    final = {}
    for line in sys.stdin:
        if line == "" or line == "\n":
            break
        else:
            teams = []
            line = line.rstrip()
            line_split = line.split(',')
            for i in line_split:
                teams.append(i)
                sorting(teams, final)

def sort_ranking(final):
    return

def sorting(teams, final):
    scores = []
    names = []
    #only works for one line
    for team in teams:
        if team.split(" ")[0] == "":
            team = team.lstrip()
        else:
            team = team
        team_name = team.split(" ")[0]
        names.append(team_name)
        team_points = int(team.split(" ")[1])
        scores.append(team_points)
    print(scores)
    return decision(scores, names, final)

def decision(scores,names, final):
    if len(scores) == 1:
        return 
    if scores[0] > scores[1]:
        if names[0] in final.keys():
            final[names[0]] = final.get(names[0]) + 3
        if names[1] in final.keys():
            final[names[1]] = final.get(names[1]) + 0
        else:
            final[names[0]] = 3
            final[names[1]] = 0
    if scores[0] < scores[1]:
        if names[1] in final.keys():
            final[names[1]] = final.get(names[1]) + 3 
        if names[0] in final.keys():
            final[names[0]] = final.get(names[0]) + 0
        else:
            final[names[1]] = 3
            final[names[0]] = 0
    if scores[0] == scores[1]:
         print("reached")
         if names[0] in final.keys():
            final[names[0]] = final.get(names[0]) + 1
         else:
             final[names[0]] = 1
        
         if names[1] in final.keys():
             final[names[1]] = final.get(names[1]) + 1
         else:
             final[names[1]] = 1
       
    print(final)
    return final


        