import re

from lxml import html

def gen_tree(html_content):
	"""
	html_content: simple html content to parse
	return: return the lxml tree

	this method will take simple html content in tree form and 
	output the tree.
	"""
	if html_content is None:
		raise ValueError("tree content cant be empty.")

	tree = html.fromstring(html_content)

	return tree

def parse_links(html_content):
	"""
	this function will take plain html content and 
	output all links in list formate.
	"""
	urls = []

	if not isinstance(html_content, str):
		html_content = str(html_content)

	if html_content is not None:
		urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', html_content)

	return urls