repValues = [5,8,10,15,20]
sets = [3,4,5,10, 15,21]
# for x in y loop
# for rep in reps
# for set in sets 
# for rep in repValues:
#     for set in sets:
#         print(f"I normally complete {rep} for a total of {set} sets.")
# statement = f"I normally complete {repValues} for a total of {sets[1]} sets."
# print("This is so fvking cool")
for set in sets:
    for rep in repValues:
     if set == rep:
        print(f"i usually do a {set} by {rep}")