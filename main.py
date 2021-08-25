

from raylibpy import *

def main():

    # Initialization
    # ---------------------------------------------------------------
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
    # ---------------------------------------------------------------

    # Main game loop
    while not window_should_close():

        # Update
        # -----------------------------------------------------------

        # -----------------------------------------------------------

        # Draw
        # -----------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

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
class track(){
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
}

# Class for a Train
class train(){
    def __init__(self, color, direction, tile = 0, components = None, speed = 0):
        # What color the train is
        self.color = color

        # What tile the train is currently on
        self.tile = tile

        # What cars are attached to the train
        self.components = components

        # How far along the train is along the current track
        self.progress = 0.0

        # What direaction the train is facing (0 or 1)
        self.direction = direction

        # How fast the train is moving
        self.speed = speed
}

# Class for any obsticals on the map
class obstical(){
    def __init__(self, type, color = None):

        # What kind of obstical this obstical is
        self.type = type

        # Whar color is the obstical (None for trees)
        self.color = color
}


if __name__ == '__main__':
    main()
