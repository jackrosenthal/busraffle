from secrets import SystemRandom


def main():
    # Initialize random number generator.
    rng = SystemRandom()
    
    # Query user on raffle information
    item = input("What are you giving away? ")
    n = int(input("How many {} are you giving away? ".format(item)))
    useNames = yes_no_check(input("Do you want to enter names? (y/N) "))
    print()

    # Initialize names dictionary. Indexed at population number.
    # Population number is independent from participant number.
    names = {}

    # Using names requires entering names of each participant.
    if useNames:
        for i in range(n):
            names[i] = input("Participant: ")
            print("You get one of the {}! For now.".format(item))
        print()
    else:
        print(
            "To start, participants 0 through {} get one of the {} (for now...)".format(
                n - 1, item))
        # Sets name of each person into dictionary.
        for i in range(n):
            names[i] = str(i)
        print()

    # Define bus with first n people.
    bus =  list(range(n))

    print("List anyone who was gone, end with a blank line...")

    # Participant number defined independently of population number.
    participant_number = n
    line = input()
    while line != "":
        # Searches dictionary for name. If it appears,
        # it breaks out of for loop and uses that index.
        # -1 indicates not found
        index = -1
        for i, name in names.items():
            if line == name:
                index = i
                break

        if index == -1:
            continue

        # Resets name entered. User may enter name or use next number 
        if useNames:
            names[index] = input("New Participant: ")
        else:
            names[index] = str(participant_number)
        participant_number += 1
        print(
            "New Participant {} gets one of the {} (for now) then.".format(
                names[index], item))
        line = input()

    # Name index is the population number entered into dictionary.
    name_index = n
    # User given option to quit or skip a number if not using names; updates part. number.
    participant_number, more_participants = check_quitting(participant_number, useNames)
    while more_participants:
        if useNames:
            name = input("Participant: ")
            names[name_index] = name
        else:
            names[name_index] = participant_number

        # Algorithm R sampling. See wikipedia. User steals from previous participants.
        if rng.random() < (n / len(names)):
            i = rng.randrange(0, n)
            print(
                "Participant {} steals one of the {} from participant {}!".format(
                    names[name_index], item, names[bus[i]]))
            bus[i] = name_index
        else:
            print("Nothing happened.")

        name_index += 1
        participant_number += 1
        participant_number, more_participants = check_quitting(participant_number, useNames)

    print()
    print_winners(names, bus)


def yes_no_check(input_string, default=False):
    """Return boolean value of use input

    Takes string and optional default value that returns with a blank value.
    """
    input_string = input_string.lower()
    if (input_string == "y" or
        input_string == "yes"):
        return True
    elif (input_string == 'n' or
          input_string == 'no'):
        return False

    return default


def check_quitting(participant_number, useNames):
    """Query user whether to continue adding participants.

    User may choose to skip numbers when not using names.
    Otherwise, it will simply stop immediately.
    """
    if useNames:
        quit = yes_no_check(
            input("Continue with participant {} (Y/n)? ".format(
                participant_number)), True)
        return participant_number, quit
    else:
        here = yes_no_check(
            input("Continue with participant {} (Y/n)? ".format(
                participant_number)), True)
        if not here:
            if yes_no_check(input("Quit entirely (y/N)? ")):
                return participant_number, False
            else:
                # Skip number
                participant_number += 1
                return check_quitting(participant_number, useNames)
        else:
            return participant_number, True


def print_winners(names, bus):
    """Prints winners after end of the raffle"""
    if len(bus) == 1:
        print("Winner is {}!".format(names[bus[0]]))
    elif len(bus) == 2:
        print("Winners are: {} and {}!".format(
            names[bus[0]], names[bus[1]]))
    elif len(bus) > 2:
        print("Winners are: ", end='')
        for i in bus[0:-1]:
            print("{}, ".format(names[i]), end = '')
        print("and {}!".format(names[bus[-1]]))


if __name__ == "__main__":
    main()
