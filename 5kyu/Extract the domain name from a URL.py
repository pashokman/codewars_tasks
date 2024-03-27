"""
Extract the domain name from a URL

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

"""
import re

def domain_name(url):
    match = re.search(r'(?:http[s]?://)?(?:www\.)?([a-zA-Z0-9-]+)\.', url)
    if match:
        return match.group(1)
    else:
        return None


print(domain_name("http://google.com"), "google")
print(domain_name("http://google.co.jp"), "google")
print(domain_name("https://123.net"), "123")
print(domain_name("https://hyphen-site.org"), "hyphen-site")
print(domain_name("http://codewars.com"), "codewars")
print(domain_name("www.xakep.ru"), "xakep")
print(domain_name("https://youtube.com"), "youtube")
print(domain_name("http://www.codewars.com/kata/"), "codewars")
print(domain_name("icann.org"), "icann")