#!/data/data/com.termux/files/usr/bin/env python3

import os
import time
import random
import subprocess
import sys
import logging
import threading

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
    """Controlla se il tool è in esecuzione su Termux."""
    termux_path = "/data/data/com.termux/files/usr"
    if not os.path.exists(termux_path):
        print("[-] ERROR: This ain't Termux. CrackNet runs only on Termux rigs.")
        sys.exit(1)
    if "com.termux" not in os.environ.get("PREFIX", ""):
        print("[-] ERROR: Not in Termux environment. Dial up Termux first.")
        sys.exit(1)
    print("[+] Termux detected. CrackNet online.")

# Configurazione logging
def setup_logging():
    """Imposta il logging in una directory 'logs' su Termux."""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logging.basicConfig(filename="logs/cracknet.log", level=logging.INFO,
                        format="%(asctime)s - %(message)s")

# Variabili globali (specifiche Termux)
ADB_PATH = "/data/data/com.termux/files/usr/bin/adb"
DEVICE_SERIAL = None

# Inizializzazione
def init_system():
    """Inizializza il sistema, verifica ADB e collega un dispositivo."""
    global DEVICE_SERIAL
    print("[*] Connecting to the Matrix...")
    if not os.path.exists(ADB_PATH):
        print("[-] ADB offline. Install with: pkg install android-tools")
        print("[!] Running without ADB for non-ADB hacks.")
        DEVICE_SERIAL = "NO_DEVICE"
        return
    result = subprocess.run([ADB_PATH, "devices"], capture_output=True, text=True)
    devices = [line.split("\t")[0] for line in result.stdout.splitlines() if "\t" in line]
    if not devices:
        print("[-] No nodes on the line. Plug in your Android rig.")
        print("[!] Proceeding without ADB for non-ADB hacks.")
        DEVICE_SERIAL = "NO_DEVICE"
    else:
        DEVICE_SERIAL = devices[0]
        print(f"[+] Hooked into node: {DEVICE_SERIAL}")
        logging.info(f"Node hooked: {DEVICE_SERIAL}")

# Funzioni operative
def pin_phreaker(length=4, attempts=20):
    """Simula il brute-force di PIN su un dispositivo Android via ADB."""
    print("[*] Starting Pin Phreaker...")
    if DEVICE_SERIAL == "NO_DEVICE":
        print("[-] No ADB node connected. Simulating phreaking...")
        for i in range(attempts):
            pin = ''.join([str(random.randint(0, 9)) for _ in range(length)])
            print(f">>> Dialing PIN: {pin} [{i+1}/{attempts}]")
            time.sleep(0.1)  # Simulazione più veloce senza ADB
        print("[+] Phreaker offline (simulated).")
        logging.info(f"Pin Phreaker simulated {attempts} dials.")
        return
    for i in range(attempts):
        pin = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        print(f">>> Dialing PIN: {pin} [{i+1}/{attempts}]")
        subprocess.run([ADB_PATH, "-s", DEVICE_SERIAL, "shell", "input", "text", pin])
        time.sleep(0.2)
    print("[+] Phreaker offline.")
    logging.info(f"Pin Phreaker ran {attempts} dials.")

def wifi_wardialer():
    """Simula la cattura di una password WiFi."""
    print("[*] Wardialing WiFi Nets...")
    print("[!] Simulated handshake capture (no root or adapter needed).")
    fake_handshake = "WPA2:HASH:5F4DCC3B5AA765D61D8327DEB882CF99"
    print(f">>> Captured handshake: {fake_handshake}")
    password = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=8))
    print(f"[+] Cracked WiFi key: {password}")
    logging.info(f"WiFi Wardialer - Simulated crack: {password}")

# Bot AI per automazione
class CrackBot:
    """Bot AI che automatizza i comandi di CrackNet."""
    def __init__(self):
        self.running = False
        self.commands = {
            "1": self.auto_wifi_wardial,
            "2": self.auto_pin_phreak
        }

    def start(self):
        """Avvia il bot in un thread separato."""
        self.running = True
        print("[*] CrackBot online. Automating the Termux grid...")
        threading.Thread(target=self.run, daemon=True).start()

    def stop(self):
        """Ferma il bot."""
        self.running = False
        print("[+] CrackBot offline.")

    def run(self):
        """Esegue comandi casuali ogni 5 secondi."""
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

# AI Cracker
class EliteAI:
    """Semplice AI per cracking binario."""
    def __init__(self):
        self.keys = [random.randint(0, 1) for _ in range(4)]

    def boot(self):
        """Avvia l'AI con un delay retrò."""
        print("[*] Booting Elite AI Cracker...")
        time.sleep(1)
        print("[+] AI ready to phreak on Termux.")

    def crack(self, inputs):
        """Confronta input con chiavi interne."""
        score = sum(1 for i, k in zip(inputs, self.keys) if i == k)
        result = "[!] WARDIAL ALERT: Access Denied" if score < 3 else "[+] ACCESS GRANTED"
        print(result)
        logging.info(f"AI Crack - Inputs: {inputs}, Result: {result}")
        return score >= 3

# Menu principale
def main():
    """Funzione principale con menu interattivo."""
    os.system("clear")
    print(BANNER)
    check_termux()  # Verifica Termux
    setup_logging()  # Configura logging
    time.sleep(1)
    init_system()   # Inizializza sistema
    ai = EliteAI()
    ai.boot()
    bot = CrackBot()

    while True:
        print("\n=== CrackNet Menu ===")
        print("1. WiFi Wardialer (Simulated)")
        print("2. Pin Phreaker")
        print("3. AI Cracker")
        print("4. Start CrackBot (Auto-Hack)")
        print("5. Stop CrackBot")
        print("6. Log Off")
        choice = input(">>> Select hack: ")

        if choice == "1":
            wifi_wardialer()
        elif choice == "2":
            pin_phreaker()
        elif choice == "3":
            try:
                inputs = [int(x) for x in input(">>> Enter 4 bits (e.g., 1 0 1 1): ").split()]
                ai.crack(inputs)
            except ValueError:
                print("[-] Bad input. Use 4 bits (0 or 1).")
        elif choice == "4":
            bot.start()
        elif choice == "5":
            bot.stop()
        elif choice == "6":
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
