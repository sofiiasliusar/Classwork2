my_arr = []
my_arr = list()
my_arr = [1, 2, 3.5, "Hello", True, [1,2,3]]
d_arr = [[1,2,3],
         [1,2,3],
         [1,2,3]] 
print(my_arr)

fruits = ["apple","pear","peach","cherry"]
exotic_fruits = ["kiwi", "grape", "dragon-fruit"]
print(fruits)
new_arr = fruits + exotic_fruits
print(exotic_fruits)
print(new_arr)
fruits.extend(exotic_fruits)
print(fruits)

# fruits.append(input("Enter your favorite fruit"))
# print(fruits)
# fruits.append(exotic_fruits)
# print(fruits)

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

student_height = [175, 178, 179, 190, 185, 193, 168, 160, 175]
# student_height ={175, 178, 179, 190, 185, 193, 168, 160, 175}
# #?              0    1    2    3    4    5    6    7    8
print(student_height)
student_height.sort()
print(student_height)

print(student_height[0]) 
average = 0 

for height in student_height:
    average += height
print(round(average/len(student_height), 2))
average1 = sum(student_height)
print(round(average1/len(student_height), 2))

del student_height[5]
average1 = sum(student_height)
print(round(average1/len(student_height), 2))
student_height.clear()
print(student_height)

my_dict = {}
my_dict = dict()
my_dict = {"name" : "Roman",
           "surname" : "Vytvytskyi",
           "age" : "32",
           "teacher" : True,
           "work-days" : [1,2,4,5]}

print(my_dict['work-days'][2])
print(my_dict)
my_dict["adress"] = "Ivano-Frankivsk"
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
