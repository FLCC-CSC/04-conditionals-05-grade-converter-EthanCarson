# FILE NAME - grade_converter.py

# NAME: Ethan Carson
# DATE: 10/5/2025
# BRIEF DESCRIPTION:  This program converts a grade percentage into a grade letter, based on user input.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Grade Converter =====")
grade = int(input('Enter a numerical grade (1-100): '))
if(grade < 65):
    print("F")
elif(grade < 70):
    print('D')
elif(grade < 80):
    print('C')
elif(grade < 90):
    print('B')
elif(grade < 100):
    print('A')
else: print('A+')
########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

Don't overthink this problem. You need to focus on a specific range, what ways can that be done in Python? pick ur favorite, they will all work if done correctly.





'''
