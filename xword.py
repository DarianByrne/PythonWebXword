## with open("static/words") as wf:
with open("static/words-huge") as wf:
    words = {line.strip("\n").replace("'s", "").lower() for line in wf}  # A set.
words = sorted(words)[1:]  # Ignore the empty word at the start of the list.


def find_possible_matches(pattern):
    """Given any pattern of the type "__a___b__c", this function
    looks up and returns all the potential matches for the
    pattern in the dictionary of words."""

    def match_pattern(w, p):
        """Returns True if 'w' matches 'p', False otherwise."""
        letters = {k: v for k, v in enumerate(p) if v != "_"}
        return not any([w[i] != p[i] for i in letters.keys()])

    pattern = pattern.lower()  # Just in case.
    matches = {
        word  ## SELECT...
        for word in words  ## FROM...
        if len(word) == len(pattern) and match_pattern(word, pattern)  ## WHERE...
    }
    return sorted(matches)


def matches(pattern):
    """Return sorted matches as well as count of same."""
    data = find_possible_matches(pattern)
    return sorted(data), len(data)
