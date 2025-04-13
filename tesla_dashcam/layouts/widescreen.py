"""WideScreen layout for Tesla Dashcam videos."""

from .fullscreen import FullScreen

class WideScreen(FullScreen):
    """WideScreen Movie Layout

    [             FRONT_CAMERA             ]
    [LEFT_CAMERA][REAR_CAMERA][RIGHT_CAMERA]
    """

    def __init__(self):
        super().__init__()
        self.scale = 1 / 2
        # Set front scale to None so we know if it was overriden or not.
        self.cameras("front").scale = None

    # Only front_width has to be adjusted as by default width would be left+rear+right instead of normal scale.
    def _front_width(self):
        return (
            (
                self.cameras("left").width
                + self.cameras("rear").width
                + self.cameras("right").width
            )
            * self.cameras("front").include
            if self.cameras("front").scale is None
            else int(
                (
                    self.cameras("front")._width
                    * self.cameras("front").scale
                    * self.cameras("front").include
                )
            )
        ) 