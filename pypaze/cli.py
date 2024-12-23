import click
import os
import shutil
from pathlib import Path
from .app import create_app

@click.group()
def cli():
    """A CLI tool for managing the pypaze framework."""
    pass

@cli.command()
@click.option('--project-name', default='my_project', help='Name of the new project.')
def init(project_name):
    """Initialize a new pypaze project structure."""
    
    # Define the structure
    project_path = Path(project_name)
    
    # Check if the directory already exists
    if project_path.exists():
        print(f"Error: The directory '{project_name}' already exists.")
        return

    # Create basic project structure
    os.makedirs(project_path / "routes")
    os.makedirs(project_path / "static")
    os.makedirs(project_path / "templates")
    

    # Create example files

    
    # Create a basic example app file
    with open(project_path / "app.py", 'w') as f:
        f.write("""from pypaze.app import create_app

app = create_app(
    base_path="routes",
    static_folder="static",
    template_folder="templates",
    enable_hot_reload=True,
)

if __name__ == "__main__":
    app.run(debug=True)""")

    # Create basic index route
    with open(project_path / "routes/index.py", 'w') as f:
        f.write("""from flask import render_template

def handler():
    return render_template("index.html")""")

    # Create basic templates
#     with open(project_path / "templates/layout.html", 'w') as f:
#         f.write("""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{% block title %}My App{% endblock %}</title>
#     <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
# </head>
# <body>
#     <header>
#         <h1>Welcome to My App</h1>
#     </header>
#     <main>
#         {% block content %}{% endblock %}
#     </main>
#     <footer>
#         <p>&copy; 2024 My App</p>
#     </footer>
# </body>
# </html>""")

    with open(project_path / "templates/index.html", 'w') as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PyPaze - Modern Flask Framework</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    
</head>
<body>
    <header>
        <nav>
            <div class="logo">PyPaze</div>
            <div class="nav-links">
                <a href="#features">Features</a>
                <a href="#docs">Documentation</a>
                <a href="https://github.com/vishal-singh-baraiya/pypaze">GitHub</a>
            </div>
        </nav>
    </header>

    <section class="hero">
        <h1>PyPaze Web Framework</h1>
        <p>Experience the power of Next.js features in your Flask applications. Build faster, scale better, and deploy with confidence.</p>
        <a href="#get-started" class="btn">Get Started →</a>
    </section>

    <section class="features" id="features">
        <div class="feature-card">
            <h3>📁 File-based Routing</h3>
            <p>Embrace the simplicity of Next.js-style file-based routing in Flask. Your file structure becomes your routing system, making development intuitive and maintainable.</p>
        </div>
        <div class="feature-card">
            <h3>🔄 Hot Reloading</h3>
            <p>See your changes instantly with advanced hot reloading. No more manual refreshes - watch your application evolve in real-time as you code.</p>
        </div>
        <div class="feature-card">
            <h3>🚀 API Routes</h3>
            <p>Create powerful API endpoints with the same file-based approach. Build full-stack applications with ease using our integrated API routing system.</p>
        </div>
        <div class="feature-card">
            <h3>⚡ Server-side Rendering</h3>
            <p>Get lightning-fast page loads and SEO benefits with built-in SSR support. Deliver optimal user experiences without sacrificing developer productivity.</p>
        </div>
        <div class="feature-card">
            <h3>🏗️ Static Generation</h3>
            <p>Generate static pages at build time for incredible performance. Perfect for landing pages, blogs, and documentation sites.</p>
        </div>
        <div class="feature-card">
            <h3>🛠️ Developer Tools</h3>
            <p>Enhanced debugging, detailed error messages, and comprehensive logging. Develop with confidence using our modern developer tooling.</p>
        </div>
    </section>

    <footer>
        <p>Pypaze - Revolutionizing Flask Development</p>
        <p>Made with ❤️ by TheVixhal</p>
    </footer>

    <script>
        // Intersection Observer for feature cards
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = 1;
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, {
            threshold: 0.1
        });

        // Apply initial styles and observe feature cards
        document.querySelectorAll('.feature-card').forEach((card, index) => {
            card.style.opacity = 0;
            card.style.transform = 'translateY(20px)';
            card.style.transition = `all 0.5s ease-out ${index * 0.1}s`;
            observer.observe(card);
        });

        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    </script>
</body>
</html>""")

    with open(project_path / "static/styles.css", 'w') as f:
        f.write(""":root {
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --accent-primary: #3b82f6;
            --accent-secondary: #60a5fa;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --card-bg: #1e293b;
            --card-hover: #2d3b54;
            --gradient-start: rgba(59, 130, 246, 0.1);
            --gradient-end: rgba(59, 130, 246, 0.05);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Base Styles */
        body {
            font-family: system-ui, -apple-system, sans-serif;
            line-height: 1.6;
            color: var(--text-primary);
            background: var(--bg-primary);
            overflow-x: hidden;
        }

        /* Header & Navigation */
        header {
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(10px);
            padding: 1rem;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid rgba(59, 130, 246, 0.1);
        }

        nav {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: glow 2s ease-in-out infinite alternate;
        }

        .nav-links a {
            color: var(--text-primary);
            text-decoration: none;
            margin-left: 2rem;
            position: relative;
            transition: color 0.3s;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: -4px;
            left: 0;
            background: var(--accent-primary);
            transition: width 0.3s;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* Hero Section */
        .hero {
            background: radial-gradient(circle at top right, 
                                    var(--gradient-start), 
                                    var(--gradient-end));
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 8rem 2rem 4rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            width: 200%;
            height: 200%;
            background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%233b82f6' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            animation: backgroundScroll 60s linear infinite;
            opacity: 0.5;
        }

        .hero h1 {
            font-size: 4rem;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: titleReveal 1s ease-out;
        }

        .hero p {
            font-size: 1.25rem;
            color: var(--text-secondary);
            max-width: 600px;
            margin: 0 auto 2rem;
            animation: fadeUp 1s ease-out 0.5s both;
        }

        .btn {
            display: inline-block;
            padding: 1rem 2rem;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            color: var(--text-primary);
            text-decoration: none;
            border-radius: 0.5rem;
            font-weight: bold;
            position: relative;
            overflow: hidden;
            transition: transform 0.3s;
            animation: fadeUp 1s ease-out 1s both;
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: 0.5s;
        }

        .btn:hover {
            transform: translateY(-2px);
        }

        .btn:hover::before {
            left: 100%;
        }

        /* Features Section */
        .features {
            max-width: 1200px;
            margin: 4rem auto;
            padding: 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .feature-card {
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, 
                                    rgba(59, 130, 246, 0.1), 
                                    transparent);
            opacity: 0;
            transition: opacity 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            background: var(--card-hover);
        }

        .feature-card:hover::before {
            opacity: 1;
        }

        .feature-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--accent-secondary);
        }

        .feature-card p {
            color: var(--text-secondary);
        }

        /* Footer */
        footer {
            background: var(--bg-secondary);
            color: var(--text-secondary);
            text-align: center;
            padding: 2rem;
            margin-top: 4rem;
            border-top: 1px solid rgba(59, 130, 246, 0.1);
        }

        /* Animations */
        @keyframes glow {
            0% { opacity: 0.8; }
            100% { opacity: 1; }
        }

        @keyframes backgroundScroll {
            0% { transform: translate(0, 0); }
            100% { transform: translate(-50%, -50%); }
        }

        @keyframes titleReveal {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeUp {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Mobile Responsiveness */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .features {
                padding: 1rem;
            }
        }""")
    
    print(f"Project '{project_name}' initialized successfully!")
    print(f"Navigate to your project directory: cd {project_name}")
    print(f"Then run the app with: pypaze run")

@cli.command()
@click.option('--host', default='127.0.0.1', help='Host address.')
@click.option('--port', default=5000, help='Port number.')
@click.option('--debug', is_flag=True, default=True, help='Enable debug mode.')
def run(host, port, debug):
    """Run the app."""
    app = create_app()
    app.run(host=host, port=port, debug=debug)

@cli.command()
def routes():
    """Display all available routes."""
    app = create_app()
    print(f"Registered routes: {', '.join(str(rule) for rule in app.url_map.iter_rules())}")
