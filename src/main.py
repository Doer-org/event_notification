import sys
import settings
from hello import print_hello
from discord_bot import call_discord_bot

# main関数
def main():
    if len(sys.argv) > 1 and sys.argv[1] == "hello":
        print_hello()
        return

    # discord_bot.py の関数を呼び出す

if __name__ == "__main__":
    main()
