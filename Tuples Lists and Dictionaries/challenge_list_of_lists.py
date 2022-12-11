'''
Using universities, enrollment_stats(), mean(), and median(), calculate the total number of students, the total tuition, the mean and median numbers of students, and the mean and median tuition values.
'''

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

'''
Define a function, enrollment_stats(), with a single parameter. This
parameter should be a list of lists in which each individual list contains
three elements:
1. The name of a university
2. The total number of enrolled students
3. The annual tuition fees
enrollment_stats() should return two lists, the first containing all the
student enrollment values and the second containing all the tuition
fees.
'''

def enrollment_stats(university_details):
    student_num_per_uni = []
    tuition_fees =[]
    for _,student_num,tuition_fee in university_details:
        student_num_per_uni.append(student_num)
        tuition_fees.append(tuition_fee)
    return [student_num_per_uni,tuition_fees]    

'''
Next, define two functions, mean() and median(), that take a single list
argument and return the mean or median of the values in each list,
respectively.
'''

# Basically mean == average of the data inputted.
def mean(data):
    data_len = len(data)
    return sum(data) / data_len

# Great explanation of media here https://www.codingem.com/python-calculate-median/
def median(data):
    sorted_data = sorted(data)
    data_len = len(sorted_data)
    middle = (data_len - 1) // 2
    if middle % 2:
        return sorted_data[middle]
    else:
        return (sorted_data[middle] + sorted_data[middle + 1]) / 2.0

'''
Finally, output all values and format the output so that it looks like
this:
******************************
Total students: 77,285
Total tuition: $ 271,905
Student mean: 11,040.71
Student median: 10,566
Tuition mean: $ 38,843.57
Tuition median: $ 39,849
******************************
'''

def total_amounts(data):
    # Variables used in strings below
    students,tuition = data
    stars = '******************************'

    print(f'{stars}')
    print(f'Total students: $ {sum(students):,}')
    print(f'Total tuition: $ {sum(tuition):,}')
    print(f'Student mean: {mean(students):,.2f}')
    print(f'Student meadian: {median(students):,.2f}')
    print(f'Tuition mean: {mean(tuition):,.2f}')
    print(f'Tuition meadian: {median(tuition):,.2f}')
    print(f'{stars}')

if __name__ == "__main__":
    total_amounts(enrollment_stats(universities))