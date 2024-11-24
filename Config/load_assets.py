import pygame
import os
import cv2


class AssetLoader:
    def __init__(self):
        # Initialize the dictionary to store different asset types
        self.assets = {
            "logo": None,
            "fruits": [],
            "long_fruits": {},
            "sliced_fruits": {},
            "long_slash": [],
            "rankings": [],
            "star": [],
            "player": {
                "idle": [],
                "attack_1": [],
                "attack_2": [],
                "take_hit": [],
                "death": [],
                "trailing_slash": [],
            },
            "sounds": {
                "sword_attacks": [],
                "fruit_slashed": [],
                "player_hit": [],
                "flame_trailing": [],
                "scores": {},
                "slow_motion": None,
                "checkpoint": None,
                "rankings": [],
                "slam": None,
            },
            "videos": {
                "Ghost Town": None,
            },
            "fruit_deaths": {
                "sparks1": [],
                "sparks2": [],
                "splatter": []
            }
        }

        # Load assets
        self.load_logo()
        self.load_fruit_images()
        self.load_sliced_fruit_images()
        self.load_player_animations()
        self.load_sounds()
        self.load_fruit_death_animations()
        self.load_long_slash()
        self.load_long_fruit_images()
        self.load_trailing_slash_animations()
        self.load_videos()
        self.load_star_checkpoint_animation()
        self.load_rankings()

    def load_videos(self):
        video = cv2.VideoCapture('Songs/Ghost Town/background.mp4')
        self.assets["Ghost Town"] = video

        video = cv2.VideoCapture('Songs/I Want It That Way/background.mp4')
        self.assets["I Want It That Way"] = video

        video = cv2.VideoCapture('Songs/Numb/background.mp4')
        self.assets["Numb"] = video

        video = cv2.VideoCapture('Songs/Vagalumes/background.mp4')
        self.assets["Vagalumes"] = video

    def load_logo(self):
        image = pygame.image.load(f'images/logo.png').convert_alpha()
        image = pygame.transform.scale(image, (image.get_width() * 0.5, image.get_height() * 0.5))
        self.assets["logo"] = image

    def load_rankings(self):
        for i in range(1, 8):
            image = pygame.image.load(f'images/rankings/{i}.png').convert_alpha()
            self.assets['rankings'].append(image)

    def load_long_fruit_images(self):
        # Path to the long fruit directory
        long_fruits_path = 'images/fruits/long_fruits'

        for fruit_name in os.listdir(long_fruits_path):
            fruit_dir = os.path.join(long_fruits_path, fruit_name)

            # Check if the directory exists for the specific fruit
            if os.path.isdir(fruit_dir):
                self.assets["long_fruits"][int(fruit_name)] = {"start": None, "middle": None, "end": None}

                # Load the 'start' image
                start_path = os.path.join(fruit_dir, "start.png")
                if os.path.exists(start_path):
                    start_image = pygame.image.load(start_path).convert_alpha()
                    start_image = pygame.transform.scale(start_image,
                                                         (start_image.get_width() * 4, start_image.get_height() * 4))
                    self.assets["long_fruits"][int(fruit_name)]["start"] = start_image

                # Load the 'middle' image
                middle_path = os.path.join(fruit_dir, "middle.png")
                if os.path.exists(middle_path):
                    middle_image = pygame.image.load(middle_path).convert_alpha()
                    middle_image = pygame.transform.scale(middle_image,
                                                          (middle_image.get_width() * 4, middle_image.get_height() * 4))
                    self.assets["long_fruits"][int(fruit_name)]["middle"] = middle_image

                # Load the 'end' image
                end_path = os.path.join(fruit_dir, "end.png")
                if os.path.exists(end_path):
                    end_image = pygame.image.load(end_path).convert_alpha()
                    end_image = pygame.transform.scale(end_image,
                                                       (end_image.get_width() * 4, end_image.get_height() * 4))
                    self.assets["long_fruits"][int(fruit_name)]["end"] = end_image

    def load_long_slash(self):
        for i in range(10):
            image = pygame.image.load(f'Animations/Long_fruits/long_slash/{i}.png').convert_alpha()
            self.assets['long_slash'].append(image)

    def load_fruit_images(self):
        # Load fruit images and scale them
        for i in range(1, 229):
            image = pygame.image.load(f'images/fruits/Fruit_{i}.png').convert_alpha()
            image = pygame.transform.scale(image, (image.get_width() * 5, image.get_height() * 5))
            self.assets["fruits"].append(image)

    def load_sliced_fruit_images(self):
        # Load horizontally and vertically sliced fruit images
        sliced_fruits_path = 'images/slashed_fruits'
        for fruit_name in os.listdir(sliced_fruits_path):
            fruit_dir = os.path.join(sliced_fruits_path, fruit_name)
            if os.path.isdir(fruit_dir):
                self.assets["sliced_fruits"][fruit_name] = {"horizontal": [], "vertical": []}

                # Load horizontal slices
                horizontal_dir = os.path.join(fruit_dir, "horizontal")
                if os.path.isdir(horizontal_dir):
                    for image_name in os.listdir(horizontal_dir):
                        image_path = os.path.join(horizontal_dir, image_name)
                        if image_path.endswith(".png"):
                            image = pygame.image.load(image_path).convert_alpha()
                            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
                            self.assets["sliced_fruits"][fruit_name]["horizontal"].append(image)

                # Load vertical slices
                vertical_dir = os.path.join(fruit_dir, "vertical")
                if os.path.isdir(vertical_dir):
                    for image_name in os.listdir(vertical_dir):
                        image_path = os.path.join(vertical_dir, image_name)
                        if image_path.endswith(".png"):
                            image = pygame.image.load(image_path).convert_alpha()
                            image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
                            self.assets["sliced_fruits"][fruit_name]["vertical"].append(image)

    def load_player_animations(self):
        # Load player animations with scaling factor
        self.player_scale = 3

        # Load player idle poses
        for i in range(1, 5):
            image_path = f'Animations/Player/Idle/{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (
                image.get_width() * self.player_scale, image.get_height() * self.player_scale))
            self.assets["player"]["idle"].append(scaled_image)

        # Load player attack 17 poses
        for i in range(1, 5):
            image_path = f'Animations/Player/Attack 1/{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (
                image.get_width() * self.player_scale, image.get_height() * self.player_scale))
            self.assets["player"]["attack_1"].append(scaled_image)

        # Load player attack 18 poses
        for i in range(1, 5):
            image_path = f'Animations/Player/Attack 2/{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (
                image.get_width() * self.player_scale, image.get_height() * self.player_scale))
            self.assets["player"]["attack_2"].append(scaled_image)

        for i in range(1, 4):
            image_path = f'Animations/Player/Take hit/{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (
                image.get_width() * self.player_scale, image.get_height() * self.player_scale))
            self.assets["player"]["take_hit"].append(scaled_image)

        for i in range(1, 8):
            image_path = f'Animations/Player/Death/{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (
                image.get_width() * self.player_scale, image.get_height() * self.player_scale))
            self.assets["player"]["death"].append(scaled_image)

    def load_sounds(self):
        # Load sword attack sounds
        for i in range(1, 5):
            hit_sound = pygame.mixer.Sound(f'audio/sword_attacks/sword_attack_{i}.mp3')
            hit_sound.set_volume(0.5)  # Set volume to 50%
            self.assets["sounds"]["sword_attacks"].append(hit_sound)

        # Load fruit slashed sounds
        for i in range(1, 4):
            hit_sound = pygame.mixer.Sound(f'audio/fruit_slashed/{i}.mp3')
            hit_sound.set_volume(0.5)  # Set volume to 50%
            self.assets["sounds"]["fruit_slashed"].append(hit_sound)

        for i in range(1, 8):
            got_hit_sound = pygame.mixer.Sound(f'audio/player_hit/{i}.mp3')
            self.assets["sounds"]["player_hit"].append(got_hit_sound)

        for i in range(1, 3):
            sound = pygame.mixer.Sound(f'audio/flame_trailing/{i}.mp3')
            self.assets["sounds"]["flame_trailing"].append(sound)

        for i in range(1, 8):
            sound = pygame.mixer.Sound(f'audio/rankings/{i}.mp3')
            self.assets["sounds"]["rankings"].append(sound)

        sound = pygame.mixer.Sound(f'audio/slow_motion.wav')
        self.assets["sounds"]["slow_motion"] = sound

        sound = pygame.mixer.Sound(f'audio/scores/PersonalRecord.wav')
        self.assets["sounds"]["scores"]['personal_record'] = sound
        sound = pygame.mixer.Sound(f'audio/scores/WorldRecord.wav')
        self.assets["sounds"]["scores"]['world_record'] = sound

        sound = pygame.mixer.Sound(f'audio/checkpoint.mp3')
        self.assets["sounds"]["checkpoint"] = sound

        sound = pygame.mixer.Sound(f'audio/slam.mp3')
        self.assets["sounds"]["slam"] = sound

    def load_fruit_death_animations(self):
        # Load Sparks 17 death animation
        sparks1_animation = []
        for i in range(1, 31):
            image_path = f'Animations/Fruits/Deaths/Sparks 1/{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (
                image.get_width() * 2, image.get_height() * 2))
            sparks1_animation.append(scaled_image)
        self.assets["fruit_deaths"]["sparks1"] = sparks1_animation

        # Load Sparks 18 death animation
        sparks2_animation = []
        for i in range(1, 7):
            image_path = f'Animations/Fruits/Deaths/Sparks 2/{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (
                image.get_width() * 2, image.get_height() * 2))
            sparks2_animation.append(scaled_image)
        self.assets["fruit_deaths"]["sparks2"] = sparks2_animation

        # Load Splatter death animation
        splatter_animation = []
        for i in range(1, 31):
            image_path = f'Animations/Fruits/Deaths/Splatter/{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (
                image.get_width() * 2, image.get_height() * 2))
            splatter_animation.append(scaled_image)
        self.assets["fruit_deaths"]["splatter"] = splatter_animation

    def load_trailing_slash_animations(self):
        for i in range(1, 7):
            image_path = f'Animations/Player/Flame Trailing/{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
            self.assets["player"]["trailing_slash"].append(scaled_image)

    def load_star_checkpoint_animation(self):
        for i in range(1, 14):
            image_path = f'Animations/Star/{i}.png'
            image = pygame.image.load(image_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
            self.assets["star"].append(scaled_image)
