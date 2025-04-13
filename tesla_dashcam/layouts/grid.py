"""Grid layout for Tesla Dashcam videos."""

from .base import MovieLayout

class Grid(MovieLayout):
    """Grid Movie Layout

    [FRONT_CAMERA][REAR_CAMERA]
    [LEFT_CAMERA][RIGHT_CAMERA]
    """

    def __init__(self):
        super().__init__()
        self.scale = 1 / 2
        self._clip_order = ["front", "rear", "left", "right"]

    @property
    def video_width(self):
        # Width is 2 cameras side by side
        return int(
            max(
                self.cameras("front").width + self.cameras("rear").width,
                self.cameras("left").width + self.cameras("right").width
            )
        )

    @property
    def video_height(self):
        # Height is 2 cameras stacked
        perspective_adjustement = 3 / 2 if self.perspective else 1
        return int(
            self.cameras("front").height +
            max(
                perspective_adjustement * self.cameras("left").height,
                perspective_adjustement * self.cameras("right").height
            )
        )

    def _front_xpos(self):
        return 0

    def _front_ypos(self):
        return 0

    def _rear_xpos(self):
        return self.cameras("front").width

    def _rear_ypos(self):
        return 0

    def _left_xpos(self):
        return 0

    def _left_ypos(self):
        return self.cameras("front").height

    def _right_xpos(self):
        return self.cameras("left").width

    def _right_ypos(self):
        return self.cameras("front").height 