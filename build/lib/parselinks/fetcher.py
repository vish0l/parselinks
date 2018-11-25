import requests

def fetch_request(url):
	"""
	url: valid url to fetch
	@return: return the status code and content

	simple function which take url as input and return the 
	status code and content
	"""
	if url is None:
		raise ValueError("Please enter url.")

	get_request = requests.get(url)

	if get_request.status_code == 200:
		return_value = {"error": 0, "status_code": get_request.status_code,	
						"content": get_request.content}
		return return_value
	else:
		error_value = {"error": 1,
						"status_code": get_request.status_code,
						"content": get_request.content}
		return error_value


def get_content(url):
	"""
	url: valid url to fetch
	@return simple html content of page

	this page take url and call fetch requests method to fetch
	html content, all cleaning methods will be called here.
	"""
	if url is None:
		raise ValueError("Please enter url.")

	get_html_content = fetch_request(url)

	if not get_html_content["error"]:
		return get_html_content["content"]
	else:
		return get_html_content