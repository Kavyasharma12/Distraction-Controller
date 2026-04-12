def grade(env, initial_tasks=5):
    completed = initial_tasks - env.state_data["pending_tasks"]
    score = completed / initial_tasks
    return max(0.01, min(0.99, score))
