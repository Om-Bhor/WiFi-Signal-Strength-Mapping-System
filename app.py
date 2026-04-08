import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
from wifi_scanner_mac import scan_wifi
import os

st.set_page_config(page_title="WiFi Mapper", layout="wide")

st.title("📶 WiFi Signal Strength Mapping System")

# 📍 Location input
location = st.text_input("Enter Location (Room/Lab/etc)")

# 🔍 Get connected WiFi
def get_connected_wifi():
    command = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]
    result = subprocess.run(command, capture_output=True, text=True)
    
    for line in result.stdout.split("\n"):
        if " SSID:" in line:
            return line.split(":")[1].strip()
    return None

connected_ssid = get_connected_wifi()

# 🔄 Scan Button
if st.button("🔄 Scan WiFi"):
    data = scan_wifi()
    df = pd.DataFrame(data)

    # 🧹 Clean data (strongest signal per SSID)
    df = df.sort_values(by="Signal", ascending=False)
    df = df.drop_duplicates(subset="SSID", keep="first")

    df["Location"] = location

    # ⭐ Mark connected
    df["Connected"] = df["SSID"].apply(lambda x: "✅" if x == connected_ssid else "")

    # 💾 Save data (optional for future)
    try:
        old = pd.read_csv("wifi_data.csv")
        df = pd.concat([old, df])
    except:
        pass

    df.to_csv("wifi_data.csv", index=False)

    # 📋 Show current scan
    st.subheader("📍 Current Scan Data")
    st.dataframe(df)

    # 📊 GRAPH (clean + sorted + highlight)
    st.subheader("📊 Signal Strength (Live)")

    fig, ax = plt.subplots()

    colors = ["green" if ssid == connected_ssid else "blue" for ssid in df["SSID"]]

    ax.barh(df["SSID"], df["Signal"], color=colors)
    ax.set_xlabel("Signal Strength (RSSI)")
    ax.set_ylabel("WiFi Network")

    st.pyplot(fig)

    # ⭐ Show connected WiFi
    if connected_ssid:
        st.success(f"Connected WiFi: {connected_ssid}")
    else:
        st.warning("Not connected to any WiFi")

# 🗑️ Delete Data
if st.button("🗑️ Delete All Saved Data"):
    if os.path.exists("wifi_data.csv"):
        os.remove("wifi_data.csv")
        st.warning("All data deleted!")
    else:
        st.info("No data found")

# 📍 ROOM COMPARISON
st.subheader("📍 Room Comparison (Same WiFi Across Locations)")

try:
    df_all = pd.read_csv("wifi_data.csv")

    selected_ssid = st.selectbox("Select WiFi Network", df_all["SSID"].unique())

    filtered = df_all[df_all["SSID"] == selected_ssid]

    if not filtered.empty:
        fig, ax = plt.subplots()

        ax.bar(filtered["Location"], filtered["Signal"])
        ax.set_title(f"Signal Strength of {selected_ssid} across locations")
        ax.set_xlabel("Location")
        ax.set_ylabel("RSSI")

        st.pyplot(fig)

except:
    st.info("No data available for comparison yet")

# 🔥 HEATMAP (REAL VISUAL)
st.subheader("🔥 WiFi Signal Heatmap")

try:
    df_all = pd.read_csv("wifi_data.csv")

    pivot = df_all.pivot_table(
        index="SSID",
        columns="Location",
        values="Signal",
        aggfunc="mean"
    )

    fig, ax = plt.subplots()

    cax = ax.imshow(pivot, aspect='auto', cmap='coolwarm', vmin=-90, vmax=-30)

    # Labels
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, rotation=45)

    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)

    fig.colorbar(cax, label="Signal Strength (RSSI)")

    st.pyplot(fig)

except:
    st.info("No data available for heatmap yet")