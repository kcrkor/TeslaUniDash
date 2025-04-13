"""FullScreen layout for Tesla Dashcam videos."""

from .base import MovieLayout

class FullScreen(MovieLayout):
    """FullScreen Movie Layout

                 [FRONT_CAMERA]
    [LEFT_CAMERA][REAR_CAMERA][RIGHT_CAMERA]
    """

    def __init__(self):
        super().__init__()
        self.scale = 1 / 2

    @property
    def video_width(self):
        return int(
            max(
                self.cameras("front").width,
                self.cameras("left").width
                + self.cameras("rear").width
                + self.cameras("right").width,
            )
        )

    @property
    def video_height(self):
        perspective_adjustement = 3 / 2 if self.perspective else 1
        return int(
            self.cameras("front").height
            + max(
                perspective_adjustement * self.cameras("left").height,
                self.cameras("rear").height,
                perspective_adjustement * self.cameras("right").height,
            )
        )

    def _front_height(self):
        # For height keep same ratio of 4/3
        return int(self.cameras("front").width / 4 * 3)

    def _front_xpos(self):
        # Make sure that front is placed in the middle
        return (
            max(
                0,
                self.center_xpos
                - int(
                    (
                        self.cameras("left").width
                        + self.cameras("front").width
                        + self.cameras("right").width
                    )
                    / 2
                )
                + self.cameras("left").width,
            )
            * self.cameras("front").include
        )

    def _left_xpos(self):
        return (
            max(
                0,
                self.center_xpos
                - int(
                    (
                        self.cameras("left").width
                        + self.cameras("rear").width
                        + self.cameras("right").width
                    )
                    / 2
                ),
            )
            * self.cameras("left").include
        )

    def _left_ypos(self):
        return (
            self.cameras("front").ypos + self.cameras("front").height
        ) * self.cameras("left").include

    def _rear_xpos(self):
        return (
            max(
                0,
                self.center_xpos
                - int(
                    (
                        self.cameras("left").width
                        + self.cameras("rear").width
                        + self.cameras("right").width
                    )
                    / 2
                )
                + self.cameras("left").width,
            )
            * self.cameras("rear").include
        )

    def _rear_ypos(self):
        return (
            self.cameras("front").ypos + self.cameras("front").height
        ) * self.cameras("rear").include

    def _right_xpos(self):
        return (
            max(
                0,
                self.center_xpos
                - int(
                    (
                        self.cameras("left").width
                        + self.cameras("rear").width
                        + self.cameras("right").width
                    )
                    / 2
                )
                + self.cameras("left").width
                + self.cameras("rear").width,
            )
            * self.cameras("right").include
        )

    def _right_ypos(self):
        return (
            self.cameras("front").ypos + self.cameras("front").height
        ) * self.cameras("right").include 