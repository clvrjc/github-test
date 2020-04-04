open("./index.html", "x")
with open("index.html", "w") as file:
    f.write("<html><head></head><body><h1>TEST</h1></body></html>")
    f.close()
    
print("good")
