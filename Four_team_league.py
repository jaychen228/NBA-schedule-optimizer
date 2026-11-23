import random as r

teams = ['A','B','C','D']

def generate_schedule(teams):
    all_matchups = []
    for i in teams:
        for j in teams:
            if i != j:
                all_matchups.append((i,j))

    print(f"There are a total of {len(all_matchups)} mathcups\n")





generate_schedule(teams)