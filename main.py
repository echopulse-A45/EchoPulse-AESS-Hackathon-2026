import matplotlib.pyplot as plt
import random
import requests
from datetime import datetime

# =====================================================
# EchoPulse Smart Flood Monitoring System
# Advanced Hackathon Edition
# =====================================================


# =====================================================
# Region Class
# =====================================================

class Region:

    def init(self, name):

        self.name = name

        # =========================================
        # Dynamic Sensor Readings
        # =========================================

        self.rainfall = random.randint(40, 100)

        self.water_level = random.randint(35, 100)

        self.humidity = random.randint(30, 95)

        self.temperature = random.randint(18, 35)

        self.ph = round(random.uniform(5.5, 8.5), 1)

        self.turbidity = random.randint(3, 20)

        # =========================================
        # Analysis Results
        # =========================================

        self.risk = "Unknown"

        self.water_quality = "Unknown"

        self.score = 0


    # =================================================
    # Flood Risk Analysis
    # =================================================

    def analyze_risk(self):

        self.score = (

            (self.rainfall * 0.4) +

            (self.water_level * 0.4) +

            (self.humidity * 0.2)

        )

        if self.score >= 80:

            self.risk = "High"

        elif self.score >= 50:

            self.risk = "Medium"

        else:

            self.risk = "Low"

        return self.risk


    # =================================================
    # Water Quality Analysis
    # =================================================

    def analyze_water_quality(self):

        if (

            6.5 <= self.ph <= 8.5 and

            self.turbidity < 10 and

            self.temperature < 35

        ):

            self.water_quality = "Clean Water"

        else:

            self.water_quality = "Polluted Water"

        return self.water_quality


# =====================================================
# EchoPulse Main System
# =====================================================

class EchoPulseSystem:

    def init(self):

        self.regions = []

        # =========================================
        # Telegram Bot Configuration
        # =========================================

        self.bot_token = "8697261611:AAG-qxjGRXdmb4ylQbsb8J1Oj4DEa6EpCew"

        self.chat_id = "8128207004"

        # =========================================
        # Dynamic Weather System
        # =========================================

        self.weather = random.choice([

            "Sunny",
            "Cloudy",
            "Stormy"

        ])

        # =========================================
        # Dynamic Solar Energy
        # =========================================

        if self.weather == "Sunny":

            self.solar_energy_generated = random.randint(1400, 1800)

        elif self.weather == "Cloudy":

            self.solar_energy_generated = random.randint(900, 1300)

        else:

            self.solar_energy_generated = random.randint(500, 900)

        # =========================================
        # Dynamic Radar Power
        # =========================================

        self.radar_power = random.randint(40, 80)

        self.standby_power = random.randint(3, 10)

        # =========================================
        # Traditional System
        # =========================================

        self.traditional_energy = 2400

        self.smart_energy = 0

        self.saved_energy = 0

        self.saving_percentage = 0

        # =========================================
        # IoT Sensors
        # =========================================

        self.sensors = ["Rain Sensor",
            "Water Level Sensor",
            "Humidity Sensor",
            "Temperature Sensor",
            "pH Sensor",
            "Turbidity Sensor",
            "Radar Sensor"

        ]


    # =================================================
    # Add Region
    # =================================================

    def add_region(self, region):

        self.regions.append(region)


    # =================================================
    # Telegram Alert System
    # =================================================

    def send_telegram_alert(self, message):

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

        data = {

            "chat_id": self.chat_id,

            "text": message

        }

        response = requests.post(url, data=data)

        print(response.text)


    # =================================================
    # Emergency Alarm
    # =================================================

    def activate_alarm(self, region):

        print("\n🚨 EMERGENCY ALERT 🚨")

        print(f"High Flood Risk in {region.name}")

        print("Warning Sirens Activated")

        print("Emergency Teams Notified")

        message = f"""
🚨 EchoPulse Emergency Alert 🚨

📍 Region: {region.name}

⚠️ Flood Risk: HIGH

🌧 Rainfall: {region.rainfall}

🌊 Water Level: {region.water_level}

💨 Humidity: {region.humidity}

💧 Water Quality: {region.water_quality}

⏰ Immediate action required.
"""

        self.send_telegram_alert(message)


    # =================================================
    # Smart Water Management
    # =================================================

    def manage_water(self, region):

        if region.water_quality == "Clean Water":

            print(f"💧 Clean water stored in tanks ({region.name})")

        else:

            print(f"⚠️ Polluted water drained safely ({region.name})")


    # =================================================
    # AI Flood Prediction
    # =================================================

    def predict_flood(self, region):

        print(f"\n🤖 AI Monitoring Active in {region.name}")

        if region.risk == "High":

            prediction_time = int(

                100 -

                (
                    region.rainfall +
                    region.water_level
                ) / 2

            )

            prediction_time = max(3, prediction_time)

            print(f"⚠️ Possible flood within {prediction_time} hours")

        else:

            print("✅ No immediate flood danger")


    # =================================================
    # Smart Radar Activation
    # =================================================

    def activate_radar(self):

        active_hours = 0

        for region in self.regions:

            # Analyze flood risk
            region.analyze_risk()

            # Analyze water quality
            region.analyze_water_quality()

            # AI prediction
            self.predict_flood(region)

            # =====================================
            # Smart Radar Logic
            # =====================================

            if region.risk == "High":

                active_hours += 6

                self.activate_alarm(region)

            elif region.risk == "Medium":

                active_hours += 3

            else:

                active_hours += 1

            # Water management
            self.manage_water(region)

        # Maximum 24 hours
        active_hours = min(active_hours, 24)

        # =====================================
        # Smart Energy Calculation
        # =====================================

        self.smart_energy = (

            (active_hours * self.radar_power) +

            ((24 - active_hours) * self.standby_power)

        )

        # =====================================
        # Energy Saving
        # =====================================

        self.saved_energy = (

            self.traditional_energy -
            self.smart_energy

        )
