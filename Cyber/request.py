import requests

# URL target
url = "http://github.com/"
wordlist = ["admin", "login", "dashboard", "secret"]

print("Scanning directories...")
for word in wordlist:
    target_url = f"{url}{word}/"
    response = requests.get(target_url)
    if response.status_code == 200:
        print(f"Found: {target_url}")
    else:
        print(f"Not found: {target_url}")
