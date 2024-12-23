from flask import request

def apply_global_middleware(app):
    @app.before_request
    def log_request():
        print(f"Request: {request.method} {request.path}")
