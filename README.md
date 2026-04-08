# 📶 WiFi Signal Strength Mapping System

## 📌 Project Overview

This project is a **WiFi Signal Strength Mapping System** that analyzes and visualizes wireless network performance using real-time data.

It measures **RSSI (Received Signal Strength Indicator)** of nearby WiFi networks and displays the results using:

* 📊 Graphs
* 📍 Room comparison charts
* 🔥 Heatmaps

The system helps in understanding **network coverage, signal variation, and optimal router placement**.

---

## 🚀 Features

* 📡 Real-time WiFi scanning (macOS supported)
* 📊 Signal strength visualization (bar graph)
* 📍 Room-wise comparison of WiFi networks
* 🔥 Heatmap for signal distribution
* ⭐ Detection of currently connected WiFi
* 🧹 Duplicate network removal (strongest signal kept)
* 🗑️ Option to delete/reset stored data

---

## 🧠 Concepts Used (Mobile Communication)

* RSSI (Received Signal Strength Indicator)
* Signal Propagation
* Path Loss
* Interference
* Network Coverage Analysis

---

## 🛠️ Tech Stack

* Python
* Streamlit (UI Dashboard)
* Pandas (Data Processing)
* Matplotlib (Visualization)
* macOS `airport` command (WiFi scanning)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/wifi-signal-mapper.git
cd wifi-signal-mapper
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
streamlit run app.py
```

---

## 📊 How It Works

1. Enter a **location** (e.g., Classroom, Corridor)
2. Click **Scan WiFi**
3. The system:

   * Scans nearby networks
   * Extracts RSSI values
   * Cleans and processes data
4. Displays:

   * 📋 Table of networks
   * 📊 Signal strength graph
   * 📍 Room comparison chart
   * 🔥 Heatmap

---

## 📈 Output Explanation

### 📊 Graph

* Shows signal strength of WiFi networks
* Higher value (closer to 0) = stronger signal

### 📍 Room Comparison

* Compares the same WiFi across different locations
* Helps analyze signal drop

### 🔥 Heatmap

* Color-based representation of signal strength
* 🔴 Strong signal
* 🔵 Weak signal

---

## 🚧 Challenges Faced

* ❌ `pywifi` not working on macOS
  ✔️ Solved using native `airport` command

* ❌ Parsing irregular WiFi output
  ✔️ Solved using regex-based extraction

* ❌ Graph showing old data
  ✔️ Fixed using fresh matplotlib figure

* ❌ Duplicate SSIDs
  ✔️ Filtered using strongest signal

---

## 🌍 Real-World Applications

* WiFi coverage analysis
* Network optimization
* Smart building systems
* Router placement planning

---

## 🎯 Future Enhancements

* 📱 Android app integration
* 📍 Automatic location detection
* 🗺️ Floor-map based heatmap
* 📊 Export reports (PDF)

---
 
