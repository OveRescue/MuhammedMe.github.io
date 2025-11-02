import turtle
import time
import random 
delay = 0.1

# score
score = 0
high_score = 0


# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("Green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("black")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# Snake food
snake_food = turtle.Turtle()
snake_food.speed(0)
snake_food.shape("square")
snake_food.color("red")
snake_food.penup()
snake_food.goto(0, 100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to control the snake
def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"
        
    
def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# main game loop
while True:
    wn.update()
    
    # Check for a collision with the food
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"
        
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()
        
        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    move()
    
        # Check for head collision with the body segments
    for segment in segments:
        if snake_head.distance(segment) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            # Clear the segments list
            segments.clear()
        
    time.sleep(delay)
    if snake_head.distance(snake_food) < 20: # Collision with the food
        x = random.randint(-290, 290) # New random position
        y = random.randint(-290, 290)
        snake_food.goto(x, y) # Move the food to new position
    
        new_segment = turtle.Turtle() # Add a segment
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        

   # Shorten the delay
        delay -= 0.001
   
   # Reset the delay
        if delay < 0.08:
            delay = 0.08
    
    # Increase the score
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)
wn.mainloop()