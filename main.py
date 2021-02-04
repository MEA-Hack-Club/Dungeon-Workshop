import helpers;
import turtle;

f = open("level1.txt", "r")

def main():
  helpers.readWASD(f)
  helpers.drawMap()
  
  turtle.onkey(helpers.up, "w")
  turtle.onkey(helpers.left, "a")
  turtle.onkey(helpers.right, "d")
  turtle.onkey(helpers.down, "s")
  
  turtle.listen()
  turtle.mainloop()

main();