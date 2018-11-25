#parselinks - parse links from webpage, pdf, and other file formate etc


#Install

pip install parselinks

#How to use

to parse and print link

from parselinks import get_links

get_links(pass_url)
eg.

get_links("https://pypi.org/project/parselinks/")

#to parse and return value as list

get_links(pass_url, as_list=True)

eg.

get_links("https://pypi.org/project/parselinks/", as_list=True)