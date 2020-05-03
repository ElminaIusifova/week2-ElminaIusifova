
# Snail has to climb to the tree with h meters high.
# It goes up 5 m every daylight but goes down 2 m every night.
# How long it will take for snail to reach the top.
# Lets accept h as 100 meters.
# But it is a variable and can be modified by user

height = 100
up = 5
down = 2
day = 0
moving=0


while moving < height:
      moving=moving+up-down
      day += 1
      if height - moving < 5:
          break
day=day+1
print("The snail needs", day, "days.")






