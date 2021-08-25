

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

class track(){
    def __init__(self, type, has_switch):
        self.type = type
        self.has_switch = has_switch
        self.tile = 0
}


if __name__ == '__main__':
    main()
