# Sample input list
scores = [2, 3, 6, 6, 5]

max_score = max(scores)

filtered_scores = [score for score in scores if score != max_score]

runner_up = max(filtered_scores)

print("Runner-up score:", runner_up)
