import random

#point system
set_point_to_win = int(input("What is the points needed to win? \n"))
player_point = 0
robot_point = 0

#actual game mechanics
game = ['stone','paper','scissors']
while True: 
    print(f"player point: {player_point} | robot point: {robot_point}")
    
    if player_point == set_point_to_win:
        print("")
        print(f'player won by {player_point - robot_point}')
        break
    elif robot_point == set_point_to_win:
        print("")
        print(f'robot won by {robot_point - player_point}')
        break
    else:
        pass
    
    print("stone, paper, scissors \n")
    robot = random.choice(game)
    player = input("Player: ")
    print("Robot: ",robot, '\n')
    if robot == player:
        print("it's a draw \n")
        continue
    elif (robot == "stone" and player == "paper") or (robot == "scissors" and player == "stone") or (robot == "paper" and player == "scissors"):
        player_point += 1
        pass
        
    elif (player == "stone" and robot == "paper") or (player == "scissors" and robot == "stone") or (player == "paper" and robot == "scissors"):
        robot_point += 1
        pass
    else:
        print("error try again")
        pass
