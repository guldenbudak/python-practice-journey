grades_by_course = {
      "Matematik": [70, 85, 90],
      "Türkçe": [60, 75],
      "Fizik": [40, 55, 65]
}
print(grades_by_course)
for key,item in grades_by_course.items():
      avg = sum(item)/len(item)
      grades_by_course[key] = float(f"{avg:.2f}")
print(grades_by_course)