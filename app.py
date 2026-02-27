from flask import Flask, render_template
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# --- Fake data helpers ---

STATUSES = ["Active", "Inactive", "Pending"]
ROLES = ["Admin", "Editor", "Viewer", "Manager"]

USERS = [
    {"id": i + 1,
     "name": name,
     "email": f"{name.lower().replace(' ', '.')}",
     "role": ROLES[i % len(ROLES)],
     "status": STATUSES[i % len(STATUSES)],
     "joined": (datetime(2023, 1, 1) + timedelta(days=i * 17)).strftime("%b %d, %Y")}
    for i, name in enumerate([
        "Alice Johnson", "Bob Martinez", "Carol White", "David Lee",
        "Eva Brown", "Frank Garcia", "Grace Kim", "Henry Wilson",
        "Isla Davis", "Jack Taylor", "Karen Moore", "Liam Anderson"
    ])
]

for u in USERS:
    u["email"] = u["name"].lower().replace(" ", ".") + "@example.com"


def get_summary_stats():
    return {
        "total_users": len(USERS),
        "active_users": sum(1 for u in USERS if u["status"] == "Active"),
        "pending_users": sum(1 for u in USERS if u["status"] == "Pending"),
        "new_this_month": 3,
    }


def get_recent_activity():
    events = [
        ("Alice Johnson", "logged in", "2 minutes ago"),
        ("Bob Martinez", "updated profile", "15 minutes ago"),
        ("Carol White", "created a report", "1 hour ago"),
        ("David Lee", "invited a user", "3 hours ago"),
        ("Eva Brown", "changed settings", "yesterday"),
    ]
    return [{"user": e[0], "action": e[1], "time": e[2]} for e in events]


# --- Routes ---

@app.route("/")
def index():
    stats = get_summary_stats()
    activity = get_recent_activity()
    recent_users = USERS[:5]
    return render_template("index.html",
                           active_page="dashboard",
                           stats=stats,
                           activity=activity,
                           recent_users=recent_users)


@app.route("/users")
def users():
    return render_template("users.html",
                           active_page="users",
                           users=USERS)


@app.route("/analytics")
def analytics():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    signups = [4, 7, 5, 10, 8, 13, 11, 15, 9, 12, 14, 17]
    logins  = [22, 30, 28, 40, 35, 50, 45, 60, 42, 55, 58, 70]
    return render_template("analytics.html",
                           active_page="analytics",
                           months=months,
                           signups=signups,
                           logins=logins)


if __name__ == "__main__":
    app.run(debug=True)
