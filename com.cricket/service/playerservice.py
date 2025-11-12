from abc import ABC, abstractmethod

class PlayerService(ABC):

    @abstractmethod
    def add_player(self, player):
        pass

    @abstractmethod
    def list_players(self):
        pass

    @abstractmethod
    def update_player_stats(self, player_id, runs, wickets):
        pass

    @abstractmethod
    def remove_player(self, player_id):
        pass