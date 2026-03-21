# 🌊 EchoPulse - Smart Flood Monitoring & Water Management System

AESS Sustainability Hackathon 2026  
Green Radar Systems for Environmental Monitoring

---

### Team 👥
- Shahd Al-Ananzeh  
- Ibrahim Ba'arah  
- Dana Bani Malhem  
- Mariam Abu Shaqir  
- Alaa Al-Ghazawi  

Ajloun National University - Faculty of Information Technology

---

##  Project Overview
EchoPulse is an intelligent, low-power radar-based system for real-time flood monitoring and sustainable water management. It uses FMCW radar + low-energy sensors with Event-Driven Activation to save up to 75% energy while enabling early flood detection and smart reuse of floodwater.

---

## Submission Contents
- Case & Design Document → [EchoPulse_CaseDesign.pdf](EchoPulse_CaseDesign.pdf) *(16 pages - full documentation)*
- Algorithm & Simulation Files → simulations/ folder
  - fmcw_radar_signal_processing.py → FMCW radar signal simulation
  - adaptive_low_power_demo.py → 75% energy saving demonstration

---

## Key Innovations
- First Green Radar using Event-Driven Activation (sensors always on, radar only when anomaly detected)
- FMCW Radar + AI for flood prediction 6–24 hours in advance
-  Smart floodwater reuse (pH + Turbidity + Temperature analysis → automatic redirection to irrigation)
- Interactive Risk Map + Dashboard (Red/Orange/Yellow)
- IoT network of smart radar nodes with low-power communication

---

##  Simulation Results

![FMCW Radar Detection](simulations/screenshots/fmcw_detection.png)  
FMCW Radar - Accurate Water Level Detection

![Energy Saving](simulations/screenshots/energy_saving_75.png)  
75% Energy Saved with Event-Driven Operation

---

## How to Run the Simulations
`bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/EchoPulse-AESS-Hackathon-2026.git

# 2. Install requirements
pip install numpy matplotlib

# 3. Run simulations
python simulations/fmcw_radar_signal_processing.py
python simulations/adaptive_low_power_demo.py
