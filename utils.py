import sys 
import fileinput 
from pathlib import Path

def read_file():
    final = {}
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

def display_ranking(final):
    count = 1
    for k,v in sorted(final.items(),key=lambda x:(-x[1],x[0])):
        print("{}. {}, {} pts".format(count,k,v))
        count+=1

def sorting(teams, final):
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
    return decision(scores, names, final)

def decision(scores,names, final):
    if len(scores) == 1:
        return 
    if scores[0] > scores[1]:
        if names[0] in final.keys():
            final[names[0]] = final.get(names[0]) + 3
        else:
            final[names[0]] = 3
        if names[1] in final.keys():
            final[names[1]] = final.get(names[1]) + 0
        else:
            final[names[1]] = 0
    if scores[0] < scores[1]:
        if names[1] in final.keys():
            final[names[1]] = final.get(names[1]) + 3
        else:
            final[names[1]] = 3 
        if names[0] in final.keys():
            final[names[0]] = final.get(names[0]) + 0
        else:
            final[names[0]] = 0
    if scores[0] == scores[1]:
         if names[0] in final.keys():
            final[names[0]] = final.get(names[0]) + 1
         else:
             final[names[0]] = 1
        
         if names[1] in final.keys():
             final[names[1]] = final.get(names[1]) + 1
         else:
             final[names[1]] = 1
       
    return display_ranking(final)
        