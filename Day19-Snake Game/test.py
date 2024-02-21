with open('score.txt', mode='r') as s:
    score_list = s.read()
    
    
list = []
for i in score_list:
    if i != '\n':
        list.append(i)

print(list)