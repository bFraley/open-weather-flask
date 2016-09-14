import sys

from app import app
try:
	import settings
except ImportError:
    print("Please copy settings-dist.py to settings.py and update your AP key")
    sys.exit()

app.run(debug=True)