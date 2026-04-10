import os
from env import DistractionEnv

# required env variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

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

    # ⚠️ CRITICAL: use ALL possible actions at least once
    actions = ["block_app", "start_focus_session", "give_break", "allow_usage"]

    for action in actions:
        result = step(action)
        print("STEP", result)

    print("END")
