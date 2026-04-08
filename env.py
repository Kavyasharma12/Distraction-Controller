class DistractionEnv:
    def __init__(self):
        self.state_data = {}

    def reset(self, custom_state=None):
        if custom_state:
            self.state_data = custom_state.copy()
        else:
            self.state_data = {
                "distraction_level": 50,
                "energy": 50
            }

        return {
            "distraction_level": self.state_data["distraction_level"],
            "energy": self.state_data["energy"]
        }

    def step(self, action):
        reward = 0
        done = False

        # natural increase
        self.state_data["distraction_level"] += 2

        if action == "block_app":
            self.state_data["distraction_level"] -= 10
            self.state_data["current_app"] = "none"
            reward += 1

        elif action == "start_focus_session":
            if self.state_data["energy"] > 20:
                self.state_data["pending_tasks"] -= 1
                self.state_data["energy"] -= 15
                self.state_data["distraction_level"] -= 15
                reward += 2
            else:
                reward -= 1

        elif action == "give_break":
            self.state_data["energy"] += 10
            self.state_data["distraction_level"] -= 5
            reward += 0.5

        elif action == "allow_usage":
            self.state_data["distraction_level"] += 5
            reward -= 1

        # penalties
        if self.state_data["distraction_level"] > 80:
            reward -= 2

        if self.state_data["energy"] < 20:
            reward -= 1

        # time update
        self.state_data["time"] += 1

        # clamp
        self.state_data["distraction_level"] = max(0, min(100, self.state_data["distraction_level"]))
        self.state_data["energy"] = max(0, min(100, self.state_data["energy"]))
        self.state_data["pending_tasks"] = max(0, self.state_data["pending_tasks"])

        # done condition
        if self.state_data["pending_tasks"] == 0 or self.state_data["time"] >= 18:
            done = True

        return obs, reward, done, {}

    def state(self):
        return self.state_data
