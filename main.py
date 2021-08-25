

from raylibpy import *

def main():

    # Initialization
    # ---------------------------------------------------------------
    # Raylib stuff
    screen_width = 800
    screen_height = 450

    init_window(screen_width, screen_height, "Shortline Railroad - Remastered")

    spacing = 0

    camera = Camera2D()

    camera.offset = Vector2(0, 0)
    camera.target = Vector2(20, 20)
    camera.rotation = 0.0
    camera.zoom = 1.0

    set_target_fps(60)

    # Game counters & Flags:

    # Debug mode: Enable dev tools/cheats (maybe give this as a reward for beating year 2000?)
    debug = False

    # What year the player is at
    current_year = 1800

    # Cash is internally counted as 1's, but displayed as 1000's
    # Defaults to 100
    current_cash = 100

    # How many trains the player has successfully gotten to a station
    trains_stationed = 0

    # What "level" the player is on
    # Defaults to 15
    level = 15

    # List of entrances open to the player
    # Will be filled with a dictionary of entrances, the key being color and content being the state of the entrance
    entrances = []


    # ---------------------------------------------------------------

    # Main game loop
    while not window_should_close():

        # Update
        # -----------------------------------------------------------

        # -----------------------------------------------------------

        # Draw
        # -----------------------------------------------------------
        begin_drawing()

        clear_background(Color(85, 170, 0, 255))

        begin_mode2d(camera)

        end_mode2d()

        draw_text("SCREEN AREA", 640, 10, 20, RED)

        end_drawing()
        # -----------------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------------
    close_window()       # Close window and OpenGL context
    # ---------------------------------------------------------------

# Class for a track on the grid
class track():
    def __init__(self, type, has_switch, direction, has_light, tile = 0):
        # Types are:
        #   Long Curve (Top and Bottom)
        #   Sharp Curve (Left and Right)
        #   Straightaway (Facing 45* or -45*)
        self.type = type

        # A track has a switch if it has a "branching" path. Triple Switches are not allowed!
        self.has_switch = has_switch

        # A flag to set if the current track has a stop light
        self.has_light = has_light

        # Direction on the track (either 0 or 1)
        self.direction = direction

        # What tile on the map the track is on
        self.tile = tile

# Class for a Train
class train():
    def __init__(self, color, direction, type, tile = 0, components = None, speed = 0):
        # What color the train is
        self.color = color

        # What tile the train is currently on
        self.tile = tile

        # What kind of train is this train
        self.type = type

        # What cars are attached to the train (should be a list or None)
        self.components = components

        # How far along the train is along the current track (0% is start, 100% is end)
        self.progress = 0.0

        # What direaction the train is facing (0 or 1)
        self.direction = direction

        # How fast the train is moving (negative speed makes a train go backwards)
        self.speed = speed

# Class for any obsticals on the map
class obstical():
    def __init__(self, type, color = None):

        # What kind of obstical this obstical is
        self.type = type

        # Whar color is the obstical (None for trees)
        self.color = color


if __name__ == '__main__':
    main()
