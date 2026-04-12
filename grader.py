def grade(env, initial_tasks=5):
    completed = initial_tasks - env.state_data["pending_tasks"]
    score = completed / initial_tasks

    # MUST be strictly between 0 and 1
    if score <= 0:
        score = 0.1
    if score >= 1:
        score = 0.9

    return score
