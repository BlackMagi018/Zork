class Weapon:
    """Your Halloween has become your last line of defense from terrifying monsters"""

    def __init__(self, text, modifier, ammo):
        """Constructor for Weapon class

            Parameters:
            text - weapon name
            modifier - weapons attack modifier
            ammo - uses left in candy
        """

        self.name = text
        self.mod = modifier
        self.ammo = ammo
