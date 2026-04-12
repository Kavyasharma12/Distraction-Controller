from env import DistractionEnv
from grader import grade

def task1():
    env = DistractionEnv()
    env.reset({
        "distraction_level": 50,
        "energy": 50,
        "pending_tasks": 5,
        "time": 0
    })
    env.step("start_focus_session")
    return grade(env)

def task2():
    env = DistractionEnv()
    env.reset({
        "distraction_level": 70,
        "energy": 40,
        "pending_tasks": 5,
        "time": 0
    })
    env.step("block_app")
    return grade(env)

def task3():
    env = DistractionEnv()
    env.reset({
        "distraction_level": 30,
        "energy": 60,
        "pending_tasks": 5,
        "time": 0
    })
    env.step("give_break")
    return grade(env)

tasks = [task1, task2, task3]
