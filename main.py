import time
import requests
import random

THINGSPEAK_API_KEY = "API_KEY"
#use generated api key
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Simulated ultrasonic distance readings (in cm)
def get_bin_fill_level():
    # simulate bin level reading (0 = empty, 100 = full)
    return random.randint(10, 100)

def send_to_thingspeak(level):
    try:
        response = requests.get(THINGSPEAK_URL, params={"api_key": THINGSPEAK_API_KEY, "field1": level})
        if response.status_code == 200:
            print(f"[+] Data sent successfully. Bin level: {level}%")
        else:
            print(f"[!] Failed to send data. Response: {response.status_code}")
    except Exception as e:
        print(f"[!] Connection error: {e}")

def check_threshold(level, threshold=80):
    if level >= threshold:
        print(f"[ALERT] Bin level is {level}% — time to collect waste!")
        # Here we could send an SMS/Email alert via Twilio or Firebase
    else:
        print(f"Bin level normal ({level}%)")

def main():
    print("Smart Waste Management System Starting...\n")
    while True:
        level = get_bin_fill_level()
        send_to_thingspeak(level)
        check_threshold(level)
        time.sleep(5)  # simulate data every 5 seconds

if __name__ == "__main__":
    main()
