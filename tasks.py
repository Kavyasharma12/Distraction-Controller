from env import DistractionEnv

def task1():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")
    return env

def task2():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")
    env.step("start_focus_session")
    return env

def task3():
    env = DistractionEnv()
    env.reset()
    env.step("start_focus_session")
    env.step("block_app")
    return env

tasks = [task1, task2, task3]
