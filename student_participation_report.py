lesson_minutes = {}
student_minutes = {}
attendance = [
    {"student": "Ali", "lesson": "Python", "minutes": 45},
    {"student": "Ali", "lesson": "SQL", "minutes": 30},
    {"student": "Alisa", "lesson": "Python", "minutes": 60},
    {"student": "Ali", "lesson": "Python", "minutes": 15},
    {"student": "Mehmet", "lesson": "Java", "minutes": 50},
    {"student": "Zeynep", "lesson": "Python", "minutes": 40},
    {"student": "Ali", "lesson": "SQL", "minutes": 35},
    {"student": "Alisa", "lesson": "Java", "minutes": 55},
    {"student": "Mehmet", "lesson": "Python", "minutes": 20},
    {"student": "Zeynep", "lesson": "SQL", "minutes": 25},
    {"student": "Ali", "lesson": "Java", "minutes": 45},
    {"student": "Alisa", "lesson": "Python", "minutes": 30},
    {"student": "Mehmet", "lesson": "SQL", "minutes": 60},
    {"student": "Zeynep", "lesson": "Java", "minutes": 35},
    {"student": "Ali", "lesson": "Python", "minutes": 50}
]
for item in attendance:

    student = item["student"]
    minutes = item["minutes"]
    lesson = item["lesson"]
    student_minutes[student] = student_minutes.get(student, 0) + minutes
    lesson_minutes[lesson] = lesson_minutes.get(lesson, 0) + minutes
print(student_minutes)
print(lesson_minutes)
