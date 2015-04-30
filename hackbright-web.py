from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)



@app.route("/")
def get_student_form():
    """Show form for searching for a student."""
    
    return render_template("student_search.html")

@app.route('/student-add', methods=["POST"])
def student_add():
    """add a new student"""

    first, last, github = hackbright.make_new_student(first_name, last_name, github)
    
    
@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github',)
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
        first=first,
        last=last,
        github=github)
    return html






if __name__ == "__main__":
    app.run(debug=True)