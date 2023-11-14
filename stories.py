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
    ['adjective', 'name', 'adjective2', 'animal', 'adjective3',
        'name2', 'verb', 'adjective4', 'city', 'activity'],
    """Once there was a {adjective} prince named {name}. He loved to hunt {adjective2} {animal}s. He had a {adjective3} sister named {name2}. Sometimes the two of them would {verb} through the {adjective4} forest. Sometimes they would travel to {city} and {activity}."""
)

stories = {s.code: s for s in [story1, story2]}
