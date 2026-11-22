student = {}

student["name"] = input("Enter student name: ")
student["roll"] = int(input("Enter roll number: "))
student["marks"] = float(input("Enter marks: "))

print("\nStudent Details")
print("Name:", student["name"])
print("Roll Number:", student["roll"])
print("Marks:", format(student["marks"], ".2f"))
