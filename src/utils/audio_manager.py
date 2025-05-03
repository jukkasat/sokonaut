import pygame
from collections import OrderedDict

class AudioManager:
    def __init__(self, cache_size=5):
        pygame.mixer.init()
        self.sounds = OrderedDict()
        self.music = {}
        self.sound_paths = {
            "move": "src/audio/move.ogg",
            "select": "src/audio/menu_confirm.ogg",
            "level_won": "src/audio/level_won.ogg",
            "barrel_ready": "src/audio/barrel_ready_effect.ogg",
            "menu_select":  "src/audio/menu_select.ogg",
            "level_select": "src/audio/level_select.ogg"
        }
        self.music_paths = {
            "menu": "src/audio/menu_music.ogg",
            "level": "src/audio/level_music.ogg"
        }
        self._load_music()
        self.cache_size = cache_size

    def _load_sound(self, path):
        try:
            sound = pygame.mixer.Sound(path)
            sound.set_volume(0.2)
            return sound
        except pygame.error as e:
            print(f"Could not load sound {path}: {e}")
            return None

    def play_sound(self, name):
        if name in self.sound_paths:
            if name not in self.sounds:
                # Load the sound if it's not already loaded
                sound = self._load_sound(self.sound_paths[name])
                self.sounds[name] = sound
            else:
                # Move the sound to the end of the ordered dict to mark it as recently used
                self.sounds.move_to_end(name)

            if self.sounds[name]:
                self.sounds[name].play()
                self._manage_cache()

    def _manage_cache(self):
        """Remove the least recently used sound if the cache is full"""
        if len(self.sounds) > self.cache_size:
            # Get the least recently used sound (the first item in the ordered dict)
            lru_sound_name, lru_sound = self.sounds.popitem(last=False)
            print(f"Unloading sound: {lru_sound_name}")
            del lru_sound  # Remove the sound from memory

    def _load_music(self):
        try:
            for name, path in self.music_paths.items():
                pygame.mixer.music.load(path)
                pygame.mixer.music.set_volume(0.1)
                self.music[name] = path  # Store the loaded music
        except pygame.error as e:
            print(f"Could not load music: {e}")

    def play_music(self, name, loop=-1):
        if name in self.music:
            if pygame.mixer.music.get_busy():  # Check if music is already playing
                pygame.mixer.music.stop()  # Stop the current music
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.play(loop)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()