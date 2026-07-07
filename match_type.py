from shootout import shootout
from tournament_mode import tournament


def match_type_query():
    while True:
        choice = input(
            "\nMatch Type\n"
            "S = Quick Match\n"
            "T = Tournament\n"
            "Enter choice: "
        ).upper().strip()

        if choice == "S":
            print("\nYou have chosen a quick match.")
            shootout()
            return

        if choice == "T":
            print("\nYou have chosen a tournament.")
            tournament()
            return

        print("❌ Please enter S or T.")