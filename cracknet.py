#!/data/data/com.termux/files/usr/bin/env python3

import os
import time
import random
import subprocess
import sys
import logging
import requests
import serial
import threading
import platform

# ASCII Art di benvenuto
BANNER = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          C R A C K N E T - ELITE HACK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   SysOp: xAI Crew | Baud: 300 | Est. '89
   "Breaking the Grid Since the Dial-Up Days"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# Verifica ambiente Termux
def check_termux():
    termux_path = "/data/data/com.termux/files/usr"
    if not os.path.exists(termux_path):
        print("[-] ERROR: This system ain't Termux. CrackNet runs only on Termux rigs.")
        sys.exit(1)
    if "com.termux" not in os.environ.get("PREFIX", ""):
        print("[-] ERROR: Not running in Termux environment. Dial up Termux first.")
        sys.exit(1)
    print("[+] Termux detected. CrackNet online.")

# Controllo dipendenze
try:
    import requests
    import serial
except ImportError as e:
    print(f"[-] ERROR: {e.name} not found. Dial 'pip install {e.name}' in Termux.")
    sys.exit(1)

# Configurazione logging
if not os.path.exists("logs"):
    os.makedirs("logs")
logging.basicConfig(filename="logs/cracknet.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

# Variabili globali (specifiche Termux)
ADB_PATH = "/data/data/com.termux/files/usr/bin/adb"
TWILIO_SID = "YOUR_TWILIO_SID"  # Sostituisci con le tue credenziali
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE = "YOUR_TWILIO_PHONE"
DEVICE_SERIAL = None
SERIAL_PORT = "/dev/ttyUSB0"  # Porta seriale USB-to-jack su Termux
SERIAL_BAUD = 9600  # Baud rate per SIM/ATM

# Inizializzazione
def init_system():
    global DEVICE_SERIAL
    print("[*] Connecting to the Matrix...")
    if not os.path.exists(ADB_PATH):
        print("[-] ADB offline. Install with: pkg install android-tools")
        sys.exit(1)
    result = subprocess.run([ADB_PATH, "devices"], capture_output=True, text=True)
    devices = [line.split("\t")[0] for line in result.stdout.splitlines() if "\t" in line]
    if not devices:
        print("[-] No nodes on the line. Plug in your Android rig.")
        sys.exit(1)
    DEVICE_SERIAL = devices[0]
    print(f"[+] Hooked into node: {DEVICE_SERIAL}")
    logging.info(f"Node hooked: {DEVICE_SERIAL}")

# Funzioni operative
def pin_phreaker(length=4, attempts=20):
    print("[*] Starting Pin Phreaker...")
    for i in range(attempts):
        pin = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        print(f">>> Dialing PIN: {pin} [{i+1}/{attempts}]")
        subprocess.run([ADB_PATH, "-s", DEVICE_SERIAL, "shell", "input", "text", pin])
        time.sleep(0.2)
    print("[+] Phreaker offline.")
    logging.info(f"Pin Phreaker ran {attempts} dials.")

def wifi_wardialer():
    print("[*] Wardialing WiFi Nets...")
    print("[!] Simulated handshake capture (needs root or monitor adapter).")
    fake_handshake = "WPA2:HASH:5F4DCC3B5AA765D61D8327DEB882CF99"
    print(f">>> Captured handshake: {fake_handshake}")
    password = "password123"
    print(f"[+] Cracked WiFi key: {password}")
    logging.info(f"WiFi Wardialer - Simulated crack: {password}")

def tone_blaster(target, message="CrackNet Tone", count=15):
    print(f"[*] Blasting tones to {target}...")
    for i in range(count):
        try:
            response = requests.post(
                f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json",
                auth=(TWILIO_SID, TWILIO_AUTH_TOKEN),
                data={"To": target, "From": TWILIO_PHONE, "Body": f"{message} #{i+1}"}
            )
            if response.status_code == 201:
                print(f">>> Tone {i+1}/{count} sent.")
            else:
                print(f"[-] Tone {i+1} dropped: {response.text}")
            time.sleep(1)
        except Exception as e:
            print(f"[-] Tone blast error: {e}")
            logging.error(f"Tone Blaster error: {e}")
    print("[+] Tone blast complete.")

def sim_jacker():
    print("[*] Initiating SIM Jacker...")
    try:
        with serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1) as ser:
            print(f"[+] Connected to {SERIAL_PORT} at {SERIAL_BAUD} baud.")
            ser.write(b"AT+CSQ\r")
            time.sleep(1)
            response = ser.read(100).decode('ascii', errors='ignore')
            print(f">>> SIM Response: {response}")
            logging.info(f"SIM Jacker - Response: {response}")
    except serial.SerialException as e:
        print(f"[-] SIM Jacker error: {e}")
        print("[!] Check USB-to-jack connection or port config in Termux.")
        logging.error(f"SIM Jacker error: {e}")

