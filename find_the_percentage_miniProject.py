
student_records = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

student_name = input("Enter a name: ")


if student_name in student_records:
    marks = student_records[student_name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark: {int(average)}")
else:
    print("Student not found.")
