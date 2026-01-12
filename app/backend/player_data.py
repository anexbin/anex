echo "import json, os

PLAYER_FILE = 'xp/player_xp.json'
TOKEN_FILE = 'tokens/player_tokens.json'

def load_player():
    if os.path.exists(PLAYER_FILE):
        with open(PLAYER_FILE, 'r') as f:
            return json.load(f)
    return {'xp':0, 'tokens':0, 'badges':[]}

def save_player(player):
    os.makedirs(os.path.dirname(PLAYER_FILE), exist_ok=True)
    with open(PLAYER_FILE, 'w') as f:
        json.dump(player, f)

def update_xp(amount):
    player = load_player()
    player['xp'] += amount
    save_player(player)
    return player

def update_tokens(amount):
    player = load_player()
    player['tokens'] += amount
    save_player(player)
    return player
" > backend/player_data.py
