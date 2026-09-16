# Initial list of scores
scores = [72, 45, 90, 61, 38]

# Trackers for passed, failed, and running total
passed_count = 0
failed_count = 0
total_score = 0

# Loop through each score in the list
for score in scores:
    total_score += score  # Accumulate total score
    
    # Determine the grade using if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    # Count passed and failed learners
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1
        
    # Print individual score and grade
    print(f"Score: {score} - Grade: {grade}")

# Calculate average
average = total_score / len(scores)

# Print final results
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average: {round(average, 1)}")
