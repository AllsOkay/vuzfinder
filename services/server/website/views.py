from flask import Blueprint, request, url_for, render_template, redirect, flash
import logging

from database.models import db, User, Uni, Quiz

website = Blueprint('website', __name__)

@website.route('/')
def index():
    return render_template('start.html')

@website.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        result_uni = Uni.query.filter_by(region=request.form['1']).\
        filter(Uni.areas.contains(request.form['3'])).\
        filter(Uni.eg_score.contains(request.form['2'])).\
        filter(Uni.price.contains(request.form['4']))
        
        return render_template('result.html', result_uni=result_uni)

    if request.method == 'GET':
        questions = Quiz.query
        return render_template('quiz.html', questions=questions)

@website.route('/uni_info/<id>', methods=["GET"])
def uni_info(id):
    uni_id = int(id)
    uni_details = Uni.query.filter(Uni.id == int(id))
    return render_template('uni_info.html', uni_details=uni_details)