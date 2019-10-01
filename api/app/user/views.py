import json
from flask import redirect, render_template, request, jsonify
from sqlalchemy import or_

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
        search_str = request.args.get('s', default='', type=str)
        print('Search String: {}'.format(search_str))
 
        q = User.query

        try:
            (t1, t2) = search_str.split('-', 1)
        except Exception as e:
            try:
                age = int(search_str)
            except Exception as e:
                if 'male' == search_str.lower() or 'female' == search_str.lower():
                    q = q.filter_by(gender=search_str.lower())
                elif search_str:
                    q = q.filter(or_(User.firstname.like('%{}%'.format(search_str)), \
                        User.lastname.like('%{}%'.format(search_str)), \
                        User.email.like('%{}%'.format(search_str)) \
                    ))
            else:
                if age:
                    q = q.filter_by(age=age)
        else:
            if t1 and t2:
                age_start = int(t1)
                age_end = int(t2)
                if age_start:
                    q = q.filter(User.age >= age_start).filter(User.age <= age_end)

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


@user.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    form = json.loads(request.data)
    print('Update: ' + str(form))
    firstname = form['firstname']
    lastname = form['lastname']
    email = form['email'].lower()
    age = int(form['age'])
    gender = form['gender'].lower()

    try:
        # Get user by ID
        data = User.query.filter_by(id=user_id).first()
        if data.firstname != firstname:
            data.firstname = firstname
        if data.lastname != lastname:
            data.lastname = lastname
        if data.email != email:
            data.email = email
        if data.age != age:
            data.age = age
        if data.gender != gender:
            data.gender = gender
        db.session.commit()

        return jsonify(data.to_serializable_dict())
    except Exception as e:
        print(e)
        message = {'message': 'Something went wrong'}
        return jsonify(message), 500


@user.route('/users/<user_id>', methods=['DELETE'])
def remove_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        print('Cannot remove user iD {}'.format(user_id))
        print(e)
        message = {'message': 'Cannot remove user ID {}'.format(user_id)}
        return jsonify(message), 500
    else:
        data = User.query.all()
        return jsonify(User.to_serializable_list(data))
