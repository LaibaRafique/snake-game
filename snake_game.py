#importing modules
import turtle
import time
import random

#game delay
delay=0.1

#score when we start the game
score=0
high_score=0

#setup the screen
wn=turtle.Screen()
wn.title("Snake Game by Laiba") #title of windows
wn.bgcolor("green") #bg color
wn.setup(width=600, height=600) #size pf screen
wn.tracer(0) #turns off animations on the screen/screen updates (to let the module go as fast as possible)

#Border
border = turtle.Turtle()
border.speed(0)
border.color("white")      
border.pensize(3)          
border.penup()
border.goto(-300, -300)
border.pendown()
for _ in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()

#snake head
head= turtle.Turtle() #this will create the turtle 
head.speed(0) #animation speed of turtle module (0 is the fastest animation speed)
head.shape("square") #shape of head (circle,arrow,turtle,triangle,classic)
head.color("black") #color of head
head.penup() #turtle draw lines(penup() so it does not draw lines with the head is moving)
head.goto(0,0) #head's position center of screen (xcor=0,ycor=0), in turtle things always start from center
head.direction="stop" #dicrection of head when program starts will be stop (resting in middle)

#Snake food
food= turtle.Turtle() #this will create the turtle 
food.speed(0) #animation speed of turtle module (0 is the fastest animation speed)
food.shape("circle") #shape of food
food.color("red") # color of food
food.penup() #turtle draw lines(penup() so it does not draw lines with the head is moving)
food.goto(0,100) #food's position is a little above the head (xcor=0,ycor=100)

#snake body will be stored in a list
segments=[]

#pen
pen=turtle.Turtle() #creating turtle object called pen 
pen.speed(0) #animation speed
pen.shape("square") #shape(which we will not be able to see so does'nt matter)
pen.color("white") #color of text
pen.penup() #to let the turtle not draw lines
pen.hideturtle() #to make the turtle invisible that's why shape did'nt matter
pen.goto(0,260) #so the text can be on top of game screen because ycor=260
pen.write("Score:0  High Score:0", align="center",font=("Courier",24,"normal")) #write() to put text on the screen

#functions
def go_up(): #changing direction of head
#if conditions are to prevent the snake from going into its own body (from reversing directions)
    if head.direction != "down": 
        head.direction="up"
    
def go_down():
    if head.direction != "up":
        head.direction="down"

def go_left():
    if head.direction != "right":
        head.direction="left"

def go_right():
    if head.direction != "left":
        head.direction="right"

def move(): #for movement of head
#if condition is for checking if the head is going in that direction or not
    if head.direction =="up":
        y=head.ycor() #calling ycor 
        head.sety(y + 20) #setting new value of ycor, before the ycor was set to 0 in head.goto()
    #each of basic turtle's shapes is 20 pixels width by 20 pixels tall.
    if head.direction =="down":
        y=head.ycor()  
        head.sety(y - 20) 
    
    if head.direction =="left":
        x=head.xcor() #calling xcor 
        head.setx(x - 20) #setting new value of xcor, before the xcor was set to 0 in head.goto()
    
    if head.direction =="right":
        x=head.xcor()
        head.setx(x + 20)
    
#keyboard bindings (connects keypress with particular function)
wn.listen() #windows to listen for clicks/keypresses
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#main game loop
while True: #repeats over and over and over again
    wn.update() #everytime through the while loop it will update the screen
    
    #check for the collision with the border
    #if the head goes off the screen up,down,left,right (screen was 600x600 so 290 is used)
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290: 
        time.sleep(1) #pause the game of 1 second
        head.goto(0,0) #send the head back to the center of screen
        head.direction="stop" #head's direction is stop until the user decides to move it
        
        #hide the segments
        for segment in segments: #goes through list of segments(snake body)
            segment.goto(1000,1000) #moving the segment off the game screen(because we cant delete segments from memory)
            
        #clear the segments list (because the segment that went off the game screen will jump back when the game restarts) 
        segments.clear() #so we need to clear the list
        
        #reset the score
        score=0
        
        #reset the delay (so the previously shorten delay is reset to this)
        delay=0.1
        
        #update the score display
        pen.clear() #to clear the previously written text
        pen.write("Score: {}  High Score:  {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
        #displaying current score using format()
        
    #check for a collision with the food
    if head.distance(food) < 20: #built-in func to measure the distance between 2 turtles
    #each of basic turtle's shapes is 20 pixels width by 20 pixels tall, less than 20 means they collided
        #move food to random position
        x=random.randint(-290,290) #screen was 600x600 (290 is used so it does'nt go off the screen)
        y=random.randint(-290,290) 
        food.goto(x,y)
        
        #add a segment
        new_segment=turtle.Turtle() #new turtle object for snake body
        new_segment.speed(0) #animation speed
        new_segment.shape("square") #body shape
        new_segment.color("pink") #body color
        new_segment.penup() #so the turtle does'nt draw lines with the body moves
        segments.append(new_segment) #to add new segment to the list called segments(snake body)
        
        #shorten the delay (as the snakes get longer the game speeds up)
        delay-=0.001
        
        #Increase score
        score +=10 #adds 10 to the current score
        if score > high_score: #changing value of high score if score is greater than high score
            high_score = score 
        pen.clear() #to clear the previously written text
        pen.write("Score: {}  High Score:  {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
        #displaying current score using format()
    
    #move the end segments first in the reverse order (if there are more than 1 segments than this works)
    for index in range(len(segments)-1,0,-1): #to get index of list len(segments)-1,0 means till 1 ,-1 to get the 0 index)
        x=segments[index-1].xcor() #segments list members are new_segments which are turtle objects and has xcor & ycor.
        y=segments[index-1].ycor()
        segments[index].goto(x,y) #(descending order,e.g 9th segment will be connected with 8th segment, 8th with 7th & so on)
        
    #move segments[0] to where the head is (for segment 1 because this will be connected with the head)
    if len(segments)>0: #is there a segment 0
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y) #segment 1 to move where the head is
    
    move() #calling func for movement of head
    
    #check the head collision with the body segments
    for segment in segments: #goes through each segment
        if segment.distance(head)<20: #less than 20 means they are overlapping
            #each of basic turtle's shapes is 20 pixels width by 20 pixels tall, less than 20 means they collided
            time.sleep(1) #pause the game for 1 second
            head.goto(0,0) #send the head back to the center of screen
            head.direction="stop" #head's direction is stop until the user decides to move it
    
            #hide the segments
            for segment in segments: #goes through list of segments(snake body)
                segment.goto(1000,1000) #moving the segment off the game screen(because we cant delete segments from memory)
            
            #clear the segments list (because the segment that went off the game screen will jump back when the game restarts)
            segments.clear() #so we need to clear the list
            
            #reset the score
            score=0
            
            #reset the delay (so the previously shorten delay is reset to this)
            delay=0.1
        
            #update the score display
            pen.clear() #to clear the previously written text
            pen.write("Score: {}  High Score:  {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
            #displaying current score using format()
    
    time.sleep(delay) #stops the program for 0.1 seconds(so we can see the head's movement), delay=0.1 in starting of program

wn.mainloop() #this will keep the windows open for us!