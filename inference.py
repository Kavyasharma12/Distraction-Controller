from env import DistractionEnv

env = DistractionEnv()

def reset():
    return env.reset()

def step(action):
    obs, reward, done, _ = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }
