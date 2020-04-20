from graph import app

# NOTE: not sure this is right.
# This is only needed if I run the app with 'python graph.py' which uses the
# toy Wertzeug server.
# Since I figured out how to make gunicorn hot-reload source on source changes,
# i.e.
#   gunicorn graph:server --reload -b :8000
# I don't think I really need this.

if __name__ == "__main__":
    app.run()
