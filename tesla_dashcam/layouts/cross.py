"""Cross layout for Tesla Dashcam videos."""

from .fullscreen import FullScreen

class Cross(FullScreen):
    """Cross Movie Layout

         [FRONT_CAMERA]
    [LEFT_CAMERA][RIGHT_CAMERA]
         [REAR_CAMERA]
    """

    def __init__(self):
        super().__init__()
        self.scale = 1 / 2

    @property
    def video_width(self):
        return max(
            self.cameras("front").width,
            self.cameras("left").width + self.cameras("right").width,
            self.cameras("rear").width,
        )

    @property
    def video_height(self):
        if self.perspective:
            height = int(
                max(
                    3 / 2 * self.cameras("left").height,
                    3 / 2 * self.cameras("right").height,
                )
            )
            if (
                self.cameras("left").include
                and self.cameras("left").scale >= self.cameras("rear").scale
                and self.cameras("right").include
                and self.cameras("right").scale >= self.cameras("rear").scale
                and self.cameras("rear").include
            ):
                height = int(height / 3 * 2)
            height += self.cameras("rear").height
        else:
            height = (
                max(self.cameras("left").height, self.cameras("right").height)
                + self.cameras("rear").height
            )

        return int(height + self.cameras("front").height)

    def _front_xpos(self):
        return (
            int(max(0, self.center_xpos - (self.cameras("front").width / 2)))
            * self.cameras("front").include
        )

    def _left_xpos(self):
        return (
            max(
                0,
                self.center_xpos
                - int((self.cameras("left").width + self.cameras("right").width) / 2),
            )
            * self.cameras("left").include
        )

    def _left_ypos(self):
        return (
            self.cameras("front").height
            + int(
                (
                    max(self.cameras("left").height, self.cameras("right").height)
                    - self.cameras("left").height
                )
                / 2
            )
        ) * self.cameras("left").include

    def _right_xpos(self):
        return (
            max(
                0,
                self.center_xpos
                - int((self.cameras("left").width + self.cameras("right").width) / 2)
                + self.cameras("left").width,
            )
            * self.cameras("right").include
        )

    def _right_ypos(self):
        return (
            self.cameras("front").height
            + int(
                (
                    max(self.cameras("left").height, self.cameras("right").height)
                    - self.cameras("right").height
                )
                / 2
            )
        ) * self.cameras("right").include

    def _rear_xpos(self):
        return (
            int(max(0, self.center_xpos - (self.cameras("rear").width / 2)))
            * self.cameras("rear").include
        )

    def _rear_ypos(self):
        return int(max(0, self.video_height - self.cameras("rear").height)) 