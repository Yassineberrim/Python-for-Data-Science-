import time
from datetime import datetime
timestamp = time.time()
date = datetime.now()
print(
    f"Seconds since January 1, 1970: "
    f"{timestamp:,.4f} or "
    f"{timestamp:.2e} in scientific notation"
    
)
print(date.strftime("%b %d %Y"))