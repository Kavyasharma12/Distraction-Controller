# Distraction Control Environment

## 💡 Problem
In today's digital world, users often struggle with distractions from apps and notifications. This environment simulates a real-world scenario where an AI agent helps manage user focus and productivity.

---

## ⚙️ Environment Description
This is a reinforcement learning-style environment where:
- The agent observes user state
- Takes actions to reduce distraction
- Receives rewards based on productivity improvements

---

## 📊 Observation Space
```json
{
  "distraction_level": 0-100,
  "energy": 0-100
}