from service.playerservice_impl import PlayerServiceImpl
from model.player import Player

service = PlayerServiceImpl()

def menu():
    while True:
        print("\n CRICKET MANAGEMENT SYSTEM")
        print("1. Add Player")
        print("2. View All Players")
        print("3. Update Player Stats")
        print("4. Delete Player")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            service.add_player()
            break

        elif choice == '2':
            service.list_players()
            break

        elif choice == '3':
            service.update_player_stats()
            break

        elif choice == '4':
            service.remove_player()
            break

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()

