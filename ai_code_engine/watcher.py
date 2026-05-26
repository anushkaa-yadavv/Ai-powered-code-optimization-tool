from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from ai_code_engine.engine import process_file

import time


class Watcher(FileSystemEventHandler):

    def on_modified(self, event):

        if event.src_path.endswith(".py"):

            with open(event.src_path, "r", encoding="utf-8") as f:
                code = f.read()

            result = process_file(code, event.src_path)

            print(result)


observer = Observer()
observer.schedule(Watcher(), path=".", recursive=True)
observer.start()

print("Watching files...")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()