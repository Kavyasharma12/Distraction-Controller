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

def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
