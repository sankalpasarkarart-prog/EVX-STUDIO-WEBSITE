import urllib.request
import re

url = "https://drive.google.com/drive/folders/179xsZgVmBKOkDbjtsK81s9hj4sbNb-64?usp=drive_link"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        # Google Drive folder pages usually contain data chunks in script tags
        # We can try to look for patterns like '1.mp4' and nearby IDs
        
        # Let's print out the raw HTML or a subset around '.mp4'
        matches = re.finditer(r'.{0,50}\.mp4.{0,100}', html)
        found = False
        for m in matches:
            print("MATCH:", m.group(0))
            found = True
        
        if not found:
            print("No .mp4 matches found. The page might be rendering via JS only.")
            
        # Try to find common file ID patterns
        # File IDs are usually 33 characters long, e.g. 1ABC...
except Exception as e:
    print("Error:", e)
