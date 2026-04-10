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
if __name__ == "__main__":
    print("START")

    obs = reset()
    print("STEP", obs)

    for _ in range(3):
        result = step("start_focus_session")
        print("STEP", result)

    print("END")
