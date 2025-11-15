from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def healthcheck():
    # Simple check so hitting the root in a browser shows it's alive
    return "OK"

@app.route("/webhook", methods=["POST"])
def webhook():
    # Read the incoming JSON (if you ever want to inspect what Manychat sends)
    data = request.get_json(silent=True)
    print("Received body from client:", data)

    # Fixed JSON response for your training task
    response = {
        "profile": {
            "username": "greenfox",
            "details": {
                "full_name": "Evelyn Carter",
                "role": "Content Manager",
                "preferences": {
                    "theme": "dark",
                    "notifications": {
                        "email": "enabled",
                        "push": "disabled"
                    }
                }
            },
            "projects": [
                {
                    "title": "Autumn Campaign",
                    "status": "in_progress",
                    "notes": {
                        "goal": "increase engagement",
                        "focus_area": "storytelling",
                        "assets": {
                            "copy": "draft_ready",
                            "images": "awaiting_review"
                        }
                    }
                },
                {
                    "title": "Website Refresh",
                    "status": "planning",
                    "notes": {
                        "goal": "improve clarity",
                        "focus_area": "navigation",
                        "assets": {
                            "wireframes": "in_discussion",
                            "branding": "confirmed"
                        }
                    }
                }
            ]
        }
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
