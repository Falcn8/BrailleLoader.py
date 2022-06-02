try:
    import os
    import time
    braille = ['⠟', '⠯', '⠷', '⠾', '⠽', '⠻']
    os.system("clear")
    while True:
        for i in braille:
            print(i+" ➜ Loading")
            time.sleep(0.12)
            print("\033[H", end="")
except KeyboardInterrupt:
    exit()
