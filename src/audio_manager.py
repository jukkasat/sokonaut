import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music = {}

        self.load_sounds()
        self.load_music()

    def load_sounds(self):
        self.sounds["move"] = self._load_sound("src/audio/move.ogg")
        self.sounds["select"] = self._load_sound("src/audio/menu_confirm.ogg")
        self.sounds["level_won"] = self._load_sound("src/audio/level_won.ogg")
        self.sounds["barrel_ready"] = self._load_sound("src/audio/barrel_ready_effect.ogg")
        self.sounds["menu_select"] = self._load_sound("src/audio/menu_select.ogg")
        self.sounds["level_select"] = self._load_sound("src/audio/level_select.ogg")

    def load_music(self):
        self.music["menu"] = self._load_music("src/audio/menu_music.ogg")
        self.music["level"] = self._load_music("src/audio/level_music.ogg")

    def _load_sound(self, path):
        try:
            sound = pygame.mixer.Sound(path)
            sound.set_volume(0.2)
            return sound
        except pygame.error as e:
            print(f"Could not load sound {path}: {e}")
            return None

    def _load_music(self, path):
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(0.1)
            return path  # Return the path for playing
        except pygame.error as e:
            print(f"Could not load music {path}: {e}")
            return None

    def play_sound(self, name):
        if name in self.sounds and self.sounds[name]:
            self.sounds[name].play()

    def play_music(self, name, loop=-1):
        if name in self.music and self.music[name]:
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