def determine_grade(average):
    if average >= 75:
        return 'A'
    elif 60 <= average < 75:
        return 'B'
    elif 40 <= average < 60:
        return 'C'
    else:
        return 'D'


marks1 = float(input("Enter the marks for subject 1: "))
marks2 = float(input("Enter the marks for subject 2: "))
marks3 = float(input("Enter the marks for subject 3: "))
marks4 = float(input("Enter the marks for subject 4: "))


average = (marks1 + marks2 + marks3 + marks4) / 4

grade = determine_grade(average)

print(f"Average marks: {average:.2f}")
print(f"Grade: {grade}")
