from urllib import request, parse
from urllib.error import HTTPError, URLError

#region URLOPEN
#urllib.request.urlopen(url, data=None, headers={}, timeout=...) GET by default, POST if data obj provided NO PATCH OR DELETE
#urlopen=>   url: str | Request,  data: _DataType = None, timeout: float | None  
response = request.urlopen("https://www.example.com/")
print(response) #<http.client.HTTPResponse object at 0x000001BE94B4FBB0>
print(response.status)
html = response.read()
print(html) #b'<!doctype html><html lang="en"><head><title>Example Domain</title><meta name=".......... bytes string
print("--------------------------------------------------------------------")
#POST
data = parse.urlencode({"name":"Bob", "age":12})
data =data.encode("utf-8")
req = request.Request("https://httpbin.org/post", data=data)
response2 = request.urlopen(req,data=data)
print(response2.read().decode())# { "args": {},..............
#region REQUEST
#request object to build more complex HTTP requests, 
# class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
#url should be a string containing a valid, properly encoded URL
# data is obj or None 
# headers should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments
url = "https://httpbin.org/get"
headers = {'User-Agent': 'MyApp/1.0'}
print("--------------------------------------------------------------------")
req = request.Request(url, headers=headers)
#with statements open a resource and guarantee that the resource will be closed when the with block completes, regardless of how the block completes
with request.urlopen(req) as resp:
    print(response.status)
    print(response.read().decode())
#region RESPONSE
#After calling urlopen(), you get a response object with:
  #.read() → response body (bytes)
  #.status → HTTP status code (int)
  #.getheader('Content-Type') → header value
  #.headers → all headers
  #.url → final URL (after redirects)
#region PARSE
#Used to manipulate URLs and query strings.
print("--------------------------------------------------------------------")
url = "https://www.example.com:8080/path/page.html?query=python#section"
parts = parse.urlparse(url)
print(parts) #ParseResult( scheme='https', netloc='www.example.com:8080', path='/path/page.html', params='', query='query=python', fragment='section')
print("--------------------------------------------------------------------")
parts_List =('https', 'example.com','/path/page.html', '', 'query=python','section')
print(parse.urlunparse(parts_List))#"https://example.com/path/page.html?query=python&section
print("--------------------------------------------------------------------")
#region ERROR
# Contains exceptions raised by urllib.request. URLError: Base exception for URL-related errors 
# HTTPError: Subclass of URLError, raised for HTTP-specific errors (like 404, 500).
try:
    request.urlopen("https://www.example.com/404")
except HTTPError as e:
   print("HTTP error:", e.code)
except URLError as e:
    print("URL error:", e.reason)

