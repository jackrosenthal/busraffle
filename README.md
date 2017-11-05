# _n_-item Raffle Simulation using "Algorithm R" aka. "Crazy Bus Driver Algorithm"

This script is useful for running an raffle where you are giving away _n_
identical items to an unknown number _p_ participants where _n <= p_. Each participant will have a
equal probability of having one of the items by the end of the simulation.

Mathematically, this relies on "Algorithm R" for reservoir sampling:

    procedure Sample(population, n) (
        Δ A is an array of size n
        Initialize A to the first n elements from population
        j <- n
        for each of the remaining elements in the population as e (
            j <- j + 1
            if Bernoulli(n / j) (
                Choose a random element from A and swap it with e
            )
        )
        return A
    )

A proof that this algorithm creates a random sample can be found
[here](https://en.wikipedia.org/wiki/Reservoir_sampling#Algorithm_R).

Here is a sample run of the script:

    What are you giving away? shirts
    How many shirts are you giving away? 10
    Do you want to enter names? (y/N) n
    To start, participants 0 through 9 get one of the shirts (for now...)

    List anyone who was gone, end with a blank line...
    4
    Participant 10 gets one of the shirts (for now) then.

    Continue with participant 11 (Y/n)? y
    Nothing happened.
    Continue with participant 12 (Y/n)? y
    Participant 12 steals one of the shirts from participant 6!
    ...
    Continue with particpant 54 (Y/n)? n
    Quit entirely (y/N)? y
    
    Winners are: 0, 14, 3, 48, 22, 35, 50, and 25!
