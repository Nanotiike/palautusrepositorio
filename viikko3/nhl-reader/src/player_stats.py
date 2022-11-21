from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = []

        for player_dict in self.reader.response:
            player = Player(
                player_dict['name'], player_dict['nationality'], player_dict['team'], player_dict['goals'], player_dict['assists']
            )

            self.players.append(player)

    def top_scorers_by_nationality(self, nationality):
        top_scores = []
        for player in self.players:
            if player.nationality == nationality:
                top_scores.append(player)
        
        top_scores.sort(key=lambda x: x.goals+x.assists, reverse=True)

        return(top_scores)