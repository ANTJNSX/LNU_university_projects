
# drumken saimlor :3

import random

# define a plane

# loop over choices
# check if place is off grid
    # add 1 to dead 
    # continue loop to next sailor/index
# else keep looping
# if its taken enough steps, continue loop

plank_size = int(input("Enter size: "))
steps = int(input("Enter the number of steps: "))
sailors = int(input("Enter the number of sailors: "))

dead_sailors=0

x_min, x_max, y_min, y_max = -plank_size, plank_size, -plank_size, plank_size

for i in range(sailors):
    
    x, y = 0, 0

    for j in range(0, steps):
        step_dir = random.choice(['up','down','left','right'])

        match step_dir:
            case 'up':
                y+=1 
        
            case 'down':
                y-=1

            case 'left':
                x-=1

            case 'right':
                x+=1
         
        if x < x_min or x > x_max or y < y_min or y > y_max: 
            dead_sailors+=1
            break

    # print(y,x)

print(f"Out of {sailors} drunk sailors, {dead_sailors} ({round((dead_sailors/sailors)*100, 2)}%) fell into the water.")
