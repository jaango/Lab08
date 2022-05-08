# -*- coding: utf-8 -*-
"""
THis file contains the Ballon Flight game. IN the game you use the mouse to dodge obsticles.
When you hold down the mouse(right click) the ballon moves up, otherwise it moves down.
@author: Jake Angobaldo
"""


import pgzrun
from pgzero.builtins import Actor
from random import randint

WIDTH = 800
HEIGHT = 600


balloon = Actor("balloon")
balloon.pos = 400, 300

bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10, 200)

bird2 = Actor("bird-up")
bird2.pos = randint(800, 1600), randint(10, 200)

house = Actor("house")
house.pos = randint(800, 1600), 460

house2 = Actor("house")
house2.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

tree2 = Actor("tree")
tree2.pos = randint(800, 1600), 450 

bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0
scores = []

def update_high_scores():
    global score, scores
    filename = r"C:\Users\angob\Desktop\EE104\lab8_angobaldo_jake\high-scores.txt"
    scores = []
    
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        
 
        for high_score in high_scores:
            if(score > int(high_score)): 
                scores.append(str(score) + " ") 
                score = int(high_score)
            else:
                scores.append(str(high_score) + " ")
    with open(filename, "w") as file:
        for high_score in scores: 
            file.write(high_score)


def display_high_scores(): 
    screen.draw.text("HIGH SCORES", (350, 150), color="black") 
    y = 175 
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + ". " + high_score, (350, y), color="black") 
        y += 25 
        position += 1


def draw():
    screen.blit("background", (0, 0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        bird2.draw()
        house2.draw()
        tree2.draw()
        screen.draw.text("Score: " + str(score), (700, 5), color="black")
       
    
    else: 
        display_high_scores()
        

def on_mouse_down():
    global up
    up = True
    balloon.y -= 50
 
def on_mouse_up():
    global up
    up = False
    

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True
        

def update():
    global game_over, score, number_of_updates
    if not game_over:
        if not up:
            balloon.y += 1
        

        if bird.x > 0:
            bird.x -= 6
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1

        else:    
            bird.x = randint(800, 1600)  
            bird.y = randint(10, 200)        
            score += 1 
            number_of_updates = 0
            
        if bird2.x > 0:
            bird2.x -= 6
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1

        else:          
            bird2.x = randint(800, 1600) 
            bird2.y = randint(10, 200)        
            score += 1 
            number_of_updates = 0


        if house.right > 0:
            house.x -= 4 
        else:
            house.x = randint(800, 1600) 
            score += 1 
        
        if house2.right > 0:
            house2.x -= 4 
        else:
            house2.x = randint(800, 1600) 
            score += 1 
            
            

        if tree.right > 0:
            tree.x -= 4
        else:
            tree.x = randint(800, 1600)
            score += 1
            
 
        if tree2.right > 0:
            tree2.x -= 4
        else:
            tree2.x = randint(800, 1600)
            score += 1
            

        if balloon.top < 0 or balloon.bottom > 560:
            game_over = True
            update_high_scores()
            
            

        if balloon.collidepoint(bird.x, bird.y) or balloon.collidepoint(house.x, house.y) or balloon.collidepoint(tree.x, tree.y) or balloon.collidepoint(tree2.x, tree2.y):#This checks if the bird has hit any of the three obstacles.
            game_over = True
            update_high_scores()
            

        if tree.x == tree2.x:
            tree2.x = randint(800, 1000)
            
        if tree.x == house.x:
            house.x = randint(800, 1000)
            
        if tree2.x == tree.x:
            tree2.x = randint(800, 1000)
                    
pgzrun.go()