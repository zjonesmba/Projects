from flask import Flask, jsonify, request

app = Flask(__name__)

Marvel = [ {'Title': "Captain America: The First Avenger",
             'Year': "2011",
             'See More': "https://www.google.com/search?q=Captain+America%3A+First+Avenger&rlz=1C1CHBF_enUS944US944&oq=Captain+America%3A+First+Avenger&aqs=chrome..69i57.328j0j9&sourceid=chrome&ie=UTF-8",
             'IMDB': "https://www.imdb.com/title/tt0458339/"},
             {'Title': "Captain Marvel",
              'Year': "2019",
              'See More': "https://www.google.com/search?gs_ssp=eJzj4tbP1TcwNDJLsrBINmD0EklOLChJzMxTyE0sKkvNUcjNL8tMBQC0JQs1&q=captain+marvel+movie&rlz=1C1CHBF_enUS944US944&oq=captain+marvel&aqs=chrome.4.69i57j46i67i433j0i67i433j46i67i131i433j46i67i433j0i433i512j0i512j0i433i512j0i131i433j0i433i512.7186j0j4&sourceid=chrome&ie=UTF-8",
              'IMDB': "https://www.imdb.com/title/tt4154664/"},
              {'Title': "Iron Man",
              'Year': "2008",
              'See More': "https://www.google.com/search?q=Iron+Man+1&rlz=1C1CHBF_enUS944US944&biw=1920&bih=937&sxsrf=ALiCzsYkJSoDeTVwyqoPJUGCPS2aJAtuOw%3A1657941910761&ei=li_SYsWDLojBkPIP56GgyAc&ved=0ahUKEwjFppj1uvz4AhWIIEQIHecQCHkQ4dUDCA4&oq=Iron+Man+1&gs_lcp=Cgdnd3Mtd2l6EAxKBAhBGABKBAhGGABQAFgAYABoAHABeACAAQCIAQCSAQCYAQA&sclient=gws-wiz",
              'IMDB': "https://www.imdb.com/title/tt0371746/"}, 
              {'Title': "Iron Man 2",
              'Year': "2010",
              'See More': "https://www.google.com/search?q=iron+man+2&rlz=1C1CHBF_enUS944US944&biw=1920&bih=937&sxsrf=ALiCzsZpoVHkF3jO7Orb6T6gsG-iDmCbJg%3A1657941916658&ei=nC_SYt7jJ9zUkPIPl_S72Ak&gs_ssp=eJzj4tLP1TcwLUxKzk4zYPTiyizKz1PITcxTMAIAWjcHNw&oq=Iron+Man+2&gs_lcp=Cgdnd3Mtd2l6EAEYADIICC4QsQMQkQIyBQgAEIAEMgUIABCRAjIICC4QgAQQsQMyCggAEIAEELEDEAoyBQgAEIAEMgUILhCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToPCC4Q1AIQyAMQsAMQQxgCOgQIABBDOggIABCABBCxAzoFCC4QsQNKBAhBGABKBAhGGAFQtgFYgQNggQxoAXABeACAAYUBiAGCApIBAzAuMpgBAKABAcgBEMABAdoBBggBEAEYCdoBBggCEAEYCA&sclient=gws-wiz",
              'IMDB': "https://www.imdb.com/title/tt1228705/"}
            ]

# Creates the server
@app.route('/') # Create a URL to invoke the index function
def index():
    return "Welcome To The Course API"

#This return the entire Marvel database (or list(dictionary))
@app.route("/marvel", methods=['GET']) # This creates the /marvel URL to invoke the get method on the HTTP
def get():
    return jsonify({'marvel':Marvel}) # This quoted 'marvel' needs to match the route "/marvel" above

#This is how you use the Headers of HTTP to return specific values
@app.route("/marvel/<int:Title>", methods=['GET'])
def get_title(Title):
    return jsonify({'marvel':Marvel[Title]})


# POST method to add a new title to the database
# To invoke use the following command in the terminal: curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/marvel
@app.route("/marvel", methods=['POST'])
def create():
    NewTitle = {'Title': "The Incredible Hulk",
              'Year': "2008",
              'See More': "https://www.google.com/search?gs_ssp=eJzj4tTP1TdIycvOLTRg9BIuyUhVyMxLLkpNyUzKSVXIKM3JBgCrnAr-&q=the+incredible+hulk&rlz=1C1CHBF_enUS944US944&oq=the+inc&aqs=chrome.1.0i67i355i433j46i67i433j46i67j46i433i512j69i57j0i512j46i433i512j69i65.5378j0j4&sourceid=chrome&ie=UTF-8",
              'IMDB': "https://www.imdb.com/title/tt0800080/"}
    Marvel.append(NewTitle)
    return jsonify({'Created':NewTitle})


# PUT method to update the "See More" in the Marvel database
# To invoke use the following command in the terminal: curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/marvel/4
# 4 indiates the index of Marvel (so use the POST method first)
@app.route("/marvel/<int:SeeMore>", methods=['PUT'])
def update(SeeMore):
    Marvel[SeeMore]['See More'] = 'XYZ'
    return jsonify({'Updated':Marvel[SeeMore]})

# DELETE method to delete an entry in the Marvel database
# To invoke use the following command in the terminal: curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/marvel/4
# 4 indiates the index of Marvel (so use the POST method first to create it)
@app.route("/marvel/<int:Title>", methods=['DELETE'])
def delete(Title):
    Marvel.remove(Marvel[Title])
    return jsonify({'Result':True})

if __name__ == "__main__":
    app.run(debug=True)



