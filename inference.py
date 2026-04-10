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
    print("Starting environment...")

    obs = reset()
    print("Initial state:", obs)

    for _ in range(3):
        result = step("start_focus_session")
        print("Step result:", result)
