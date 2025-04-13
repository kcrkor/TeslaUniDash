"""Diamond layout for Tesla Dashcam videos."""

from .cross import Cross

class Diamond(Cross):
    """Diamond Movie Layout

                [FRONT_CAMERA]
    [LEFT_CAMERA]            [RIGHT_CAMERA]
                [REAR_CAMERA]
    """

    def __init__(self):
        super().__init__()
        self.scale = 1 / 2
        self._font.valign = "MIDDLE"

    def _font_halign(self):
        if self._font._halign == "CENTER":
            # Change alignment to left or right if one of the left/right cameras is excluded.
            if (self.cameras("left").include and not self.cameras("right").include) or (
                self.cameras("right").include and not self.cameras("left").include
            ):
                x_pos = int(
                    max(
                        self.cameras("front").xpos + self.cameras("front").width / 2,
                        self.cameras("rear").xpos + self.cameras("rear").width / 2,
                    )
                )
                return f"({x_pos} - text_w / 2)"

        return HALIGN.get(self._font._halign, self._font._halign)

    def _font_valign(self):
        if self._font._valign == "MIDDLE":
            if self.cameras("front").include:
                return (
                    f'({self.cameras("front").ypos + self.cameras("front").height} + 5)'
                )
            elif self.cameras("rear").include:
                return f'({self.cameras("rear").ypos} - 5 - text_h)'

        return VALIGN.get(self._font._valign, self._font._valign)

    def _font_size(self):
        # For this layout the video height has to include font size. But default for calculating
        # font size is based on video height.
        # Thus overriding font size to get video height without font size to figure our scaling.
        if self.font._size is None:
            scale = (
                self._video_height(include_fontsize=False)
                * self.video_width
                / (1280 * 960)
            )
            return int(max(16, 16 * scale))
        else:
            return self.font.size

    @property
    def video_width(self):
        return (
            max(self.cameras("front").width, self.cameras("rear").width)
            + self.cameras("left").width
            + self.cameras("right").width
        )

    def _video_height(self, include_fontsize=True):
        perspective = 3 / 2 if self.perspective else 1
        fontsize = self.font.size if include_fontsize else 0

        return int(
            max(
                perspective
                * max(self.cameras("left").height, self.cameras("right").height),
                self.cameras("front").height + self.cameras("rear").height + fontsize,
            )
        )

    @property
    def video_height(self):
        return self._video_height(include_fontsize=True)

    def _front_xpos(self):
        return (
            self.cameras("left").width
            + int(
                (
                    max(self.cameras("front").width, self.cameras("rear").width)
                    - self.cameras("front").width
                )
                / 2
            )
        ) * self.cameras("front").include

    def _left_xpos(self):
        return 0

    def _left_ypos(self):
        return max(0, self.center_ypos - int(self.cameras("left").height / 2))

    def _right_xpos(self):
        return max(
            self.cameras("front").xpos + self.cameras("front").width,
            self.cameras("rear").xpos + self.cameras("rear").width,
        )

    def _right_ypos(self):
        return max(0, self.center_ypos - int(self.cameras("right").height / 2))

    def _rear_xpos(self):
        return (
            self.cameras("left").width
            + int(
                (
                    max(self.cameras("front").width, self.cameras("rear").width)
                    - self.cameras("rear").width
                )
                / 2
            )
        ) * self.cameras("rear").include 