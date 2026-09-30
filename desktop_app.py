
import threading
import webview
from app import app

HOST, PORT = "127.0.0.1", 5000


def run_flask():
    app.run(host=HOST, port=PORT, debug=False, use_reloader=False)


if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    webview.create_window("Campaign Analytics", f"http://{HOST}:{PORT}",
                           width=1150, height=780, min_size=(700, 500))
    webview.start()
