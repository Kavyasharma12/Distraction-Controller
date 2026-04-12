from env import DistractionEnv
from grader import grade

def task1():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")  # reduces pending_tasks by 1
    return grade(env)

def task2():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")
    env.step("start_focus_session")  # reduces by 2
    return grade(env)

def task3():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")
    env.step("block_app")  # mix actions but still reduce once
    return grade(env)

tasks = [task1, task2, task3]
