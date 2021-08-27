from flask import Flask,render_template, request
import requests

def Translator(url):
  _VERSION = 1

  querystring = {
    "filename":"sample.jpg","imageurl": url
  }

  headers = {
      'x-rapidapi-host': "ocrly-image-to-text.p.rapidapi.com",
      'x-rapidapi-key': ""
      }

  response = requests.request("GET", "https://ocrly-image-to-text.p.rapidapi.com/", headers=headers, params=querystring)

  return response.text

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def page():
        if request.method == "GET":
            return render_template('mtemp.html')
        else:
            url = request.form['text']
            print(url)
            text = Translator(url)
            print(text)
            return render_template('mtemp.html', li = text, url=url)


if __name__ == '__main__':
    app.run(debug=True)