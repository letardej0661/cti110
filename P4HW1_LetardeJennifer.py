# CTI-110
# P4HW1 - Score List
# Jennifer Letarde
# 4/26/2023
#

num = int(input('How many scores do you want to enter? '))

print()

score_list = []
total = 0
count = 1

for count in range(num):
    score = int(input("Enter score #" + str(count + 1) + ": "))
    score_list.append(score)

    if score < 0:
        print("INVALID Score entered!!!")
        print("Score should be between 0 and 100")
        print(int(input("Enter score #" + str(count + 1) + " again: ")))
    
    total = score + total

print()

print("----------Results----------")
print(f'Lowest Score:   {min(score_list)}')
print(f'Modified List:  {score_list}')
average = sum(score_list) / 5
print(f'Scores Average:  {average}')
 
print("---------------------------")





