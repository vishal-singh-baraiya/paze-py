from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RouteChangeHandler(FileSystemEventHandler):
    def __init__(self, app):
        self.app = app

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"Route changed: {event.src_path}. Reloading routes...")
            with self.app.app_context():
                self.app.url_map._rules.clear()
                from .routing import register_routes
                register_routes(self.app)

def enable_hot_reload(app, watch_path):
    observer = Observer()
    handler = RouteChangeHandler(app)
    observer.schedule(handler, path=watch_path, recursive=True)
    observer.start()
    print("Hot-reloading enabled for routes.")
