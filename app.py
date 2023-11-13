from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsADumbSecretKey1'

debug = DebugToolbarExtension(app)


@app.route('/')
def ask_story():
    """Show list of stories form
    """
    return render_template('choose-story.html', stories=stories.values())


@app.route('/questions')
def ask_questions():
    """generate and show the form to ask for the words
    """
    story_id = request.args['story_id']
    story = stories[story_id]

    prompts = story.prompts

    return render_template('questions.html', story_id=story_id, title=story.title, prompts=prompts)


@app.route('/story')
def show_story():
    """show the story based on the questions asked
    """
    story_id = request.args['story_id']
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template('story.html', title=story.title, text=text)
