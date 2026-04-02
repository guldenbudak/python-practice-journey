highest_score = 0
student_info = []
students = [
    {"name": "Ali", "score": 78},
    {"name": "Ayşe", "score": 92},
    {"name": "Ali", "score": 92},
    {"name": "Gülden", "score": 92},
    {"name": "Mehmet", "score": 88},
    {"name": "Elif", "score": 85},
    {"name": "Ahmet", "score": 90},
    {"name": "Zeynep", "score": 85},
    {"name": "Can", "score": 76},
    {"name": "Deniz", "score": 92},
    {"name": "Burak", "score": 81},
    {"name": "Selin", "score": 88},
    {"name": "Mert", "score": 74},
    {"name": "Ece", "score": 90},
    {"name": "AAli", "score": 92},
    {"name": "Kaan", "score": 79}
]
for student in students:

    name = student["name"]
    score = student["score"]
    if score > highest_score:
        highest_score = score
        student_info = [student]
    elif score == highest_score:
        student_info.append(student)

print(sorted(student_info, key=lambda x: x["name"]))
