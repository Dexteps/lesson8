grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted(list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}))
average_rating = {}
for i in range(len(students)):
    average_rating[students[i]] = sum(grades[i]) / len(grades[i])
print(average_rating)
