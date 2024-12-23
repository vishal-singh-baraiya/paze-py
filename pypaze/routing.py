import os
import importlib.util
from flask import request

def register_routes(app, base_path):
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                relative_path = os.path.relpath(os.path.join(root, file), base_path)
                module_path = os.path.join(root, file).replace("/", ".").replace("\\", ".").replace(".py", "")

                # Generate the route path
                route = "/" + relative_path.replace("\\", "/").replace(".py", "")
                route = route.replace("index", "").replace("/_", "/").replace("_", "").replace("[", "<").replace("]", ">")
                if "[...]" in route:
                    route = route.replace("[...<", "<").replace(">", ":path>")

                # Dynamically load the route module
                spec = importlib.util.spec_from_file_location(module_path, os.path.join(root, file))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Register the route
                if hasattr(module, "handler"):
                    methods = getattr(module, "methods", ["GET"])
                    middleware = getattr(module, "middleware", [])

                    # Middleware wrapper
                    def wrap_handler(handler, middleware):
                        def wrapped_handler(*args, **kwargs):
                            for mw in middleware:
                                mw_response = mw(request)
                                if mw_response:
                                    return mw_response
                            return handler(*args, **kwargs)
                        return wrapped_handler

                    endpoint = module_path.replace(".", "_")
                    app.route(route, methods=methods, endpoint=endpoint)(
                        wrap_handler(module.handler, middleware)
                    )

                print(f"Registered route: {route}")
