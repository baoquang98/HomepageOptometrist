import urllib.request

def get_html_at_url(url,charset="UTF-8"):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'PurdueUniversityClassProject/1.0 (nguye279@purdue.edu https://goo.gl/dk8u5S)')
    response = urllib.request.urlopen(req)
    response = response.read()
    return response.decode(charset)

def make_etree(html, url):
    from lxml.html import HTMLParser, document_fromstring
    parser = HTMLParser(encoding="UTF-8")
    root = document_fromstring(html, parser = parser, base_url = url)
    return root

def make_outline(etree):
    res_string = ""
    #tag_list = ["h1", "h2", "h3"]
    for node in etree.iter():
        #if node.tag in tag_list:
            #white_space = tag_list.index(node.tag) * "    "
            res_string = res_string + str(node)
    return res_string
import re
def check_url(url):
    not_valid = [r"facebook", r"instagram", r"twitter", r"linkdin", "google+"]
    url = url.lower()
    for i in not_valid:
        found = re.search(i, url)
        if found != None:
            return False
    return True
#
# url = "http://alexquinn.org"
# html = get_html_at_url(url)
# print(html)
# new = ""
# for i in html:
#     if i == "<img":
#         i = "<base"
#     new = new + i

#root = make_etree(html, url)
#outline = make_outline(root)
#print(outline)
import os
import flask
app = flask.Flask(__name__)

@app.route('/')
def root_page():
    return flask.render_template('root.html')

@app.route("/outline")
def view_page():
    url = flask.request.args.get("url")
    if (check_url(url)):
        html = get_html_at_url(url)
        line = 0
        index = 0
        for i in html:
            if i == '\n':
                line = line + 1
            index = index + 1
            if line == 3:
                break
        html = html[:index] + "<base href='" + url + "'>\n" + html[index:]
    else:
        html = "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Home Page Optometris</title></head><body><h1>Please do not use social network site</h1><p1>Social network site included but not limited to:<br>Press back to try again</p1></body></html>"
    return html
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=os.environ.get("ECE364_HTTP_PORT", 8000),
            use_reloader=True, use_evalex=False, debug=True, use_debugger=False)
    # Each student has their own port, which is set in an environment variable.
    # When not on ecegrid, the port defaults to 8000.  Do not change the host,
    # use_evalex, and use_debugger parameters.  They are required for security.
    #
    # Credit:  Alex Quinn.  Used with permission.  Preceding line only.

