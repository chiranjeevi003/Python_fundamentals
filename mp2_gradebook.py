# Grade book 

students = {
    "Chiru":85,
    "Dusky":92,
    "Deeks":67,
    "arjun":78,
    "kiran":55
}
def get_grades(score):
    if score >= 90: return 'A'
    elif score >= 75: return 'B'
    elif score >= 60: return 'C'
    else: return 'F'


def print_report(students):
    print('\n-------Grade Report-------')
    print('\nName\t     Score\tGrade')
    for name, score in students.items():
        print(f'{name:10} | {score:5} |\t{get_grades(score)}')


def class_stats(students):
    score = list(students.values())
    avg = sum(score) / len(score)
    top = max(students, key=students.get)
    print(f'\nClass Average : {avg:.1f}')
    print(f'Top Students : {top}({students[top]})')


print_report(students)
class_stats(students)

#add new students
name = input("\nAdd Student Name : ")
score = int(input("Score (0-100): "))
students[name] = score
print_report(students)
class_stats(students)
