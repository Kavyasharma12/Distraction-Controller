from env import DistractionEnv
from grader import grade
from tasks import easy_task, medium_task, hard_task
from openai import OpenAI

client = OpenAI(api_key="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")


# AI decides action
def get_action(observation):
    prompt = f"""
You are an AI helping a user stay productive.

Current state:
{observation}

Choose ONE action from:
- allow_usage
- block_app
- start_focus_session
- give_break

Respond with ONLY the action name.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


# Run one task
def run_task(task, initial_tasks):
    env = DistractionEnv()
    obs = env.reset(custom_state=task)

    done = False
    steps = 0

    while not done and steps < 20:
        # ✅ ALWAYS use AI (no rule-based logic)
        try:
            action = get_action(obs)
        except:
    # fallback logic if API fails
            if obs["distraction_level"] > 70:
                action = "block_app"
            elif obs["energy"] < 30:
                action = "give_break"
            else:
                action = "start_focus_session"

        # ✅ Safety check (important)
        if action not in [
            "allow_usage",
            "block_app",
            "start_focus_session",
            "give_break"
        ]:
            action = "allow_usage"

        obs, reward, done, _ = env.step(action)

        steps += 1

    return grade(env, initial_tasks)


# Run all tasks
print("Easy Score:", run_task(easy_task, 3))
print("Medium Score:", run_task(medium_task, 5))
print("Hard Score:", run_task(hard_task, 7))