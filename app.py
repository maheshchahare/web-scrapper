from flask import Flask, render_template, request, jsonify
import urllib.request
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')


@app.route('/report', methods=['POST'])  # This will be called from UI
def web_scrapping():
    if request.method == 'POST':
        while True:
            try:
                link = str(request.form['link'])
            except:
                continue
            else:
                break
        # Fetch the html file
        response = urllib.request.urlopen(link)
        html_doc = response.read()

        # Parse the html file
        soup = BeautifulSoup(html_doc, 'html.parser')

        # Format the parsed html file
        # string_html = soup.prettify()
        alice = ''
        for x in soup.find_all('p'):
            try:
                temp = x.string
                if temp[-1] == '.':
                    alice = alice + temp.replace("\r\n", '') + " "
                else:
                    alice = alice + temp.replace("\r\n", '') + '.' + " "

            except:
                None

        result = alice
        return render_template('results.html', result=result)


if __name__ == '__main__':
    app.run()
