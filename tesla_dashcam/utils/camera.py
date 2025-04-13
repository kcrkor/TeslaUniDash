"""Camera class for Tesla Dashcam videos."""

class Camera:
    """Camera Class"""

    def __init__(self, layout, camera):
        self._layout = layout
        self._camera = camera
        self._include = True
        self._width = 1280
        self._height = 960
        self._xpos = 0
        self._xpos_override = False
        self._ypos = 0
        self._ypos_override = False
        self._scale = 0
        self._options = ""

    @property
    def camera(self):
        return self._camera

    @camera.setter
    def camera(self, value):
        self._camera = value

    @property
    def include(self):
        return self._include

    @include.setter
    def include(self, value):
        self._include = value

    @property
    def width(self):
        return (
            getattr(self._layout, "_" + self._camera + "_width")()
            if hasattr(self._layout, "_" + self._camera + "_width")
            else int(self._width * self.scale * self.include)
        )

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return (
            getattr(self._layout, "_" + self._camera + "_height")()
            if hasattr(self._layout, "_" + self._camera + "_height")
            else int(self._height * self.scale * self.include)
        )

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def xpos(self):
        if not self._xpos_override and hasattr(
            self._layout, "_" + self._camera + "_xpos"
        ):
            return getattr(self._layout, "_" + self._camera + "_xpos")() * self.include

        return self._xpos * self.include

    @xpos.setter
    def xpos(self, value):
        if value is not None:
            self._xpos = int(value)
            self._xpos_override = True
        else:
            self._xpos_override = False

    @property
    def ypos(self):
        if not self._ypos_override and hasattr(
            self._layout, "_" + self._camera + "_ypos"
        ):
            return getattr(self._layout, "_" + self._camera + "_ypos")() * self.include

        return self._ypos * self.include

    @ypos.setter
    def ypos(self, value):
        if value is not None:
            self._ypos = int(value)
            self._ypos_override = True
        else:
            self._ypos_override = False

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        if value is None:
            self._scale = None
        elif len(str(value).split("x")) == 1:
            # Scale provided is a multiplier
            self._scale = float(str(value).split("x")[0])
        else:
            # Scale is a resolution.
            self.width = int(str(value).split("x")[0])
            self.height = int(str(value).split("x")[1])
            self._scale = 1

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = value 