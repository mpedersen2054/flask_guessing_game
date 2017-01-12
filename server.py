from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'asecretkey'

@app.route('/')
def handle_index():
  if not 'rand_numb' in session:
    session['rand_numb'] = random.randrange(0, 101)
    session['guess_state'] = ''
    session['error'] = ''
  return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_submit():
  print request.form['number'], session['rand_numb']

  try:
    guess = int(request.form['number'])
  except ValueError:
    guess = False

  if guess:
    session['error'] = ''
    print "guess was a number!!!"
    if guess == session['rand_numb']:
      session['guess_state'] = 0
    elif guess < session['rand_numb']:
      session['guess_state'] = -1
    elif guess > session['rand_numb']:
      session['guess_state'] = 1
  else:
    session['error'] = 'Please enter a number, bro.'
    session['guess_state'] = ''

  return redirect('/')

@app.route('/playagain', methods=['POST'])
def play_again():
  session.pop('rand_numb')
  return redirect('/')


app.run(debug=True)
