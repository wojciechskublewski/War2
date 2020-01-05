from models import User
import argparse
from clcrypto import check_password
from database import get_connection, get_cursor

parser = argparse.ArgumentParser(description="Opis naszej aplikacji")
parser.add_argument('-u', '--user', type=str, help="Pomoc komendy. Użycie -u login")
parser.add_argument('-p', '--password', type=str, help="Pomoc komendy. Użycie -p hasło")
parser.add_argument('-a', '--aaa', type=str, help="Pomoc komendy. Użycie -p hasło")

args = parser.parse_args()

if __name__ == '__main__':
    connection = get_connection()
    cursor = get_cursor(connection)

    if args.user and args.password:
        print(f"Podany login: {args.user} a podane hasło to: {args.password}")

        loaded_user = User.load_user_by_username(cursor, args.user)
        if loaded_user and check_password(args.password, loaded_user.hashed_password):
            print("Poprawne dane")
        else:
            print("Błędne dane")

    connection.close()
