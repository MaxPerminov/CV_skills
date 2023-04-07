# endswith and startswith methods can take several searching requests

print("https://www.google.com".startswith(("https://", "http://")))  # True
print("https://www.google.co.uk".endswith((".com", ".co.uk")))  # True
