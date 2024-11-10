class AvailableMoves:
    def __init__(self, magnet_x, magnet_y, available_x, available_y):
        self.magnet_x = magnet_x
        self.magnet_y = magnet_y
        self.available_x = available_x
        self.available_y = available_y

    def __str__(self):
        return f"AvailableMoves(magnet_x={self.magnet_x}, magnet_y={self.magnet_y}, available_x={self.available_x}, available_y={self.available_y})"
