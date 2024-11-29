from flask import Flask, render_template, request,redirect,url_for,make_response, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'esunsecreto'

@app.route('/')
def index():
    consent = request.cookies.get('cookie_consent')
    return render_template('index.html', consent=consent)
@app.route("/privacy-policy")
def privacy_policy():
    return render_template("privacy_policy.html")

@app.route('/consent',methods=['GET','POST'])
def consent():
    if request.method == 'POST':
        consent_value = request.form.get('consent')
        response = make_response(redirect(url_for('index')))
        if consent_value == "accept":
            response.set_cookie("cookie_consent","accepted", max_age=365*24*60*60)
        elif consent_value == "reject":
            response.set_cookie("cookie_consent","rejected", max_age=365*24*60*60)
        flash("Your preferences have been saved")
        return response
    return render_template("consent.html")


if __name__ == '__main__':
    app.run(debug=True)

