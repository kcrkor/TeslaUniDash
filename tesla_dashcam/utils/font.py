"""Font class for Tesla Dashcam videos."""

from ..constants import HALIGN, VALIGN

class Font:
    """Font Class"""

    def __init__(self, layout, font=None, size=None, color=None):
        self._layout = layout
        self._font = font
        self._size = size
        self._color = color
        self._halign = None
        self._valign = None
        self._xpos = None
        self._ypos = None

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value

    @property
    def size(self):
        if hasattr(self._layout, "_font_size"):
            return getattr(self._layout, "_font_size")()

        return (
            int(max(16, 16 * self._layout.scale)) if self._size is None else self._size
        )

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def halign(self):
        if hasattr(self._layout, "_font_halign"):
            return getattr(self._layout, "_font_halign")()

        return HALIGN.get(self._halign, self._halign)

    @halign.setter
    def halign(self, value):
        self._halign = value

    @property
    def valign(self):
        if hasattr(self._layout, "_font_valign"):
            return getattr(self._layout, "_font_valign")()

        return VALIGN.get(self._valign, self._valign)

    @valign.setter
    def valign(self, value):
        self._valign = value

    @property
    def xpos(self):
        return self._xpos

    @xpos.setter
    def xpos(self, value):
        self._xpos = value

    @property
    def ypos(self):
        return self._ypos

    @ypos.setter
    def ypos(self, value):
        self._ypos = value 