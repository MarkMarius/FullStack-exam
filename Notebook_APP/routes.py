from notebook_app import app, db, bcrypt
from notebook_app.models import User, Notes, Categories
from notebook_app.forms import RegistrationForm, LoginForm, UpdateAccountForm, UpdateNoteForm, NewCategoryForm, SearchForm

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required

def a_current_user():
    superuser =  User.query.filter_by(username='superuser').first()
    return superuser


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if (email and password):
            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(url_for(next_page)) if next_page else redirect(url_for('home'))
            else:
                flash('Login unsuccessfull, Please check email and password', 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = NewCategoryForm()
    user_notes = User.query.get(current_user.id)
    notes = user_notes.notes
    users_categories = user_notes.categories

    for note in notes:
        print(note.date_saved)
    if request.method == 'POST':
        category_data = request.form['category']
        notes_data = request.form['notes']
        if category_data and notes_data:
            note = Notes(categories=category_data, notes=notes_data, author=current_user)
            db.session.add(note)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('home.html', notes=notes, users_categories=users_categories, form=form, superuser=a_current_user(), title='Summary-Notebook')


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    searched = form.searched.data
    category = Categories.query
    note = Notes.query.filter_by(user_id=id)
    if form.validate_on_submit():
        category = category.filter(Categories.name.like('%' + searched + '%'))
        note = Notes.order_by().all()
        return redirect(url_for('search'), form=form, category=category, note=note)
    return render_template("search.html", user=current_user, notes=note, form=form, categories=category)


@app.route('/update/<int:note_id>', methods=['GET', 'POST'])
@login_required
def update(note_id):
    note = Notes.query.get(note_id)
    form = UpdateNoteForm()

    if form.validate_on_submit():
        categories = form.category.data
        notes = form.notes.data
        if (categories and notes):
            note.categories = form.category.data
            note.notes = form.notes.data
            db.session.commit()
            flash("Note updated successfull", "success")
            return redirect(url_for('home'))
    elif request.method == 'GET':
        form.category.data = note.categories
        form.notes.data = note.notes
    return render_template('update.html', note=note, title="Update", form=form)


@app.route('/note/<int:note_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_note(note_id):
    note = Notes.query.get(note_id)
    db.session.delete(note)
    db.session.commit()
    flash("Your note have been deleted", "success")
    return redirect(url_for('home'))


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    form = NewCategoryForm()

    if form.validate_on_submit():
        new_category_data = form.categories_name.data
        if new_category_data:
            category = Categories(categories_name=new_category_data, category_author=current_user)
            db.session.add(category)
            db.session.commit()
            flash("New category added", "success")
            return redirect(url_for('home'))


@app.route('/delete_category/<int:category_id>', methods=['GET', 'POST'])
def delete_category(category_id):
    user_subj = Categories.query.get(category_id)
    db.session.delete(user_subj)
    db.session.commit()
    flash("Category deleted successfully", "success")
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if (username and email and password):
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username, email=email, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash("Welcome. Now you can login", "success")
        return redirect(url_for('login'))

    return render_template('register.html', title="Register", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/account/<int:user_id>', methods=['GET', 'POST'])
@login_required
def account(user_id):
    user = User.query.get(user_id)
    form = UpdateAccountForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        if username:
            user.username = username
            user.email = email
            db.session.commit()
            flash("Your account has been updated", "success")
            return redirect(url_for('account', user_id=user.id))
        if email:
            user.username = username
            user.email = email
            db.session.commit()
            flash("Your account has been updated", "success")
            return redirect(url_for('account', user_id=user.id))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', title="Account", form=form)









