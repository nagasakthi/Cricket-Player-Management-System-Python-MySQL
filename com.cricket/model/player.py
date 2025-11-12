class Player:
    def __init__(self, player_id=None, name="",country="",role="",BattingStyle="",BowlingStyle="", matches=0, runs=0, wickets=0):
        self.player_id = player_id
        self.name = name
        self.country = country
        self.role = role
        self.BattingStyle = BattingStyle
        self.BowlingStyle = BowlingStyle
        self.matches = matches
        self.runs = runs
        self.wickets = wickets
       

    def __str__(self):
        return f" Player_id : {self.player_id} | Name : {self.name} | Country : {self.country} | Role : {self.role} | BattingStyle : {self.BattingStyle} | BowlingStyle : {self.BowlingStyle} | Matches: {self.matches} | Runs: {self.runs} | Wickets: {self.wickets} "


