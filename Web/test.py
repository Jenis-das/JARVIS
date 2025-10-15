import requests
from bs4 import BeautifulSoup

def cmd_browser(url):
    if not url.startswith("http"):
        url = "http://" + url
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text()
        print("\n" + "="*80 + "\n")
        print(text[:4000])
        print("\n" + "="*80 + "\n")
    except Exception as e:
        print("Error opening page:", e)

# Example integration
while True:
    command = input("JARVIS> ").lower()
    if command == "exit":
        break
    elif "open" in command:
        url = command.replace("open", "").strip()
        cmd_browser(url)
    elif "search" in command:
        query = command.replace("search", "").strip().replace(" ", "+")
        cmd_browser(f"https://www.google.com/search?q={query}")
    else:
        print("Unknown command")
