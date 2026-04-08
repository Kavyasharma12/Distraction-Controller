def grade(env, initial_tasks=5):
    completed = initial_tasks - env.state_data["pending_tasks"]
    score = completed / initial_tasks
    return max(0.0, min(1.0, score))