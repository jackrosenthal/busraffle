from secrets import SystemRandom

rng = SystemRandom()

item = input("What are you giving away? ")
n = int(input("How many {} are you giving away? ".format(item)))
participants = int(input("How many people are participating? "))

print("To start, participants 0 through {} get one of the {} (for now...)".format(n - 1, item))
bus = list(range(n))
print()
print("List anyone who was gone, end with a blank line...")
s = n
while True:
    line = input()
    if line == '':
        break
    print("Participant {} gets one of the {} (for now) then.".format(s, item))
    bus[bus.index(int(line))] = s
    s += 1

j = n
for e in range(s, participants):
    here = input("Is participant {} here (y/n)? ".format(e)) == 'y'
    if not here:
        continue
    j = j + 1
    if rng.random() < n / j:
        i = rng.randrange(0, n)
        print("Participant {} steals one of the {} from participant {}!".format(e, item, bus[i]))
        bus[i] = e
    else:
        print("Nothing happened.")

