try:
	from parselinks.fetcher import get_content
	from parselinks.parser import parse_links
except ImportError:
	from fetcher import get_content
	from parser import parse_links

def get_links(url, as_list=False):

	content = get_content(url)

	links = parse_links(content)

	if not len(links):
		print("url not found....")
		return []

	if as_list:
		return links

	for link in links:
		print(f"{link}", end="\n")