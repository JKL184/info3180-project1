"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort,send_from_directory
from werkzeug.utils import secure_filename
from .forms import PropertyForm
from app.models import Property
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
    return render_template('about.html', name="Jordan Lewis")


@app.route('/property', methods=['POST', 'GET'])
def newProperty():
    # Instantiate your form class
    form=PropertyForm()
    # Validate file upload on submit
    if request.method == 'POST':
        if form.validate_on_submit():
        # Get file data and save to your uploads folder
            title=form.title.data
            desc=form.desc.data
            room =form.room.data
            bathroom =form.bathroom.data
            price=form.price.data
            proptype=form.proptype.data
            location=form.location.data
            photo=form.photo.data
            filename=secure_filename(photo.filename)
            prop=Property(title=title,desc=desc,room=room,bathroom=bathroom,price=price,proptype=proptype,location=location,photo=filename)
            if prop is not None:
                db.session.add(prop)
                db.session.commit()
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('Property Added Succesfully.','success') 
                return redirect(url_for("properties"))
            else:
                flash('Property was not added.','danger')
    return render_template('new_property.html', form=form)



@app.route("/property/<propertyid>")
def get_property(propertyid):
    prop = Property.query.filter_by(id=propertyid).first()
    return render_template('property.html', prop=prop)

@app.route("/properties")
def properties():
    props=Property.query.all()
    return render_template('properties.html', props=props)


@app.route("/uploads/<filename>")
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

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
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
