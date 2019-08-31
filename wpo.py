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
    tag_list = ["h1", "h2", "h3"]
    for node in etree.iter():
        if node.tag in tag_list:
            white_space = tag_list.index(node.tag) * "    "
            res_string = res_string + white_space + node.text_content() + "\n"
    return res_string

# url = "http://alexquinn.org"
# html = get_html_at_url(url)
# root = make_etree(html, url)
# outline = make_outline(root)
# print(outline)
import os
import flask
app = flask.Flask(__name__)

@app.route('/')
def root_page():
    return flask.render_template('root.html')

@app.route("/outline")
def outline_view():
    url = flask.request.args.get("url")
    html = get_html_at_url(url)
    root = make_etree(html, url)
    outline = make_outline(root)
    return "<pre>"+ outline + "</pre>"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=os.environ.get("ECE364_HTTP_PORT", 8000),
            use_reloader=True, use_evalex=False, debug=True, use_debugger=False)
    # Each student has their own port, which is set in an environment variable.
    # When not on ecegrid, the port defaults to 8000.  Do not change the host,
    # use_evalex, and use_debugger parameters.  They are required for security.
    #
    # Credit:  Alex Quinn.  Used with permission.  Preceding line only.

