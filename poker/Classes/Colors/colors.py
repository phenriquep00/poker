class Colors:
    def __init__(self):
        """
        Class to eliminate the need for adding variables every time you need to add a color to the project
        :return:
        None
        """
        # primary colors
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        # grays
        # light
        self.light_gray3 = (220, 220, 220)
        self.light_gray2 = (200, 200, 200)
        self.light_gray1 = (180, 180, 180)
        # dark
        self.dark_gray3 = (30, 30, 30)
        self.dark_gray2 = (45, 45, 45)
        self.dark_gray1 = (60, 60, 60)
        # greens
        # dark
        self.dark_green3 = (1, 24, 1)
        self.dark_green2 = (2, 50, 2)
        self.dark_green1 = (3, 76, 3)

        # blues
        # dark
        self.dark_blue3 = (1, 1, 24)
        self.dark_blue2 = (2, 2, 50)
        self.dark_blue1 = (3, 3, 76)

        # reds
        # dark
        self.dark_red3 = (24, 1, 1)
        self.dark_red2 = (50, 2, 2)
        self.dark_red1 = (76, 3, 3)

        # yellow
        self.yellow = (255, 255, 0)
