import webbrowser
a=int(input("Enter mobile number that you want to open for whatsapp:"))
b=str(a)
c="wa.me/91"+b
d=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('crome',None,webbrowser.BackgroundBrowser(d))
webbrowser.get('crome').open_new_tab(c)

