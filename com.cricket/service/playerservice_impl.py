from service.playerservice import PlayerService
from dao.playerdao_impl import PlayerDAOImpl
from model.player import Player

class PlayerServiceImpl(PlayerService):

    def __init__(self):

        self.dao = PlayerDAOImpl()

    def add_player(self, player=None):
        name = input("Name: ")
        country = input("Country: ")
        role = input("Role: ")
        BattingStyle=input("BattingStyle:")
        BowlingStyle=input("BowlingStyle:")
        matches = int(input("Matches Played: "))
        runs = int(input("Runs: "))
        wickets = int(input("Wickets: "))
        player = Player(name=name,country=country,role=role,BattingStyle=BattingStyle,BowlingStyle=BowlingStyle,matches=matches,runs=runs,wickets=wickets)
        self.dao.add_player(player)
        print(" Successfully Added Player!")
        
    def list_players(self):
        players = self.dao.get_all_players() # when i try to print a players but i'am used in wrong place , correct place is players= self.dao.get_all_players
        print("\nAll Players:")
        for p in players:
            print(p)

    def update_player_stats(self):  #,player_id, runs, wickets
        player_id = int(input("Enter Player ID to update: "))
        runs = int(input("Enter new Runs: "))
        wickets = int(input("Enter new Wickets: "))        

        player = self.dao.get_player_by_id(player_id)
        
        if player:
            player.runs = runs
            player.wickets = wickets
            self.dao.update_player(player)
            print("Player stats updated successfully!")
            return True
        else:
            print("Player not found.")
            return False

    def remove_player(self): #player_id
        player_id = int(input("Enter Player ID to delete: "))
        player = self.dao.get_player_by_id(player_id)
        if player:
            self.dao.delete_player(player_id)
            print("Player deleted successfully!")
        else:
            print("Player not found.")
            return True
        return False