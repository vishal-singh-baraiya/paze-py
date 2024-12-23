from flask import Flask
from .routing import register_routes
from .middleware import apply_global_middleware
from .utils import enable_hot_reload
import os

def create_app(
    base_path="routes",
    static_folder="static",
    template_folder="templates",
    enable_hot_reload=False
):
    # Create the Flask app with explicit static and template folder paths
    app = Flask(
        __name__,
        static_folder=os.path.abspath(static_folder),
        template_folder=os.path.abspath(template_folder),
    )

    # Dynamically register routes from the base_path
    register_routes(app, base_path=os.path.abspath(base_path))

    # Apply global middleware
    apply_global_middleware(app)

    # Enable hot reloading (if requested)
    if enable_hot_reload:
        enable_hot_reload(app, watch_path=base_path)

    # Add a default 404 handler
    @app.errorhandler(404)
    def page_not_found(e):
        return {"error": "Not Found"}, 404

    # Add a 500 error handler with template-specific debugging
    @app.errorhandler(500)
    def server_error(e):
        from jinja2.exceptions import TemplateNotFound
        if isinstance(e.original_exception, TemplateNotFound):
            return {"error": f"Template '{e.original_exception.name}' not found"}, 500
        return {"error": "Internal Server Error"}, 500

    return app
