import os
import json
import pygame
from collections import OrderedDict
from src.utils.helper import get_base_path

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = OrderedDict()
        self.music = {}
        self.settings_path = get_base_path("settings.json")
        self.sound_enabled = self._load_audio_setting()

        self._load_all_sounds()
        self._load_music()

        if not self.sound_enabled:
            for sound in self.sounds.values():
                if isinstance(sound, pygame.mixer.Sound):
                    sound.set_volume(0)

    def _load_audio_setting(self):
        try:
            if os.path.exists(self.settings_path):
                with open(self.settings_path, "r") as f:
                    settings = json.load(f)
                    return settings.get("audio_on", True)
        except Exception as e:
            print(f"Error loading audio setting: {e}")
        return True

    def _save_audio_setting(self):
        try:
            settings = {"audio_on": self.sound_enabled}
            with open(self.settings_path, "w") as f:
                json.dump(settings, f)
        except Exception as e:
            print(f"Error saving audio setting: {e}")

    def _load_all_sounds(self):
        """Load all sound effects into memory."""
        base_path = get_base_path("audio")

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

        try:
            # Load each sound file
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

    def _load_music(self):
        base_path = get_base_path("audio")

        # Dictionary to store the music files
        self.music = {
            "menu": os.path.join(base_path, "menu_music.ogg"),
            "level": os.path.join(base_path, "level_music.ogg")
        }

        try:
            # Load each music file
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

    def play_sound(self, name):
        """Play a sound if it exists"""
        if name in self.sounds and self.sounds[name]:
            self.sounds[name].play()

    def play_music(self, name, loop=-1):
        if name in self.music and self.sound_enabled:
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

    def toggle_audio(self, enabled):
        """Toggle all audio on/off"""
        self.sound_enabled = enabled
        self._save_audio_setting()
        if enabled:
            self.unpause_music()
            for sound in self.sounds.values():
                if isinstance(sound, pygame.mixer.Sound):
                    sound.set_volume(0.2)
        else:
            self.pause_music()
            for sound in self.sounds.values():
                if isinstance(sound, pygame.mixer.Sound):
                    sound.set_volume(0)
