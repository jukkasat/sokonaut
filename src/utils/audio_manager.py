import os
import sys
import pygame
from collections import OrderedDict

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = OrderedDict()
        self.music = {}
        self.sound_enabled = True
        self._load_all_sounds()
        self._load_music()

    def _load_all_sounds(self):
        """Load all sound effects into memory."""
        base_path = self._get_base_path()

        # Dictionary to store our sound effects
        self.sounds = {
            'move': os.path.join(base_path, "move.ogg"),
            'level_select': os.path.join(base_path, "level_select.ogg"),
            'level_won': os.path.join(base_path, "level_won.ogg"),
            'menu_select': os.path.join(base_path, "menu_select.ogg"),
            'select': os.path.join(base_path, "menu_confirm.ogg"),
            'barrel_ready': os.path.join(base_path, "barrel_ready_effect.ogg"),
            'level_select': os.path.join(base_path, "level_select.ogg")
        }

        # Load each sound file
        try:
            for sound_name, path in self.sounds.items():
                if os.path.exists(path):
                    self.sounds[sound_name] = pygame.mixer.Sound(path)
                    self.sounds[sound_name].set_volume(0.2)
                else:
                    print(f"Warning: Sound file not found: {path}")
        except Exception as e:
            print(f"Error loading sounds: {str(e)}")
            # Initialize with None if loading fails
            self.sounds = {name: None for name in self.sounds}


    def play_sound(self, name):
        """Play a sound if it exists"""
        if name in self.sounds and self.sounds[name]:
            self.sounds[name].play()

    def _load_music(self):
        base_path = self._get_base_path()

        # Dictionary to store the music files
        self.music = {
            "menu": os.path.join(base_path, "menu_music.ogg"),
            "level": os.path.join(base_path, "level_music.ogg")
        }

        # Load each music file
        try:
            for name, path in self.music.items():
                if os.path.exists(path):
                    self.music[name] = pygame.mixer.music.load(path)
                    pygame.mixer.music.set_volume(0.1)
                    self.music[name] = path
                else:
                    print(f"Warning: Sound file not found: {path}")
        except Exception as e:
            print(f"Error loading sounds: {str(e)}")
            # Initialize with None if loading fails
            self.sounds = {name: None for name in self.sounds}

    def play_music(self, name, loop=-1):
        if name in self.music and self.sound_enabled:
            if pygame.mixer.music.get_busy():  # Check if music is already playing
                pygame.mixer.music.stop()  # Stop the current music
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.play(loop)

    def toggle_audio(self, enabled):
        """Toggle all audio on/off"""
        self.sound_enabled = enabled
        if enabled:
            self.unpause_music()
            # Reset all sound volumes
            for sound in self.sounds.values():
                if isinstance(sound, pygame.mixer.Sound):
                    sound.set_volume(0.2)
        else:
            self.pause_music()
            # Mute all sounds
            for sound in self.sounds.values():
                if isinstance(sound, pygame.mixer.Sound):
                    sound.set_volume(0)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def _get_base_path(self):
        """Helper method to determine the correct image directory path"""
        if hasattr(sys, '_MEIPASS'):  # Running as PyInstaller bundle
            return os.path.join(sys._MEIPASS, "src", "audio")
        return os.path.join(os.path.dirname(__file__), "..", "audio") # Running in development