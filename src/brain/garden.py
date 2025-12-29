import turtle
import time
import random

def pulse_screen():
    # Setup Screen
    screen = turtle.Screen()
    screen.title("Nucleus Digital Garden")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    
    # Setup Turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0) # Fastest
    t.left(90)
    t.width(2)
    
    # Colors
    colors = ['#ff0055', '#00ffaa', '#00ccff', '#ffee00', '#ff00ff']
    
    def draw_tree(branch_len, pen_size):
        if branch_len < 5:
            return
            
        # Color based on length/depth
        if branch_len < 20:
            t.color(random.choice(colors))
        else:
            t.color("white")
            
        t.pensize(pen_size)
        t.forward(branch_len)
        
        # Angles
        angle = random.randint(20, 30)
        shrink = random.uniform(0.7, 0.8)
        
        t.left(angle)
        draw_tree(branch_len * shrink, pen_size * 0.7)
        t.right(angle * 2)
        draw_tree(branch_len * shrink, pen_size * 0.7)
        t.left(angle)
        
        t.penup()
        t.backward(branch_len)
        t.pendown()

    print("[GARDENER BRAIN] Planting seeds...")
    
    # Start position
    t.penup()
    t.goto(0, -250)
    t.pendown()
    
    # Grow
    print("[GARDENER BRAIN] Growing Fractal...")
    draw_tree(100, 10)
    
    print("[GARDENER BRAIN] Transformation Complete.")
    print("[GARDENER BRAIN] Keeping window open for 10 seconds...")
    time.sleep(10)

if __name__ == "__main__":
    try:
        pulse_screen()
    except turtle.Terminator:
        print("Window closed.")
