import gym
import pygame
from gym.utils.play import play


ep_reward=0
episode=1

def callback(obs_t, obs_tp1, action, rew, terminated, truncated, info):
    global ep_reward
    global episode
    ep_reward+=rew
    if terminated or truncated:
        print(f"Reward after Episode {episode} is {ep_reward}")
        ep_reward = 0  
        episode+=1
    return None


def interactive_cartpole2():
    env = gym.make('CartPole-v0', render_mode="rgb_array_list")
    mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 1}  
    play(env, keys_to_action=mapping, callback=callback)


# def interactive_cartpole():
#     """
#     Allows you to control the cart with the arrow keys.
#     Press Space to reset the cart-pole and press Escape to close the window.
#     """

#     env = gym.make('CartPole-v1')
#     # Make sure to render once so that the viewer exists
#     env.reset()
#     env.render()
#     # Inject key_handler
#     key_handler = key.KeyStateHandler()
#     env.viewer.window.push_handlers(key_handler)

#     action = 0
#     already_done = False
#     t = 0
#     while True:
#         if key_handler[key.ESCAPE]:
#             break

#         if key_handler[key.SPACE]:
#             env.reset()
#             action = 0
#             t = 0
#             already_done = False

#         if key_handler[key.LEFT]:
#             action = 0
#         elif key_handler[key.RIGHT]:
#             action = 1

#         observation, reward, done, info = env.step(action)
#         env.render()

#         if done and not already_done:
#             print(f'Episode finished after {t+1} time steps')
#             already_done = True

#         t += 1

#     env.close()


if __name__ == '__main__':
    interactive_cartpole2()