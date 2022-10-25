import urllib.request
try:
    site = urllib.request.urlopen('https://www.jw.org/pt/')
except urllib.error.URLError:
    print('\033[1;31mInfelizmente o site JW.org não está acessível no momento.\033[m')
else:
    print('\033[1;32mO site JW.org está acessível.\033[m')
