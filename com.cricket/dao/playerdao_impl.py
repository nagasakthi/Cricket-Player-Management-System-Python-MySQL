from dao.playerdao import PlayerDAO
from util.db_connection import get_connection
from model.player import Player

class PlayerDAOImpl(PlayerDAO):
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
    
    def add_player(self, player):

        sql = "INSERT INTO cricketplayers(PlayerName,Country,Roles,BattingStyle,BowlingStyle,MatchesPlayed,Runs,Wickets) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (player.name, player.country,player.role,player.BattingStyle,player.BowlingStyle,player.matches, player.runs, player.wickets, )
        self.cursor.execute(sql, values)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def get_all_players(self):

        self.cursor.execute("SELECT * FROM cricketplayers")
        rows = self.cursor.fetchall()
        players = []
        for row in rows:
            player = Player(*row)  # exclude CreatedAt
            players.append(player)
        
        self.cursor.close()
        self.conn.close()
        return players

    def get_player_by_id(self, player_id):
        self.cursor.execute("SELECT * FROM cricketplayers WHERE playerid = %s", (player_id,))
        row = self.cursor.fetchone()
        if row:
            return Player(*row)
        return None
        
    def update_player(self, player):
        sql = "UPDATE cricketplayers SET Runs = %s, Wickets = %s WHERE playerid = %s"
        values = (player.runs, player.wickets, player.player_id)
        self.cursor.execute(sql, values)
        self.conn.commit()



    def delete_player(self, player_id):
        self.cursor.execute("DELETE FROM cricketplayers WHERE playerid = %s", (player_id,))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()