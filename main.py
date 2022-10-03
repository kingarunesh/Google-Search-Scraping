from flask import Flask, render_template, request
from search_query import search_engine


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("search")
        results = search_engine(search=query)

        titles = results[0]
        links = results[1]
        texts = results[2]

        print(len(titles))
        print(len(links))
        print(len(texts))

        loop_length = [len(titles), len(links), len(texts)]

        cards = []
        for i in range(min(loop_length)):
            cards.append({
                "title":titles[i],
                "link":links[i],
                "text":texts[i]
                })
        
        print(cards)

        return render_template("index.html", cards=cards)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
