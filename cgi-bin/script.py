#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

print("Content-type: text/html; charset=utf-8")
print()
print("<h1>Привет, Яндекс!</h1>")
print("<ol>")
for i in range(10):
    print("<li>", i**2, "</li>")
print("</ol>")
