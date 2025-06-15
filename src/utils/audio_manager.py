import pygame
from collections import OrderedDict

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = OrderedDict()
        self.sound_paths = {
            "move": "src/audio/move.ogg",
            "select": "src/audio/menu_confirm.ogg",
            "level_won": "src/audio/level_won.ogg",
            "barrel_ready": "src/audio/barrel_ready_effect.ogg",
            "menu_select":  "src/audio/menu_select.ogg",
            "level_select": "src/audio/level_select.ogg"
        }
        self.music = {}
        self.music_paths = {
            "menu": "src/audio/menu_music.ogg",
            "level": "src/audio/level_music.ogg"
        }
        self._load_all_sounds()
        self._load_music()
        # self.cache_size = cache_size

    def _load_all_sounds(self):
        """Load all sounds at once"""
        for name, path in self.sound_paths.items():
            try:
                sound = pygame.mixer.Sound(path)
                sound.set_volume(0.2)
                self.sounds[name] = sound
            except pygame.error as e:
                print(f"Could not load sound {path}: {e}")
                self.sounds[name] = None

    def play_sound(self, name):
        """Play a sound if it exists"""
        if name in self.sounds and self.sounds[name]:
            self.sounds[name].play()

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