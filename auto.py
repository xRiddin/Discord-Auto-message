import json
import sys
import random
import time
from datetime import datetime
from http.client import HTTPSConnection

INFO_FILE = "info.txt"
MESSAGES_FILE = "messages.txt"


def get_timestamp():
    """
    Returns a timestamp in the format YYYY-MM-DD HH:MM:SS
    """
    return "[" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "]"


def random_sleep(duration, min_random, max_random):
    sleep_duration = duration + random.randint(min_random, max_random)
    print(f"{get_timestamp()} Sleeping for {sleep_duration} seconds")

    time.sleep(sleep_duration)


def read_info():
    try:
        with open(INFO_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"{get_timestamp()} Info file not found.")
        return None


def write_info(user_id, token, channel_url, channel_id):
    try:
        with open(INFO_FILE, "w") as file:
            file.write(f"{user_id}\n{token}\n{channel_url}\n{channel_id}")
    except Exception as e:
        print(f"{get_timestamp()} Error configuring user information: {e}")
        exit()


def configure_info():
    try:
        user_id = input("User-ID: ")
        token = input("Discord token: ")
        channel_url = input("Discord channel URL: ")
        channel_id = input("Discord channel ID: ")
        write_info(user_id, token, channel_url, channel_id)
        print(f"Written config to info.txt, please rerun to start!")
    except Exception as e:
        print(f"{get_timestamp()} Error configuring user information: {e}")
        exit()


def set_channel():
    info = read_info()
    if info:
        user_id, token, _, _ = info
        channel_url = input("Discord channel URL: ")
        channel_id = input("Discord channel ID: ")
        write_info(user_id, token, channel_url, channel_id)
        print(f"Written config to info.txt, please rerun to start!")


def show_help():
    print("Showing help for discord-auto-messenger")
    print("Usage:")
    print("  'python3 auto.py'               :  Runs the automessenger. Type in the wait time and take a back seat.")
    print("  'python3 auto.py --config'      :  Configure settings.")
    print("  'python3 auto.py --setC'  :  Set channel to send message to. Including Channel ID and Channel URL")
    print("  'python3 auto.py --help'        :  Show help")


def send_message(conn, channel_id, message_data, header_data):
    try:
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data)
        resp = conn.getresponse()
        if 199 < resp.status < 300:
            print(f"{get_timestamp()} Message {message_data} sent!")
    except Exception as e:
        print(f"{get_timestamp()} Error sending message: {e} | {message_data}")


def get_connection():
    return HTTPSConnection("discordapp.com", 443)


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--config" and input("Configure? (y/n)") == "y":
            configure_info()
            return
        elif sys.argv[1] == "--setC" and input("Set channel? (y/n)") == "y":
            set_channel()
            return
        elif sys.argv[1] == "--help":
            show_help()
            return

    info = read_info()
    if not info or len(info) != 4:
        print(
            f"{get_timestamp()} An error was found inside the user information file. Please ensure the file contains "
            f"the following information in order: User agent, Discord token, Discord channel URL, and Discord channel "
            f"ID. Try again with python3 auto.py"
        )
        configure_info()
        return

    header_data = {
        "content-type": "application/json",
        "user-id": info[0],
        "authorization": info[1],
        "host": "discordapp.com",
        "referrer": info[2]
    }

    print(f"{get_timestamp()} Messages will be sent to " + header_data["referrer"] + ".")

    print("Please initialise your delays and sleep time, there will be some random offsets applied as well!\n")
    delay_between_messages = int(input("Delay (in seconds) between messages: "))
    sleep_time = int(input("Sleep time (in seconds): "))

    while True:
        try:
            with open(MESSAGES_FILE, "r") as file:
                messages = file.read().splitlines()
        except FileNotFoundError:
            print(f"{get_timestamp()} Messages file not found.")
            return

        for message in messages:
            message_data = json.dumps({"content": message})
            conn = get_connection()
            send_message(conn, info[3], message_data, header_data)
            conn.close()

            random_sleep(delay_between_messages, 1, 10)

        print(f"{get_timestamp()} Finished sending all messages!")
        random_sleep(sleep_time, 20, 1200)


if __name__ == "__main__":
    main()
