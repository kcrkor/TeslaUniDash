"""Base layout class for Tesla Dashcam videos."""

from ..utils.camera import Camera
from ..utils.font import Font

class MovieLayout:
    """Main Layout class"""

    def __init__(self):
        self._cameras = {
            "front": Camera(layout=self, camera="front"),
            "left": Camera(layout=self, camera="left"),
            "right": Camera(layout=self, camera="right"),
            "rear": Camera(layout=self, camera="rear"),
        }
        self._clip_order = ["left", "right", "front", "rear"]
        self._font = Font(layout=self)

        self._swap_left_right = False
        self._swap_front_rear = False

        self._perspective = False
        self._title_screen_map = False

        self._font.halign = "CENTER"
        self._font.valign = "BOTTOM"

    def cameras(self, camera):
        return self._cameras.get(camera, self._cameras)

    @property
    def clip_order(self) -> list:
        return self._clip_order

    @clip_order.setter
    def clip_order(self, value: list):
        self._clip_order = []
        for camera in value:
            camera = camera.lower().strip()
            if camera in ["front", "left", "right", "rear"]:
                self._clip_order.append(camera)

        # Make sure we have all of them, if not then add based on default order.
        if "left" not in self._clip_order:
            self._clip_order.append("left")
        if "right" not in self._clip_order:
            self._clip_order.append("right")
        if "front" not in self._clip_order:
            self._clip_order.append("front")
        if "rear" not in self._clip_order:
            self._clip_order.append("rear")

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value

    @property
    def swap_left_right(self):
        return self._swap_left_right

    @swap_left_right.setter
    def swap_left_right(self, value):
        self._swap_left_right = value

    @property
    def swap_front_rear(self):
        return self._swap_front_rear

    @swap_front_rear.setter
    def swap_front_rear(self, value):
        self._swap_front_rear = value

    @property
    def perspective(self):
        return self._perspective

    @perspective.setter
    def perspective(self, new_perspective):
        self._perspective = new_perspective

        if self._perspective:
            self.cameras("left").options = (
                ", pad=iw+4:3/2*ih:-1:ih/8:0x00000000, "
                "perspective=x0=0:y0=1*H/5:x1=W:y1=-3/44*H:"
                "x2=0:y2=6*H/5:x3=7/8*W:y3=5*H/6:sense=destination"
            )
            self.cameras("right").options = (
                ", pad=iw+4:3/2*ih:-1:ih/8:0x00000000,"
                "perspective=x0=0:y1=1*H/5:x1=W:y0=-3/44*H:"
                "x2=1/8*W:y3=6*H/5:x3=W:y2=5*H/6:sense=destination"
            )
        else:
            self.cameras("left").options = ""
            self.cameras("right").options = ""

    @property
    def title_screen_map(self):
        return self._title_screen_map

    @title_screen_map.setter
    def title_screen_map(self, value):
        self._title_screen_map = value

    @property
    def scale(self):
        # Return scale of new video based on 1280x960 video = scale:1
        return (self.video_height * self.video_width) / (1280 * 960)

    @scale.setter
    def scale(self, scale):
        self.cameras("front").scale = scale
        self.cameras("left").scale = scale
        self.cameras("right").scale = scale
        self.cameras("rear").scale = scale

    @property
    def video_width(self):
        return int(
            max(
                self.cameras("front").xpos + self.cameras("front").width,
                self.cameras("left").xpos + self.cameras("left").width,
                self.cameras("right").xpos + self.cameras("right").width,
                self.cameras("rear").xpos + self.cameras("rear").width,
            )
        )

    @property
    def video_height(self):
        perspective_adjustement = 3 / 2 if self.perspective else 1
        return int(
            max(
                self.cameras("front").ypos + self.cameras("front").height,
                perspective_adjustement * self.cameras("left").ypos
                + self.cameras("left").height,
                perspective_adjustement * self.cameras("right").ypos
                + self.cameras("right").height,
                self.cameras("rear").ypos + self.cameras("rear").height,
            )
        )

    @property
    def center_xpos(self):
        return int(self.video_width / 2)

    @property
    def center_ypos(self):
        return int(self.video_height / 2)

    @property
    def _rear_xpos(self):
        return self.cameras("front").xpos + self.cameras("front").width

    @property
    def _left_ypos(self):
        return max(
            self.cameras("front").ypos + self.cameras("front").height,
            self.cameras("rear").ypos + self.cameras("rear").height,
        )

    @property
    def _right_xpos(self):
        return self.cameras("left").xpos + self.cameras("left").width

    @property
    def _right_ypos(self):
        return max(
            self.cameras("front").ypos + self.cameras("front").height,
            self.cameras("rear").ypos + self.cameras("rear").height,
        ) 