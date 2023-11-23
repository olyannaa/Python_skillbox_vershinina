import re

def valid_color(color):

    """Return False in case incorrect color.
    Return True if color is correct.


    >>> valid_color('#21f48D')
    True
    >>> valid_color('#888')
    True
    >>> valid_color('rgb(255, 255,255)')
    True
    >>> valid_color('rgb(10%, 20%, 0%)')
    True
    >>> valid_color('hsl(200,100%,50%)')
    True
    >>> valid_color('hsl(0, 0%, 0%)')
    True

    >>> valid_color('#2345')
    False
    >>> valid_color('ffffff')
    False
    >>> valid_color('rgb(257, 50, 10)')
    False
    >>> valid_color('hsl(20, 10, 0.5)')
    False
    >>> valid_color('hsl(34%, 20%, 50%)')
    False
  
    """

    rgb_pattern = r'^rgb\((\d{1,2}|[01]?\d{2}|2[0-4]\d|25[0-5]|(0?|[1-9])\d%?),\s?(\d{1,2}|[01]?\d{2}|2[0-4]\d|25[0-5]|(0?|[1-9])\d%?),\s?(\d{1,2}|[01]?\d{2}|2[0-4]\d|25[0-5]|(0?|[1-9])\d%?)\)$'
    hex_pattern = r'(^#[A-Fa-f0-9]{6}\b)|(^#[A-Fa-f0-9]{3}\b)'
    hsl_pattern = r'^hsl\((36[0]|3[0-5]\d|[12]?\d{1,2}|0),\s?(100%|[1-9]?\d%|0%),\s?(100%|[1-9]?\d%|0%)\)$'

    if re.match(rgb_pattern, color) or re.match(hex_pattern, color) or re.match(hsl_pattern, color):
      return True
    else:
      return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()