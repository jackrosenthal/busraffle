from secrets import SystemRandom

rng = SystemRandom()

item = input("What are you giving away? ")
n = int(input("How many {} are you giving away? ".format(item)))
temp = input("Do you want to enter names? (y/N) ")
print()
useNames = (temp == "yes" or temp == "y" or temp == "Yes" or temp == "Y")

names = {}

if useNames:
    for i in range(n):
        names[i] = input("Participant: ")
        print("You get one of the {}! For now.".format(item))
    print()
else:
    print("To start, participants 0 through {} get one of the {} (for now...)".format(n - 1, item))
    for i in range(n):
        names[i] = str(i)
    print()

bus =  list(range(n))

print("List anyone who was gone, end with a blank line...")
s = n
while True:
    line = input()
    if line == '':
        break
    index = -1
    for i, name in names.items():
        if line == name:
            index = i
            break
    if index == -1:
        continue

    if useNames:
        names[index] = input("New Participant: ")
    else:
        names[index] = str(s)
    s += 1
    print("New Participant {} gets one of the {} (for now) then.".format(names[index], item))

e = s
j = n
while True:
    if useNames:
        temp = input("Continue with participant (Y/n)? ")
        quit = temp == 'y' or temp == 'Y' or temp == "yes" or temp == "Yes" or temp == ''
        if not quit:
            break
    else:
        temp = input("Continue with participant {} (Y/n)? ".format(e))
        here = temp == 'y' or temp == 'Y' or temp == "yes" or temp == "Yes" or temp == ''
        if not here:
            temp = input("Quit entirely (y/N)? ")
            if temp == 'y' or temp == 'Y' or temp == "yes" or temp == "Yes":
                break
            e += 1
            continue

    e = e + 1
    if useNames:
        temp = input("Participant: ")
        names[j] = temp
    else:
        names[j] = e

    if rng.random() < (n / len(names)):
        i = rng.randrange(0, n)
        print("Participant {} steals one of the {} from participant {}!".format(names[j], item, names[bus[i]]))
        bus[i] = j
    else:
        print("Nothing happened.")
    j = j+1

print()
print("Winners are: ", end = '')
for i in range(n - 1):
    print(names[bus[i]], end = ', ')
if n > 1:
    print('and {}!'.format(names[bus[n-1]]))
else:
    print("{}!".format(names[bus[n-1]]))
