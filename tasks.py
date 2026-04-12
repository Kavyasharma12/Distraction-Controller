from env import DistractionEnv
from grader import grade

def task1():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")  # reduces pending
    return grade(env)

def task2():
    env = DistractionEnv()
    env.reset()
    env.step("block_app")  # no pending change
    return grade(env)

def task3():
    env = DistractionEnv()
    env.reset()
    env.step("give_break")  # different behavior
    return grade(env)

tasks = [task1, task2, task3]
