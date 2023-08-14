from datetime import datetime

# epoch_time_seconds = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
epoch_time_seconds = datetime.now().timestamp()

print(f"Seconds since January 1, 1970: {epoch_time_seconds:,.4f} or {epoch_time_seconds:.3g} in scientific notation")
today = datetime.today()
print(today.strftime("%b %d %Y"))

