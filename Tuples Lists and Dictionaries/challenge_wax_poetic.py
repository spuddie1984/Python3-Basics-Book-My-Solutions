'''
Using the randomly selected words, generate and display a poem with
the following structure inspired by Clifford Pickover:

{A/An} {adj1} {noun1}
{A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}

Here, adj stands for adjective and prep for preposition.
Here’s an example of the kind of poem your program might generate:

A furry horse
A furry horse curdles within the fragrant mango
extravagantly, the horse slurps
the mango meows beneath a balding extrovert

Each time your program runs, it should generate a new poem.
'''
import random


# Create five lists for different word types:
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
"extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows",
"explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant",
"exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon",
"for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly",
"furiously", "sensuously"]


def random_word_type_selector(number_of,choices):
    random_choices = []
    for number in range(number_of):
        random_choices.append(random.choice(choices))
    return random_choices

'''
Randomly select the following number of elements from each list:
• Three nouns
• Three verbs
• Three adjectives
• Two prepositions
• One adverb
'''
[noun1,noun2,noun3] = random_word_type_selector(3,nouns)
[verb1,verb2,verb3] = random_word_type_selector(3,verbs)
[adj1,adj2,adj3] = random_word_type_selector(3,adjectives)
[prep1,prep2] = random_word_type_selector(2,prepositions)
[adverb1] = random_word_type_selector(1,adverbs)

print(f'A {adj1} {noun1}')
print(f'A {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}')
print(f'{adverb1}, the {noun1} {verb2}')
print(f'the {noun2} {verb3} {prep2} a {adj3} {noun3}')