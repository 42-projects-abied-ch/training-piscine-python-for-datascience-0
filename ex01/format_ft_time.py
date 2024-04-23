import datetime

now = datetime.datetime.now()

seconds_since_epoch = now.timestamp()

print(
    f"Seconds since January 1, 1970: {seconds_since_epoch}\
        or {seconds_since_epoch:.2e} in scientific notation"
)

print(now.strftime("%b %d %Y"))
