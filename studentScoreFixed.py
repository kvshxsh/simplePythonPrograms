# New, bug-free and updated version of student.py using functions. I've just changed up the strings a little bit, everything else on this is u/jimtk's solution that he posted on my Reddit post on r/learnpython.

def get_score(subject):
    while True:
        result = float(input(f"Enter the marks scored in {subject}: "))
        if 0 <= result <= 100:
            return result
        print(f"please enter valid score for {subject}")

def get_grades(perc):
    grades = { (0,40): 'F', (41,50): 'C', (51,65): 'B',
               (66,75): 'B+', (76,85): 'A', (86,100): 'A+' }
    for k in grades:
        if k[0] <= perc <= k[1]:
            return grades[k]

def main():
    subjects = ['maths', 'science', 'computer']
    total_marks = sum((get_score(subj) for subj in subjects))
    percentage = (total_marks/(len(subjects*100)))*100
    grade = get_grades(percentage)
    print(f"Grade: {grade}")
    print("total marks scored in class x : %.2f" % (total_marks))
    print("percentage scored by the student : %.2f" % (percentage))

main()
