#Write a Python function that takes two lists and returns True if they have at least one common member.

#List one contains integer values: 12, 45, 78, 65, 3, 20

#list1 = [12, 45, 78, 65, 3, 20]

#List two contains integer values: 51, 36, 27, 91, 20, 9

#list2 = [51, 36, 27, 91, 20, 9]

#First we must define a function, then include our two parameters: list1, list2. 

list1 = [12, 45, 78, 65, 3, 20]

list2 = [51, 36, 27, 91, 20, 9]

def common_member(list1, list2):
     for item in list1:
        if item in list2:
            return True
     return False 
     
print(common_member(list1, list2))





 

