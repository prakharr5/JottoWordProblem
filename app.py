from flask import Flask, render_template, request, jsonify
from game.threewordSolver import threewordSolver
from game.fourwordSolver import fourwordSolver
from game.fivewordSolver import fivewordSolver
from game.sixwordSolver import sixwordSolver
from game.threeuniwordSolver import threeuniwordSolver
from game.fouruniwordSolver import fouruniwordSolver
from game.fiveuniwordSolver import fiveuniwordSolver
from game.sixuniwordSolver import sixuniwordSolver

app = Flask(__name__)

threewordSolver = threewordSolver(word_length=3)
fourwordSolver = fourwordSolver(word_length=4)
fivewordSolver = fivewordSolver(word_length=5)
sixwordSolver = sixwordSolver(word_length=6)
threeuniwordSolver = threeuniwordSolver(word_length=3)
fouruniwordSolver = fouruniwordSolver(word_length=4)
fiveuniwordSolver = fiveuniwordSolver(word_length=5)
sixuniwordSolver = sixuniwordSolver(word_length=6)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/three")
def three():
    return render_template("three.html", guess=threewordSolver.current_guess, possible_words=len(threewordSolver.possible_words))

@app.route("/three/guess", methods=["POST"])
def three_guess():
    feedback = request.json.get("feedback")
    if feedback is None or not isinstance(feedback, int):
        return jsonify({"error": "Invalid feedback"}), 400

    possible_words, next_guess = threewordSolver.process_feedback(feedback)
    return jsonify({
        "remaining_words": len(possible_words),
        "next_guess": next_guess,
        "possible_words": possible_words if len(possible_words) <= 10 else []
    })
    
@app.route("/four")
def four():
    return render_template("four.html", guess=fourwordSolver.current_guess, possible_words=len(fourwordSolver.possible_words))

@app.route("/four/guess", methods=["POST"])
def four_guess():
    feedback = request.json.get("feedback")
    if feedback is None or not isinstance(feedback, int):
        return jsonify({"error": "Invalid feedback"}), 400

    possible_words, next_guess = fourwordSolver.process_feedback(feedback)
    return jsonify({
        "remaining_words": len(possible_words),
        "next_guess": next_guess,
        "possible_words": possible_words if len(possible_words) <= 10 else []
    })
    
@app.route("/five")
def five():
    return render_template("five.html", guess=fivewordSolver.current_guess, possible_words=len(fivewordSolver.possible_words))

@app.route("/five/guess", methods=["POST"])
def five_guess():
    feedback = request.json.get("feedback")
    if feedback is None or not isinstance(feedback, int):
        return jsonify({"error": "Invalid feedback"}), 400

    possible_words, next_guess = fivewordSolver.process_feedback(feedback)
    return jsonify({
        "remaining_words": len(possible_words),
        "next_guess": next_guess,
        "possible_words": possible_words if len(possible_words) <= 10 else []
    })
    
@app.route("/six")
def six():
    return render_template("six.html", guess=sixwordSolver.current_guess, possible_words=len(sixwordSolver.possible_words))

@app.route("/six/guess", methods=["POST"])
def six_guess():
    feedback = request.json.get("feedback")
    if feedback is None or not isinstance(feedback, int):
        return jsonify({"error": "Invalid feedback"}), 400

    possible_words, next_guess = sixwordSolver.process_feedback(feedback)
    return jsonify({
        "remaining_words": len(possible_words),
        "next_guess": next_guess,
        "possible_words": possible_words if len(possible_words) <= 10 else []
    })
    
@app.route("/threeuni")
def threeuni():
    return render_template("threeuni.html", guess=threeuniwordSolver.current_guess, possible_words=len(threeuniwordSolver.possible_words))

@app.route("/threeuni/guess", methods=["POST"])
def threeuni_guess():
    feedback = request.json.get("feedback")
    if feedback is None or not isinstance(feedback, int):
        return jsonify({"error": "Invalid feedback"}), 400

    possible_words, next_guess = threeuniwordSolver.process_feedback(feedback)
    return jsonify({
        "remaining_words": len(possible_words),
        "next_guess": next_guess,
        "possible_words": possible_words if len(possible_words) <= 10 else []
    })
    
@app.route("/fouruni")
def fouruni():
    return render_template("fouruni.html", guess=fouruniwordSolver.current_guess, possible_words=len(fouruniwordSolver.possible_words))

@app.route("/fouruni/guess", methods=["POST"])
def fouruni_guess():
    feedback = request.json.get("feedback")
    if feedback is None or not isinstance(feedback, int):
        return jsonify({"error": "Invalid feedback"}), 400

    possible_words, next_guess = fouruniwordSolver.process_feedback(feedback)
    return jsonify({
        "remaining_words": len(possible_words),
        "next_guess": next_guess,
        "possible_words": possible_words if len(possible_words) <= 10 else []
    })
    
@app.route("/fiveuni")
def fiveuni():
    return render_template("fiveuni.html", guess=fiveuniwordSolver.current_guess, possible_words=len(fiveuniwordSolver.possible_words))

@app.route("/fiveuni/guess", methods=["POST"])
def fiveuni_guess():
    feedback = request.json.get("feedback")
    if feedback is None or not isinstance(feedback, int):
        return jsonify({"error": "Invalid feedback"}), 400

    possible_words, next_guess = fiveuniwordSolver.process_feedback(feedback)
    return jsonify({
        "remaining_words": len(possible_words),
        "next_guess": next_guess,
        "possible_words": possible_words if len(possible_words) <= 10 else []
    })
    
@app.route("/sixuni")
def sixuni():
    return render_template("sixuni.html", guess=sixuniwordSolver.current_guess, possible_words=len(sixuniwordSolver.possible_words))

@app.route("/sixuni/guess", methods=["POST"])
def sixuni_guess():
    feedback = request.json.get("feedback")
    if feedback is None or not isinstance(feedback, int):
        return jsonify({"error": "Invalid feedback"}), 400

    possible_words, next_guess = sixuniwordSolver.process_feedback(feedback)
    return jsonify({
        "remaining_words": len(possible_words),
        "next_guess": next_guess,
        "possible_words": possible_words if len(possible_words) <= 10 else []
    })

if __name__ == "__main__":
    app.run(debug=True)