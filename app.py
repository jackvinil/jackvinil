import os
import json
import time
import random
import threading
from flask import Flask, render_template, request, jsonify, send_file
from scraper import InstagramScraper
import pandas as pd

app = Flask(__name__)
scraper = InstagramScraper()

# Global state for tracking progress
scrape_status = {
    "running": False,
    "progress": 0,
    "total": 0,
    "current_user": "",
    "data": [],
    "error": None,
    "paused": False,
    "target": ""
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    success, message = scraper.login(username, password)
    return jsonify({"success": success, "message": message})

@app.route('/start_scrape', methods=['POST'])
def start_scrape():
    global scrape_status
    if scrape_status["running"]:
        return jsonify({"success": False, "message": "Scrape já está em execução."})

    data = request.json
    target = data.get('target')

    if not target:
        return jsonify({"success": False, "message": "Perfil alvo não informado."})

    scrape_status = {
        "running": True,
        "progress": 0,
        "total": 0,
        "current_user": "",
        "data": [],
        "error": None,
        "paused": False,
        "target": target
    }

    thread = threading.Thread(target=run_scrape_thread, args=(target,))
    thread.start()

    return jsonify({"success": True})

def run_scrape_thread(target):
    global scrape_status
    try:
        target_user_id = scraper.cl.user_id_from_username(target)
        followers = scraper.cl.user_followers(target_user_id)
        scrape_status["total"] = len(followers)

        # Check if we have a resume file
        resume_file = f"resume_{target}.json"
        start_index = 0
        if os.path.exists(resume_file):
            with open(resume_file, 'r') as f:
                saved_state = json.load(f)
                scrape_status["data"] = saved_state.get("data", [])
                start_index = len(scrape_status["data"])
                scrape_status["progress"] = start_index

        follower_ids = list(followers.keys())

        for i in range(start_index, len(follower_ids)):
            if not scrape_status["running"]:
                break

            if scrape_status["paused"]:
                while scrape_status["paused"] and scrape_status["running"]:
                    time.sleep(1)
                if not scrape_status["running"]:
                    break

            follower_id = follower_ids[i]
            details = scraper.get_user_details(follower_id)

            if details:
                mapped_data = scraper.map_user_data(details)
                scrape_status["data"].append(mapped_data)

            scrape_status["progress"] = i + 1

            # Save progress periodically
            if (i + 1) % 5 == 0:
                with open(resume_file, 'w') as f:
                    json.dump({"data": scrape_status["data"]}, f)

            # Safety delay
            time.sleep(random.uniform(15, 30))

        scrape_status["running"] = False
        # Save final data to CSV when done
        if scrape_status["data"]:
            df = pd.DataFrame(scrape_status["data"])
            df.to_csv(f"followers_{target}.csv", index=False)

    except Exception as e:
        scrape_status["error"] = str(e)
        scrape_status["running"] = False

@app.route('/status')
def get_status():
    return jsonify(scrape_status)

@app.route('/pause', methods=['POST'])
def pause_scrape():
    scrape_status["paused"] = True
    return jsonify({"success": True})

@app.route('/resume', methods=['POST'])
def resume_scrape():
    scrape_status["paused"] = False
    return jsonify({"success": True})

@app.route('/stop', methods=['POST'])
def stop_scrape():
    scrape_status["running"] = False
    return jsonify({"success": True})

@app.route('/download')
def download_csv():
    target = scrape_status["target"]
    filename = f"followers_{target}.csv"
    if os.path.exists(filename):
        return send_file(filename, as_attachment=True)
    elif scrape_status["data"]:
        # Generate temporary CSV if file doesn't exist yet but data does
        df = pd.DataFrame(scrape_status["data"])
        df.to_csv(filename, index=False)
        return send_file(filename, as_attachment=True)
    return jsonify({"success": False, "message": "Arquivo não encontrado."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
