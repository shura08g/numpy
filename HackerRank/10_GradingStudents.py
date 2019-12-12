'''
HackerLand University has the following grading policy:
  Every student receives a grade in the inclusive range from 0 to 100.
  Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's
grade according to these rules:
  If the difference between the grade and the next multiple of 5 is less than
  3, round grade up to the next multiple of 5.
  If the value of grade is less than 38, no rounding occurs as the result will
  still be a failing grade.

For example, grade = 84 will be rounded to 85 but grade = 29 will not be
rounded because the rounding would result in a number that is less than 40.

Given the initial value of grade for each of Sam's n students, write code
to automate the rounding process.

Input Format
The first line contains a single integer, n, the number of students.
Each line i of the n subsequent lines contains a single integer.

Output Format
For each print the rounded grade on a new line.

Sample Input 0
4
73
67
38
33
Sample Output 0
75
67
40
33
'''


# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def gradingStudents(grades):
    result = []
    for i in grades:
        if i < 40:
            if (40 - i) < 3:
                i = 40
                result.append(i)
            else:
                result.append(i)
        else:
            if (i % 5) < 3:
                result.append(i)
            else:
                i += 5 - (i % 5)
                result.append(i)
    return result


if __name__ == '__main__':
    # fptr = open('GradingStudent.txt', 'w')
    # grades_count = int(input().strip())
    # grades = []
    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)
    grades = [73, 67, 38, 33, 72, 74, 75, 76, 77, 78]
    result = gradingStudents(grades)
    for i in result:
        print(i)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
