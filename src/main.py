import requests
import matplotlib.pyplot as plt
from datetime import datetime

# =========================
# TELEGRAM BOT (PUBLIC)
# =========================
TOKEN = "8697261611:AAG-qxjGRXdmb4ylQbsb8J1Oj4DEa6EpCew"
API = f"https://api.telegram.org/bot{TOKEN}"

users = set()


# =========================
# COLLECT USERS
# =========================
def update_users():

    try:
        data = requests.get(API + "/getUpdates").json()

        for u in data.get("result", []):

            msg = u.get("message")

            if msg:

                chat_id = msg["chat"]["id"]

                users.add(chat_id)

    except:
        pass


def send_all(text):

    for u in list(users):

        try:
            requests.post(API + "/sendMessage", data={
                "chat_id": u,
                "text": text
            })
        except:
            pass


# =========================
# REALISTIC DATA (NO RANDOM)
# =========================
regions = {
    "Ajloun": {
        "rain": 85,
        "water_level": 80,
        "humidity": 70,
        "turbidity": 6
    },
    "Petra": {
        "rain": 75,
        "water_level": 65,
        "humidity": 60,
        "turbidity": 7
    },
    "Wadi Mujib": {
        "rain": 95,
        "water_level": 92,
        "humidity": 85,
        "turbidity": 5
    },
    "Zarqa": {
        "rain": 55,
        "water_level": 50,
        "humidity": 45,
        "turbidity": 12
    },
    "Aqaba": {
        "rain": 35,
        "water_level": 30,
        "humidity": 40,
        "turbidity": 4
    }
}


# =========================
# SCIENTIFIC RISK MODEL
# =========================
def calculate_score(d):

    score = (
        d["rain"] * 0.35 +
        d["water_level"] * 0.35 +
        d["humidity"] * 0.2 +
        d["turbidity"] * 0.1
    )

    return score


def get_level(score):

    if score >= 80:
        return "HIGH"
    elif score >= 60:
        return "MEDIUM"
    else:
        return "LOW"


# =========================
# ANALYSIS
# =========================
scores = []
levels = []

def analyze():

    scores.clear()
    levels.clear()

    for name, data in regions.items():

        score = calculate_score(data)
        level = get_level(score)

        scores.append(score)
        levels.append(level)


# =========================
# FIND MOST DANGEROUS
# =========================
def most_dangerous():

    idx = scores.index(max(scores))
    name = list(regions.keys())[idx]

    return name, scores[idx], levels[idx]


# =========================
# ALERT SYSTEM
# =========================
def alert():

    name, score, level = most_dangerous()

    if level == "HIGH":

        data = regions[name]

        msg = f"""
🚨 ECHOPULSE FLOOD ALERT 🚨

📍 Region: {name}
⚠️ Risk Level: {level}
📊 Score: {round(score,2)}

🌧 Rain: {data['rain']}
🌊 Water Level: {data['water_level']}
💨 Humidity: {data['humidity']}
🧪 Turbidity: {data['turbidity']}

🕒 {datetime.now()}
"""

        send_all(msg)


# =========================
# GRAPH (CLEAN)
# =========================
def graph():

    plt.clf()

    x = list(regions.keys())

    plt.bar(x, scores, color="steelblue")

    plt.title("EchoPulse Flood Risk Map")
    plt.ylabel("Risk Score")

    for i, v in enumerate(scores):
        plt.text(i, v + 2, levels[i], ha="center")

    plt.xticks(rotation=20)

    plt.pause(0.1)


# =========================
# REPORT
# =========================
def report():

    name, score, level = most_dangerous()

    print("\n======================")
    print("ECHOPULSE REPORT")
    print("======================")
    print("Time:", datetime.now())

    for i, (n, d) in enumerate(regions.items()):
        print(f"{n} | Score: {round(scores[i],2)} | Level: {levels[i]}")

    print("\n🔥 MOST DANGEROUS:", name, level)


# =========================
# MAIN LOOP
# =========================
print("EchoPulse System Running...")

plt.ion()
plt.figure(figsize=(8,5))

while True:

    update_users()
    analyze()
    report()
    alert()
    graph()

    send_all("📡 EchoPulse System Updated Successfully")

    import time
    time.sleep(1800)
