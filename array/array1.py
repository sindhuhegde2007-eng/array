# Accept scores from the user
scores_input = input("Enter scores separated by spaces: ")

# Convert the input string into a list of numbers
scores = [float(score) for score in scores_input.split()]

# Calculate sum and average
total = sum(scores)
average = total / len(scores)

# Display results
print("Sum of scores:", total)
print("Average of scores:", average)
