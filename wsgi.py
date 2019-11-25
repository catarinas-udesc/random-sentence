import os
from app import app as application


DEFAULT_PORT = 5000


if __name__ == "__main__":
	port = int(os.environ.get('PORT', DEFAULT_PORT))
	debug = port == DEFAULT_PORT
	host = '127.0.0.1' if debug else '0.0.0.0'
	application.run(host=host, port=port, debug=debug)
