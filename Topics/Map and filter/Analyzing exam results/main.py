scores_maths = [100, 75, 90, 95, 60, 50, 95, 85, 70, 75,
                90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                95, 45, 60, 45, 80, 70, 55, 45, 60, 90]

scores_physics = [50, 65, 85, 100, 60, 55, 90, 85, 70, 90,
                  50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                  60, 90, 40, 90, 95, 90, 80, 95, 85, 80,
                  95, 90, 75, 50, 80, 70, 50, 35, 65, 90]

scores_english = [50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                  50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                  90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                  50, 65, 85, 100, 60, 55, 90, 85, 70, 90]

scores = map(lambda x, y, z: x+y+z, scores_english, scores_physics, scores_maths)
overall_scores = list(scores)
students = filter(lambda x: x >= 270, overall_scores)
admitted_students = list(students)

print(len(admitted_students))
