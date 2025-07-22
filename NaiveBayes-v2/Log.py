import datetime

class Logger:
    print = True

    @staticmethod
    def log(text):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"{now} : {text}"
        if Logger.print:
            print(f"\033[92m{message}\033[0m")
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(message + "\n")

def log(text):
    Logger.log(text)
