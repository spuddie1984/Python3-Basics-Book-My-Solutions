'''
How many flips are needed on average to for a coin to land on a both
a heads and a tails?

Write a simulation that runs 10,000 trials of the experiment and
prints the average number of flips per trial.
'''
import random

# generate a random number of heads and tails and then return average number
def coin_flip():
    if random.randint(0,1) == 0:
        return "heads"
    else:
        return "tails"    

flips = 0
num_trials = 10_000

for trial in range(num_trials):
    if coin_flip() == "heads":
        flips = flips + 1
        while coin_flip() == "heads":
            flips = flips + 1
        flips = flips + 1
    else:
        flips = flips + 1
        while coin_flip() == "tails":
            flips = flips + 1
        flips = flips + 1

avg_flips_per_trial = flips / num_trials
print(f"The average number of flips per trial is {avg_flips_per_trial}.")

if __name__ == "__main__":
    coin_flip()
