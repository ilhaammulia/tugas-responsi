from flask import Flask, request, redirect, render_template
import models
import user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'inisecretkey123@'

session = None


@app.route('/', methods=['GET', 'POST'])
def index():
    global session
    form = models.LoginForm()
    if request.method == 'POST':
        if form.validate():
            email = form.email.data
            password = form.password.data
            if (email == user.EMAIL) and (password == user.PASSWORD):
                session = user.NAME
                return redirect('/landing')
            else:
                return render_template('login.html', form=form, auth_error=True)
        else:
            errors = form.errors.items()
            return render_template('login.html', form=form, errors=errors)
    return render_template('login.html', form=form)


@app.route('/landing')
def landing():
    if session is None:
        return redirect('/')
    return render_template('landing.html', session=session)


@app.route('/logout')
def logout():
    global session
    session = None
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
