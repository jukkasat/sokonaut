import json
import os

class HighScores:
    def __init__(self):
        self.scores = []
        self.score_file = "highscores.json"
        self.load_scores()

    def load_scores(self):
        try:
            if os.path.exists(self.score_file):
                with open(self.score_file, 'r') as f:
                    self.scores = json.load(f)
            else:
                self.scores = []
        except:
            self.scores = []

    def save_scores(self):
        with open(self.score_file, 'w') as f:
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