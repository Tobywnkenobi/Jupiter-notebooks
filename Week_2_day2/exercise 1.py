# Given a list as a parameter,write a function that returns a list of numbers that are less than ten

# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

over_ten = [1,11,14,5,8,9]
under_ten = []


def numb_answer(numb):
    for n in numb:
        if n < 10:
            under_ten.append(n)
numb_answer(over_ten)
    
print("orignal", over_ten)
print("Under ten", under_ten)