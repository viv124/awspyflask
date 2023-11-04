from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

schools = {
    1: {"name": "School A", "location": "City A"},
    2: {"name": "School B", "location": "City B"},
    3: {"name": "School C", "location": "City C"},
}

@app.route('/')
def home():
    return render_template('index.html', schools=schools)

@app.route('/result', methods=['POST'])
def result():
    marks = int(request.form['marks'])
    school_id = int(request.form['school'])

    school = schools.get(school_id)
    school_name = school['name']
    school_location = school['location']

    result = "Pass" if marks >= 50 else "Fail"

    return render_template('result.html', marks=marks, school_name=school_name, school_location=school_location, result=result)

if __name__ == '__main__':
    app.run(debug=True)
