print("One minute you were in bed, before being pulled into a dream... or so you thought. You can only explore hopefully finding a safe pathway and perhaps treasure.")
print("You look around and only see a lake in front of you.")
lake = input("Do you want to swim or wait for a boat?")
if lake == "swim":
    print("You starting swimming across the lake, and before you know it a shark has crept up behind you, chomping you whole.")
    quit()
elif lake == "wait":
    print("A boat slowly reaches over to you, in which you climb in and get pushed by the lake to the other side.")

cave = input("The other side has a cave that's mysterious do you venture inside, or walk onto the steep pathway that is close to the edge?")
if cave == "walk":
    print("You're squished by oncoming boulders that were too fast to outrun, squishing you to a pulp.")
    quit()
elif cave == "venture":
    print("You walk inside and you find out that there's light deep inside.")

tunnels = input("You come across three tunnels within the cave. You can either go into the left, right or centre tunnel. You cannot walk back.")
if tunnels == "left":
    print("You walk for endless time and you collapse due to not eating or drinking. You wake up in bed exhausted by the adventure, but no time has passed since you fell asleep.")
    quit()
elif tunnels == "centre":
    print("You walk for awhile and suddenly you hear multiple growls, you want to return but when you look behind, it's sealed up. You look forwards again and see creatures you've never seen before. You struggle against their grasp before finally getting eaten by the group of mysterious animals.")
    quit()
elif tunnels == "right":
    print("Right before you were going to give up you see light up ahead, using a burst of energy you run forward finding mountains of treasure. You're shocked to find it, and before you could celebrate your victory you wake up.")