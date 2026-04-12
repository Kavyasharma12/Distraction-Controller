from env import DistractionEnv
from grader import grade

def task1():
    env = DistractionEnv()
    env.reset()
    return grade(env)

def task2():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")
    return grade(env)

def task3():
    env = DistractionEnv()
    env.reset()
    env.step("block_app")
    return grade(env)
tasks = [task1, task2, task3]
