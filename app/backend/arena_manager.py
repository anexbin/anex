echo "ARENAs = ['arena1','arena2','arena3','arena4','arena5','arena6','arena7','arena8']

def get_arena(index):
    if 0 <= index < len(ARENAs):
        return ARENAs[index]
    return None

def unlock_next_arena(current_index):
    if current_index+1 < len(ARENAs):
        return ARENAs[current_index+1]
    return None
" > backend/arena_manager.py
