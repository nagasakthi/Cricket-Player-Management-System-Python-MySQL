 from abc import ABC, abstractmethod

class PlayerDAO(ABC):
    
    @abstractmethod
    def add_player(self, player):
        pass

    @abstractmethod
    def get_all_players(self):
        pass

    @abstractmethod
    def get_player_by_id(self, player_id):
        pass

    @abstractmethod
    def update_player(self, player):
        pass

    @abstractmethod
    def delete_player(self, player_id):
        pass