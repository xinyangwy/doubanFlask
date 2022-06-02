from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    return render_template("index.html")


@app.route('/movie')
def movie():
    movies_list = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"  # 数据库中表的名字
    data = cur.execute(sql)
    for item in data:
        movies_list.append(item)
    cur.close()
    con.close()
    return render_template("movie.html", movies=movies_list)


@app.route('/score')
def score():
    score_list = []
    num_list = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score_list.append(item[0])
        num_list.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html", score=score_list, num=num_list)


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
