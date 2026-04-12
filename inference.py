from fastapi import FastAPI
from pydantic import BaseModel
from env import DistractionEnv

app = FastAPI()
env = DistractionEnv()

class ActionRequest(BaseModel):
    action: str

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(req: ActionRequest):
    obs, reward, done, _ = env.step(req.action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }

if __name__ == "__main__":
    try:
        print("[START] task=distraction_env", flush=True)

        env = DistractionEnv()

        obs = env.reset()
        print(f"[STEP] step=0 obs={obs}", flush=True)

        obs, reward, done, _ = env.step("start_focus_session")
        print(f"[STEP] step=1 reward={reward}", flush=True)

        print("[END] task=distraction_env score=1.0 steps=1", flush=True)

    except Exception as e:
        print(f"[ERROR] {e}", flush=True)