# Bot AI per automazione
class CrackBot:
    def __init__(self):
        self.running = False
        self.commands = {
            "1": self.auto_wifi_wardial,
            "2": self.auto_pin_phreak,
            "3": self.auto_tone_blast,
            "4": self.auto_ai_crack,
            "5": self.auto_sim_jack
        }

    def start(self):
        self.running = True
        print("[*] CrackBot online. Automating the Termux grid...")
        threading.Thread(target=self.run, daemon=True).start()

    def stop(self):
        self.running = False
        print("[+] CrackBot offline.")

    def run(self):
        while self.running:
            print("[*] CrackBot scanning for tasks...")
            choice = random.choice(list(self.commands.keys()))
            print(f">>> Auto-executing command: {choice}")
            self.commands[choice]()
            time.sleep(5)

    def auto_wifi_wardial(self):
        wifi_wardialer()

    def auto_pin_phreak(self):
        pin_phreaker(length=4, attempts=10)

    def auto_tone_blast(self):
        target = "+391234567890"  # Numero di default per Termux
        print(f"[*] Auto-targeting: {target}")
        tone_blaster(target, count=5)

    def auto_ai_crack(self):
        inputs = [random.randint(0, 1) for _ in range(4)]
        print(f"[*] Auto-cracking with bits: {inputs}")
        EliteAI().crack(inputs)

    def auto_sim_jack(self):
        sim_jacker()

# AI Cracker
class EliteAI:
    def __init__(self):
        self.keys = [random.randint(0, 1) for _ in range(4)]

    def boot(self):
        print("[*] Booting Elite AI Cracker...")
        time.sleep(1)
        print("[+] AI ready to phreak on Termux.")

    def crack(self, inputs):
        score = sum(1 for i, k in zip(inputs, self.keys) if i == k)
        result = "[!] WARDIAL ALERT: Access Denied" if score < 3 else "[+] ACCESS GRANTED"
        print(result)
        logging.info(f"AI Crack - Inputs: {inputs}, Result: {result}")
        return score >= 3

# Menu principale
def main():
    os.system("clear")
    print(BANNER)
    check_termux()  # Verifica Termux all'avvio
    time.sleep(1)
    init_system()
    ai = EliteAI()
    ai.boot()
    bot = CrackBot()

    while True:
        print("\n=== CrackNet Menu ===")
        print("1. WiFi Wardialer")
        print("2. Pin Phreaker")
        print("3. Tone Blaster")
        print("4. AI Cracker")
        print("5. SIM Jacker (USB-to-Jack)")
        print("6. Start CrackBot (Auto-Hack)")
        print("7. Stop CrackBot")
        print("8. Log Off")
        choice = input(">>> Select hack: ")

        if choice == "1": wifi_wardialer()
        elif choice == "2": pin_phreaker()
        elif choice == "3":
            target = input(">>> Target phone (e.g., +391234567890): ")
            tone_blaster(target)
        elif choice == "4":
            inputs = [int(x) for x in input(">>> Enter 4 bits (e.g., 1 0 1 1): ").split()]
            ai.crack(inputs)
        elif choice == "5": sim_jacker()
        elif choice == "6":
            bot.start()
        elif choice == "7":
            bot.stop()
        elif choice == "8":
            print(">>> Logging off the Termux grid...")
            bot.stop()
            logging.info("User logged off.")
            sys.exit(0)
        else:
            print("[-] Bad command. Try again, phreaker.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Ctrl+C detected. Dropping line.")
        logging.info("User dropped line.")
    except Exception as e:
        print(f"[-] System crash: {e}")
        logging.error(f"Crash: {e}")
