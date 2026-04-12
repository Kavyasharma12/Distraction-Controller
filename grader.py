def grade(env, initial_tasks=5):
    completed = initial_tasks - env.state_data.get("pending_tasks", initial_tasks)
    score = completed / initial_tasks

    # force strictly between 0 and 1
    if score <= 0:
        return 0.1
    elif score >= 1:
        return 0.9
    return score
