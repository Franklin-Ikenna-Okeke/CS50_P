#Loop with List

students = ["Hermione", "Harry", "Ron"]
houses = ["Gryffindor","Gryffindor", "Gryffindor", "Syltherin"]

#python is meant to be readable so use a reasonable variable instead of a letter 
# of pythonic case like "_"

for student in students:
    print(student)

# alt list with num to loop

for i in range(len(students)):
    print(i + 1, students[i])


#PYTHON DICTIONARY: Dict takes in keys and value and can be called an advance list

students_dict = {
    "Hermione" : "Gryffindor",
    "Harray" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco": "Slytherin"
    }

for student in students_dict:
    print(student, students_dict[student], sep=", ") #"with the keyword "sep", the output come out as eg.: Hermione Gryffindor.

#List of Dictionary
students_ls_of_dict = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "JAck Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students_ls_of_dict:
    print(student["name"], student["house"], student["patronus"], sep=", ")
