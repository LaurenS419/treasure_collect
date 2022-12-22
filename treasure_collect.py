# Treasure Collect


import random

mp = [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
player = 'O'
treasure = '*'

ran1 = random.randint(1, len(mp) * len(mp[0])-1)
ran2 = random.randint(1, len(mp) * len(mp[0])-1)
ran3 = random.randint(1, len(mp) * len(mp[0])-1)


while ran1 == ran2 or ran2 == ran3 or ran1 == ran3:
    if ran1 == ran2:
        if ran1 < len(mp) * len(mp[0])-2:
            ran1 += 1
        else:
            ran1 -= 1
    if ran2 == ran3:
        if ran2 < len(mp) * len(mp[0])-2:
            ran2 += 1
        else:
            ran2 -= 1
    if ran1 == ran3:
        if ran1 < len(mp) * len(mp[0])-2:
            ran1 += 1
        else:
            ran1 -= 1

t1_loc = (ran1//len(mp[0]), ran1 - 4*(ran1//len(mp[0])))
t2_loc = (ran2//len(mp[0]), ran2 - 4*(ran2//len(mp[0])))
t3_loc = (ran3//len(mp[0]), ran3 - 4*(ran3//len(mp[0])))

mp[t1_loc[0]][t1_loc[1]] = treasure
mp[t2_loc[0]][t2_loc[1]] = treasure
mp[t3_loc[0]][t3_loc[1]] = treasure
mp[0][0] = player

x_loc = 0
y_loc = 0
height = len(mp) - 1
width = len(mp[0]) - 1

for line in mp:
    print(line)
    
collection = 0

while collection < 3:
    
    collect = False
    inp = False
    while not inp:
        move = input("Your move: ")
        
        if move.lower() == 'up':
            move = 'up'
            inp = True
        elif move.lower() == 'down':
            move = 'down'
            inp = True
        elif move.lower() == 'left':
            move = 'left'
            inp = True
        elif move.lower() == 'right':
            move = 'right'
            inp = True
        else:
            print("Invalid move.")
    
    mp[y_loc][x_loc] = '.'
    
    if move== 'up':
        y_loc -= 1
        
        if y_loc < 0:
            y_loc = height
            
    elif move == 'down':
        y_loc += 1
        
        if y_loc > height:
            y_loc = 0
            
    elif move == 'left':
        x_loc -= 1
        
        if x_loc < 0:
            x_loc = width
            
    elif move== 'right':
        x_loc += 1
        
        if y_loc > width:
            x_loc = 0
    
    if (y_loc, x_loc) == t1_loc:
        collection += 1
        collect = True
    elif (y_loc, x_loc) == t2_loc:
        collection += 1
        collect = True
    elif (y_loc, x_loc) == t3_loc:
        collection += 1
        collect = True
    
    mp[y_loc][x_loc] = 'O'
    
    for line in mp:
        print(line)
        
    if collect:
        print("You collected a treasure!")
        
print("Congrats! You win.")
        


