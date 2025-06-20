import os
import json
from src.utils.helper import get_base_path

class Scores:
    def __init__(self):
        self.scores = []
            
        self.score_path = get_base_path("highscores.json")
        self.levels_path = get_base_path("levels_unlocked.json")
        
        self.load_scores()
        self.completed_levels = set()
        self.load_completed_levels()

    def load_scores(self):
        try:
            if os.path.exists(self.score_path):
                with open(self.score_path, 'r') as f:
                    self.scores = json.load(f)
            else:
                self.scores = []
        except:
            self.scores = []

    def save_scores(self):
        with open(self.score_path, 'w') as f:
            json.dump(self.scores, f)

    def add_score(self, name, score):
        self.scores.append({"name": name, "score": score})
        self.scores.sort(key=lambda x: x["score"], reverse=True)
        if len(self.scores) > 10:
            self.scores = self.scores[:10]
        self.save_scores()

    def is_high_score(self, score):
        if len(self.scores) < 10:
            return True
        return score > min(s["score"] for s in self.scores)

    def get_scores(self):
        return self.scores
    
    def load_completed_levels(self):
        try:
            if os.path.exists(self.levels_path):
                with open(self.levels_path, 'r') as f:
                    completed_levels = json.load(f)
                    self.completed_levels = set(int(level) if isinstance(level, str) else level for level in completed_levels)
            else:
                self.completed_levels = set()
        except Exception as e:
            print(f"Error loading completed levels: {e}")

    def save_completed_levels(self):
        try:
            with open(self.levels_path, 'w') as f:
                json.dump(list(self.completed_levels), f)
        except Exception as e:
            print(f"Error saving completed levels: {e}")

    def mark_level_completed(self, level):
        self.completed_levels.add(level)
        self.save_completed_levels()

    def is_level_completed(self, level):
        return level in self.completed_levels

    def is_level_unlocked(self, level):
        return level == 0 or (level - 1) in self.completed_levels or self.is_level_completed(level)