def compute_grade(score):
    if score >= 10.0:
        return "Bad Score"
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    elif score < 0.6:
        return 'F'

score = input('Enter Score: ')

try:
    floatScore = float(score)
    grade = compute_grade(floatScore)
    print('Final Grade: ', grade)
except:
    print('Bad score')





    