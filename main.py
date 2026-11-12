import base64
import os

# Cutest picture entry: decode the bundled image and write it out.
# The image is stored base64-encoded (one line) so the repository stays
# plain text; the decoded bytes are exactly the picture below.
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png.b64")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(SRC, "r", encoding="ascii") as f:
    data = base64.b64decode(f.read().strip())
with open(OUT, "wb") as f:
    f.write(data)

# Sanity check: the output must be a whole PNG image.
assert data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) == 626616
