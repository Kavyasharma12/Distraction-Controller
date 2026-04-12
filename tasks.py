from env import DistractionEnv

def task1():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")
    return 0.2

def task2():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")
    env.step("start_focus_session")
    return 0.4

def task3():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")
    env.step("block_app")
    return 0.3

tasks = [task1, task2, task3]
