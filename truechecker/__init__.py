__all__ = ["TrueChecker"]

import os

from .api import TrueChecker

# install uvloop if exists and not disabled
try:
    import uvloop
except ImportError:  # pragma: no cover
    uvloop = None
else:
    if "DISABLE_UVLOOP" not in os.environ:
        uvloop.install()
