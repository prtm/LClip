# stdlib
import pyperclip
import os
import validators

# select search engine
duckduckgo = True  # else google.com
firefox = True  # else chrome

output = pyperclip.paste()
is_valid_url = validators.url(output)

browser = 'firefox ' if firefox else 'google-chrome '

if(is_valid_url):
    os.system(browser + output)
elif duckduckgo:
    os.system(browser + '"www.duckduckgo.com/?q='+output+'"')
else:
    os.system(browser + '"www.google.com/search?q='+output+'"')
