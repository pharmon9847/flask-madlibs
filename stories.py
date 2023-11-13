"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    'history',
    'A most historic tale',
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    'No way!',
    'A story of Princes and Princesses',
    ['place', 'noun', 'verb', 'adjective', 'adjective2', 'name', 'color',
        'day_of_week', 'season', 'number', 'animal', 'number2', 'adjective3', 'adjective4', 'adjective5',
        'adjective6', 'adjective7', 'adjective8', 'adjective9', 'adjective10', 'adjective11', 'adjective12', 'adjective13'],
    """A long time ago, in a {adjective} galaxy, there lived {number} {adjective2} 
        princes and a {number2} {adjective3} princesses. 
        On {day_of_week}s in {season}, 
        the {adjective4} princes would wear {color} clothes and go into the {adjective5}
        forest to look for {adjective6} {animal}s that they called {name}. 
        The {adjective7} princesses thought this was a {adjective8} idea, 
        so the would stay in the {adjective9} castle. 
        At the end of the {adjective10} day, 
        the {adjective11} princes and the {adjective12} princesses
        would meet at the {adjective13} {place} and {verb}."""
)

stories = {s.code: s for s in [story1, story2]}
