import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music = {}

        self.load_sounds()
        self.load_music()

    def load_sounds(self):
        self.sounds["move"] = self._load_sound("src/audio/move1_1.wav")
        self.sounds["select"] = self._load_sound("src/audio/select2.wav")
        self.sounds["level_won"] = self._load_sound("src/audio/level_won.wav")
        # Add more sounds here

    def load_music(self):
        self.music["menu"] = self._load_music("src/audio/menu_music2.mp3")
        self.music["level"] = self._load_music("src/audio/level_music.mp3")
        # Add more music here

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
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.play(loop)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()