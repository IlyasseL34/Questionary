from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/summary', methods=['POST'])
def submit():
    form_data = request.form.to_dict()  # getting data from form
    return render_template('summary.html', form_data=form_data)  # we pass data as 'form_data'

if __name__ == '__main__':
    app.run(debug=True)
