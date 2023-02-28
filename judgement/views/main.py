"""Main."""

import flask
import judgement
from flask import Flask
from flask import render_template

@judgement.app.route("/")
def main_page():
    return render_template('mainpage.html')