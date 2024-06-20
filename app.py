from flask import Flask, request, render_template, jsonify,session
from boggle import Boggle

app=Flask(__name__)
app.config["SECRET KEY"] = "keyissecret"


boggle_game = Boggle()

@app.route("/")
def homepage():
    """this is should the home page"""
    
    board= boggle_game.make_board()
    session['board']= board 
    highscore= session.get("highsore",0)
    nplays = session.get("nplays",0)
    
    return render_template("index.html", board=board,
                           highscore=highscore,
                           nplays=nplays)
    
@app.route("/checkword")
def checkword():
    """this should check if word is in dictionary"""
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board,word)
    
    return jsonify({'result: response'})

@app.route("/post-score", methods=["POST"])
def post_score():
    """ Receive sccore, update nplays, update highscore if appropriate."""
    
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays ,0")
    
    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)
    
    return jsonify(BrokeRecord=score>score)
    