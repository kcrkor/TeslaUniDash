"""Version information."""

VERSION = {"major": 0, "minor": 1, "patch": 21, "beta": 2}

VERSION_STR = f"v{VERSION['major']}.{VERSION['minor']}.{VERSION['patch']}"
if VERSION["beta"] > -1:
    VERSION_STR = f"{VERSION_STR}b{VERSION['beta']}"

DESCRIPTION_STRING = f"Created by tesla_dashcam {VERSION_STR}"

# Legacy compatibility
__version__ = f"{VERSION['major']}.{VERSION['minor']}.{VERSION['patch']}"
