'''
You have one hundred cats.
One day, you decide to arrange all your cats in a giant circle. Initially,
none of your cats has a hat on. You walk around the circle a hundred
times, always starting with the first cat (cat #1). Each time you stop at
a cat, you check if it has a hat on. If it doesn’t, then you put a hat on
it. If it does, then you take the hat off.
1. The first round, you stop at every cat, placing a hat on each one.
2. The second round, you stop only at every second cat (#2, #4, #6,
#8, and so on).
3. The third round, you stop only at every third cat (#3, #6, #9, #12,
and so on).
4. You continue this process until you’ve made one hundred rounds
around the cats. On the last round, you stop only at cat #100.
Write a program that simply outputs which cats have hats at the end.

Description
essentially this code will be a loop within a loop using while loops
Setup a count variable that keeps track of what cat we are up too. 
will use the same variable to update a step variable.
Psuedo Code

Initialize an array with false booleans 

while the count variable is less then or equal to how many cats 
there are (in this case 100) += 1. 

While the step variable is
less then or equal to 100 increment by the count_index variable 
(if the step variable is say 3 then increment by 3, e.g 3,6,9,12,etc)
use the step variable to check the list index
if the list index is false then change to true and vice versa

'''

def cats(number_of):
    
    # Create an array of n number of items
    cat_with_hat = [False] * number_of
       
    index = 0

    while index <= number_of:
        
        index += 1

        # Start step from zero index
        step = step_count - 1 

        while step <= number_of:
            if cat_with_hat[step] == False:
                cat_with_hat[step] = True
            elif cat_with_hat[step] == True:
                cat_with_hat[step] = False
            step_count += index_count
            print(step)
            
    
    return cat_with_hat.count(True)
cats(100) 