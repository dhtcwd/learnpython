ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')#[Apples,Oranges,Crows,Telephone,Light,Sugar]
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)#[Apples,Oranges,Crows,Telephone,Light,Sugar,"Boy", "Girl", "Banana", "Corn"]
    print "There's %d items now." % len(stuff)#10

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]#'Orange'
print stuff[-1] # Corn
print stuff.pop()# Corn

print ' '.join(stuff) # Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
print stuff
print stuff[3:7]
#print '#'.join(stuff[3:6]) # Telephone#Light