import json
from flask import redirect, render_template, request, jsonify

from . import user
from app import db
from app.user.models import User


@user.route('/register', methods=['POST'])
def add_user():
    form = json.loads(request.data)
    print('Register: ' + str(form))
    firstname = form['firstname']
    lastname = form['lastname']
    email = form['email'].lower()
    age = form['age']
    gender = form['gender'].lower()

    try:
        if User.query.filter_by(email=email).first():
            message = {'message': 'User {} already exists'.format(email)}
            return jsonify(message), 500
        else:
            new_user = User(firstname=firstname, 
                lastname=lastname, email=email, age=age, gender=gender)
            db.session.add(new_user)
            db.session.commit()

            response = {
                'message': 'User {} was created'.format(new_user.firstname),
                'id': new_user.id
                }
            return jsonify(response)
    except Exception as e:
        print(e)
        message = {'message': 'Something went wrong'}
        return jsonify(message), 500


@user.route('/users', methods=['GET'])
def list_user():
    try:
        firstname = request.args.get('firstname', default='', type=str)
        lastname = request.args.get('lastname', default='', type=str)
        email = request.args.get('email', default='', type=str)
        age = request.args.get('age', default=0, type=int)
        age_start = request.args.get('age_start', default=0, type=int)
        age_end = request.args.get('age_end', default=200, type=int)
        gender = request.args.get('gender', default='', type=str)
 
        q = User.query
        if firstname:
            q = q.filter(User.firstname.like('%{}%'.format(firstname)))

        if lastname:
            q = q.filter(User.lastname.like('%{}%'.format(lastname)))

        if email:
            q = q.filter(User.email.like('%{}%'.format(email)))

        if age_start:
            q = q.filter(User.age >= age_start).filter(User.age <= age_end)
        elif age:
            q = q.filter_by(age=age)

        if gender:
            q = q.filter_by(gender=gender.lower())

        data = q.all()
        return jsonify(User.to_serializable_list(data))
    except Exception as e:
        print(e)
        message = {'message': 'Something went wrong'}
        return jsonify(message), 500


@user.route('/users/<user_id>', methods=['GET'])
def show_user(user_id):
    try:
        # Get user by ID
        data = User.query.filter_by(id=user_id).first()
        return jsonify(data.to_serializable_dict())
    except Exception as e:
        print(e)
        message = {'message': 'Cannot get user ID {}'.format(user_id)}
        return jsonify(message), 500


@user.route("/delete", methods=["POST"])
def remove_user():
    try:
        form = json.loads(request.data)
        user_id = form['id']

        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        print('Cannot remove user iD {}'.format(user_id))
        print(e)
        message = {'message': 'Cannot remove user ID {}'.format(user_id)}
        return jsonify(message), 500

    return redirect("/users")
