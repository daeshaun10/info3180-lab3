from app import app
from flask import render_template, request, redirect, url_for, flash
from .forms import ContactForm
from app import mail
from flask_mail import Message
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

## ------------------------- contact route ------------------------------------- ##

@app.route('/contact/', methods=('GET', 'POST'))
def contact():
    form = ContactForm() ## assigned contact form to a form variable
    if request.method == 'POST' and form.validate_on_submit(): 
        ## this portion of code only works when request method is POST and form is successfully validated (means all fields are filled)

        ## creating the message body and taking data from request method
        ## 1. request.form['subject'] -- subject field data of form 
        ## 2. request.form['name'] -- name field data of form 
        ## 3. request.form['email'] -- email field data of form 
        ## 4. request.form['msg'] -- msg field data of form 
        subject = request.form["subject"]
        to = "to@example.com"
        name = request.form["name"]
        sender_email = request.form['email']
        message_body = request.form['msg']

        ## creating message with parameters
        msg = Message(subject,  
                  sender=(name, sender_email),
                  recipients=[to])

        msg.body = message_body ## attaching body to message
        mail.send(msg) ## send the message using flask_mail

        ## flashing the message and redirecting to the homepage
        flash('Thank you for contacting.')
        return redirect(url_for("home"))

    ## if above process fails the only contact form will be displayed again   
    return render_template('contact.html', form=form)

## ------------------------------------------------------------------------------##


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
