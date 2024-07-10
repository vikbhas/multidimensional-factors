class PlayerPerformance:
    def __init__(self, goals_scored, assists, shots_on_target, pass_accuracy, key_passes,
                 tackles, interceptions, clearances, blocks, defensive_errors,
                 saves, clean_sheets, goals_conceded, penalty_saves,
                 possession_percentage, team_passing_accuracy, team_shots_on_target, fouls_committed, corners_won,
                 yellow_cards, red_cards, fouls):
        self.goals_scored = goals_scored
        self.assists = assists
        self.shots_on_target = shots_on_target
        self.pass_accuracy = pass_accuracy
        self.key_passes = key_passes
        self.tackles = tackles
        self.interceptions = interceptions
        self.clearances = clearances
        self.blocks = blocks
        self.defensive_errors = defensive_errors
        self.saves = saves
        self.clean_sheets = clean_sheets
        self.goals_conceded = goals_conceded
        self.penalty_saves = penalty_saves
        self.possession_percentage = possession_percentage
        self.team_passing_accuracy = team_passing_accuracy
        self.team_shots_on_target = team_shots_on_target
        self.fouls_committed = fouls_committed
        self.corners_won = corners_won
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.fouls = fouls

    def normalize(self, value, max_value):
        return value / max_value if max_value != 0 else 0

    def offensive_score(self):
        weights = {'goals_scored': 0.25, 'assists': 0.2, 'shots_on_target': 0.15, 'pass_accuracy': 0.2, 'key_passes': 0.2}
        normalized_values = {metric: self.normalize(getattr(self, metric), max_value)
                             for metric, max_value in zip(weights.keys(), [5, 5, 10, 100, 10])}
        return sum(normalized_values[metric] * weight for metric, weight in weights.items())

    def defensive_score(self):
        weights = {'tackles': 0.2, 'interceptions': 0.2, 'clearances': 0.2, 'blocks': 0.2, 'defensive_errors': 0.2}
        normalized_values = {metric: self.normalize(getattr(self, metric), max_value)
                             for metric, max_value in zip(weights.keys(), [10, 10, 10, 5, 5])}
        return sum(normalized_values[metric] * weight for metric, weight in weights.items())

    def goalkeeping_score(self):
        weights = {'saves': 0.3, 'clean_sheets': 0.3, 'goals_conceded': 0.2, 'penalty_saves': 0.2}
        normalized_values = {metric: self.normalize(getattr(self, metric), max_value)
                             for metric, max_value in zip(weights.keys(), [10, 5, 10, 5])}
        return sum(normalized_values[metric] * weight for metric, weight in weights.items())

    def team_score(self):
        weights = {'possession_percentage': 0.25, 'team_passing_accuracy': 0.25, 'team_shots_on_target': 0.2, 'fouls_committed': 0.15, 'corners_won': 0.15}
        normalized_values = {metric: self.normalize(getattr(self, metric), max_value)
                             for metric, max_value in zip(weights.keys(), [100, 100, 10, 20, 10])}
        return sum(normalized_values[metric] * weight for metric, weight in weights.items())

    def disciplinary_score(self):
        weights = {'yellow_cards': -0.1, 'red_cards': -0.3, 'fouls': -0.1}
        normalized_values = {metric: self.normalize(getattr(self, metric), max_value)
                             for metric, max_value in zip(weights.keys(), [5, 1, 20])}
        return sum(normalized_values[metric] * weight for metric, weight in weights.items())

    def final_performance_score(self):
        return (self.offensive_score() + self.defensive_score() + self.goalkeeping_score() +
                self.team_score() + self.disciplinary_score())

# Example usage
player = PlayerPerformance(goals_scored=3, assists=2, shots_on_target=5, pass_accuracy=85, key_passes=4,
                           tackles=6, interceptions=3, clearances=5, blocks=2, defensive_errors=1,
                           saves=0, clean_sheets=0, goals_conceded=0, penalty_saves=0,
                           possession_percentage=55, team_passing_accuracy=80, team_shots_on_target=7, fouls_committed=15, corners_won=6,
                           yellow_cards=1, red_cards=0, fouls=3)

print("Final Performance Score:", player.final_performance_score())
