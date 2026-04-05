from flask import Flask, request, jsonify

app = Flask(__name__)

# ----------------------------
# Fake database (IDOR)
# ----------------------------
campaigns = {
    "101": {
        "name": "summer",
        "note": "nothing interesting here"
    },
    "102": {
        "name": "winter",
        "note": "check dev environment"
    },
    "103": {
        "name": "dev",
        "note": "internal APIs shouldn't be exposed",
        "flag": "FLAG{devs_are_lazy}",
        "debug": "v2 endpoints under /api/v2/"
    }
}

# ----------------------------
# Homepage (flag 1)
# ----------------------------
@app.route("/")
def index():
    return """
    <html>
    <head>
        <script src="/js/config.js"></script>
    </head>
    <body>
        <h1>Campaign Dashboard</h1>

        <!-- FLAG{ghost_in_markup} -->

        <!-- TODO: remove hardcoded creds -->
    </body>
    </html>
    """

# ----------------------------
# JS leak (flag 2)
# ----------------------------
@app.route("/js/config.js")
def config():
    return "const API='/api/campaign?id='; const KEY='sync-9f3a'; // FLAG{entry_point_compromised}"

# ----------------------------
# API endpoint (IDOR)
# ----------------------------
@app.route("/api/campaign")
def get_campaign():
    cid = request.args.get("id")
    if cid in campaigns:
        return jsonify(campaigns[cid])
    return jsonify({"error": "not found"}), 404

# ----------------------------
# Hidden internal RCE endpoint (flag 3 path)
# ----------------------------
@app.route("/api/v2/internal/sync")
def internal_sync():

    if request.headers.get("X-Internal-Key") != "sync-9f3a":
        return "Forbidden", 403

    cmd = request.args.get("cmd")

    if not cmd:
        return "No command", 400

    import os
    os.system(cmd)

    return "Executed"

# ----------------------------
# Rabbit hole (waste time)
# ----------------------------
@app.route("/admin")
def admin():
    return jsonify({
        "message": "Admin panel coming soon",
        "hint": "Try default credentials",
        "creds": {
            "admin": "admin123",
            "dev": "password123"
        }
    })

# ----------------------------
# Run app
# ----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
