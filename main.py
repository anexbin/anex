# ===============================
# ANEX GAME — CORE ENTRY POINT
# Phone + PC friendly
# ===============================

import sys
import time

# -------------------------------
# GLOBAL PLAYER STATE
# -------------------------------
player = {
    "name": "Anex",
    "level": 1,
    "xp": 0,
    "arena": 1,
    "badges": []
}

ARENAS = [
    "Initialization",
    "Zero Trust Path",
    "Logic Exploitation",
    "System Fracture",
    "Identity Collapse",
    "AI Manipulation",
    "Red Team Ascension",
    "Anex League"
]

# -------------------------------
# UTILS
# -------------------------------
def slow_print(text, delay=0.02):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pause():
    input("\n[ Press Enter to continue ]")

# -------------------------------
# GAME LOGIC
# -------------------------------
def add_xp(amount):
    player["xp"] += amount
    slow_print(f"\n+{amount} XP earned")

    if player["xp"] >= player["level"] * 100:
        player["xp"] = 0
        player["level"] += 1
        slow_print(f"🔥 LEVEL UP → Level {player['level']}")

def show_profile():
    slow_print("\n=== PLAYER PROFILE ===")
    slow_print(f"Name   : {player['name']}")
    slow_print(f"Level  : {player['level']}")
    slow_print(f"XP     : {player['xp']}")
    slow_print(f"Arena  : {ARENAS[player['arena'] - 1]}")
    slow_print(f"Badges : {player['badges'] if player['badges'] else 'None'}")
    pause()

def play_arena():
    arena_name = ARENAS[player["arena"] - 1]
    slow_print(f"\nEntering Arena → {arena_name}")
    slow_print("Analyzing systems...")
    time.sleep(1)

    add_xp(25)

    if player["arena"] < len(ARENAS):
        player["arena"] += 1
        slow_print(f"🏆 Arena Unlocked → {ARENAS[player['arena'] - 1]}")
    else:
        slow_print("👑 You are already in the highest league")

    pause()

# -------------------------------
# MAIN MENU
# -------------------------------
def main_menu():
    while True:
        slow_print("\n=== ANEX GAME ===")
        slow_print("1. Play Arena")
        slow_print("2. Profile")
        slow_print("3. Exit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            play_arena()
        elif choice == "2":
            show_profile()
        elif choice == "3":
            slow_print("Exiting game...")
            break
        else:
            slow_print("Invalid choice")

# -------------------------------
# ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    slow_print("Booting Anex System...")
    time.sleep(0.5)
    main_menu()
