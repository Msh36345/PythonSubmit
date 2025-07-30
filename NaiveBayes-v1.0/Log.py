import datetime

class Logger:
    printed = True

    @staticmethod
    def log(text):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{now}] {text}"
        for i in range(len(message) // 130):
            split_index = message.find(" ", 130 * (i + 1))
            message = message[:split_index] + "\n" + message[split_index + 1:]

        if Logger.printed:
            print(f"\033[92m{message}\033[0m")
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(message + "\n")

def log(text):
    Logger.log(text)