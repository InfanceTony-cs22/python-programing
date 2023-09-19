# Get marks for 5 subjects
subject_marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    subject_marks.append(mark)

# Calculate the average
average_marks = sum(subject_marks) / 5

# Display the average marks
print(f"The average marks for 5 subjects are: {average_marks:.2f}")
