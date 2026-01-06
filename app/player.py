class Player:
    def __init__(self):
        # Core stats
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100

        # Progression
        self.badges = []
        self.league = "Initiate"

    def add_xp(self, amount):
        """Add XP and handle level-ups"""
        self.xp += amount
        print(f"[XP] Gained {amount} XP")

        while self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        """Increase level and scale difficulty"""
        self.xp -= self.xp_to_next_level
        self.level += 1
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)

        print(f"[LEVEL UP] You are now level {self.level}")

    def add_badge(self, badge_name):
        if badge_name not in self.badges:
            self.badges.append(badge_name)
            print(f"[BADGE UNLOCKED] {badge_name}")

    def get_status(self):
        """Return player state (used by UI later)"""
        return {
            "level": self.level,
            "xp": self.xp,
            "xp_to_next_level": self.xp_to_next_level,
            "badges": self.badges,
            "league": self.league
        }
