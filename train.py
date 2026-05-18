import gym
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import CheckpointCallback
import os

os.makedirs("models", exist_ok=True)
env = gym.make("BipedalWalker-v3")
checkpoint = CheckpointCallback(save_freq=100000, save_path="./models/", name_prefix="bipedal_ppo")
model = PPO("MlpPolicy", env, learning_rate=0.0003, n_steps=2048, batch_size=64, gamma=0.99, verbose=1, device="cpu")
print("학습 시작!")
model.learn(total_timesteps=1000000, callback=checkpoint)
model.save("models/bipedal_final")
print("학습 완료!")