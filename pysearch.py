# stdlib
import pyperclip
import os
import validators

# select search engine
duckduckgo = True  # else google.com

output = pyperclip.paste()
is_valid_url = validators.url(output)

if(is_valid_url):
    os.system('google-chrome '+output)
elif duckduckgo:
    os.system('google-chrome "www.duckduckgo.com/?q='+output+'"')
else:
    os.system('google-chrome "www.google.com/search?q='+output+'"')
