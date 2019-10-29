import urllib.error
import urllib.request

content = None
try:
    url = urllib.request.urlopen("https://www.python.org/")
    content = url.read()
    url.close()
except urllib.error.HTTPError:
    print("The web page is not found")
    exit()

file = open("python.html", "wb") # wb => write binary
file.write(content)
