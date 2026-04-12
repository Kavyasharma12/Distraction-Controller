def grade(env, initial_tasks=5):
    pending = env.state_data.get("pending_tasks", initial_tasks)
    completed = initial_tasks - pending
    score = completed / initial_tasks

    if score <= 0:
        return 0.2
    elif score >= 1:
        return 0.8
    return score
