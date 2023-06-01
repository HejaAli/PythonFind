from flask import Flask, render_template
import requests
import os
import filecmp

print("PythonFind! - a pixelated cartoon graphic of a fat, lazy, unamused python with a keyboard in front of them, awaiting your search query")
print("")
print("Bulit by HejaAli on Github | A Python-Flask Web Browser | Powered by FrogFind!")
print("")
query = input("Slither to: ")
print("Hisssss...")
if query == "NUKE IT ALL!":
    if os.path.isdir("templates"):
        for file in os.scandir("templates"):
            os.remove(file)
        os.rmdir("templates")
        print("Browser cache deleted!")
        quit()
    else:
        print("No browser cache found!")
        quit()

website = "http://frogfind.com/?q=" + query
website = requests.get(website).text
if not os.path.isdir("templates"):
    os.mkdir("templates")

if not os.path.isfile(query + ".html"):
    file = "templates/" + query + ".html"
    file = open(file, 'w')
    file.write(website)
    file.close()
else:
    file = "templates/" + query + ".temp"
    file = open(file, 'w')
    file.write(website)
    file.close()
    if filecmp.cmp("templates/" + query + ".temp", "templates/" + query + ".html") == True:
        os.remove("templates/" + query + ".temp")
    else:
        file = "templates/" + query + ".html"
        file = open(file, 'w')
        file.write(website)
        file.close()

app = Flask(__name__)


@app.route('/')
def home():
   return render_template(query + ".html")
if __name__ == '__main__':
   app.run()
