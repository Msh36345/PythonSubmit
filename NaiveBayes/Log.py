class Logger:
    enabled = True

    @staticmethod
    def print(text):
        if Logger.enabled:
            print(f"\033[92m{text}\033[0m")

def log(text):
    Logger.print(text)


