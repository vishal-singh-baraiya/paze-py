# Pypaze

Pypaze is a lightweight, full-stack web framework built on top of Flask, inspired by Next.js. It offers file-based routing, dynamic templates, middleware support, and easy configuration, making it ideal for building modern web applications.

## Features

- **File-based Routing**: Automatically registers routes based on the directory structure, simplifying navigation.

- **Dynamic Routing**: Supports dynamic route parameters and catch-all routes.

- **Middleware**: Add global or route-specific middleware to handle requests.

- **Templating**: Uses Jinja2 for rendering templates.

- **Hot-reloading**: Automatically reloads routes when files are modified during development.

- **CLI**: Comes with a built-in CLI for running the server.

## Installation

To install Pypaze, run:

```
pip install pypaze
```

## Initialize Project

To initialize Pypaze Project, run:

```
pypaze init --project-name project-name
```

## Usage

Create a simple app with Pypaze:

```python
from pypaze import create_app

# Initialize the app
app = create_app()

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
```

## Directory Structure

- `pypaze/`: Contains the framework code.


## Running the App

You can start your app from the command line:

```
python app.py
```

Or use the built-in CLI:

```
pypaze run
```

## License

MIT License. See the [LICENSE](LICENSE) file for details.
