last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjets = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = list(zip(subjets, grades))

gradebook.append(("visial arts", 93))
print(gradebook)

last_semester_gradebook = [("politics", 90), ("latin", 99), ("dance", 100), ("architecture", 78)]

full_gradebook = list(zip(gradebook, last_semester_gradebook))
print(last_semester_gradebook)