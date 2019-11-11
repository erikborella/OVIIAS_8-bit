from flask import session

def add(id):
    session['id'] = id

def remove():
    session['id'] = None

def is_logged():
    return session['id'] is not None

def get():
    return session['id']