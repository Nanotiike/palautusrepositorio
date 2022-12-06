class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0 
        self.player2_score = 0 

    def won_point(self, player_name): 
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.tie_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.endgame_score()
        else:
            score = self.earlygame_score()

        return score

    def tie_score(self):    
        result = {
            0 : "Love-All",
            1 : "Fifteen-All",
            2 : "Thirty-All",
            }.get(self.player1_score, "Deuce")

        return result

    def endgame_score(self):
        minus_result = self.player1_score - self.player2_score

        if minus_result == 1:
            return "Advantage " + self.player1_name
        elif minus_result == -1:
            return "Advantage " + self.player2_name
        elif minus_result >= 2:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name

    def earlygame_score(self):
        temp_score = 0
        result = ""
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                result = result + "-"
                temp_score = self.player2_score

            result += {
                0 : "Love",
                1 : "Fifteen",
                2 : "Thirty",
                3 : "Forty",
                }[temp_score]
        return result