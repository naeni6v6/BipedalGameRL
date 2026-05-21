# gymnasium 버전 테스트 코드
import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("BipedalWalker-v3", render_mode="human")
model = PPO.load("models/bipedal_final")

obs, info = env.reset()
for _ in range(2000):
    action, _ = model.predict(obs)
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()

env.close()