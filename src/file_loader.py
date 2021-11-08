import os
from typing import List


def listImages(dir: str) -> List[str]:
    """
    List all images (where zoom accepts: jpeg jpg png) in a directory.
    """
    return [f for f in os.listdir(dir)
            if os.path.isfile(os.path.join(dir, f))
            and f.endswith((".png", ".jpeg", ".jpg"))]
