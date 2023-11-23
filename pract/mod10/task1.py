import re

pattern = r"^(?=.*[A-Z].*[A-Z])(?=.*\d)(?=(?:.*[^A-Za-z0-9]){2,})(?!.*(.)\1\1)[A-Za-z0-9^$%@#&*!?]{6,}$"

def is_valid_password(password):
  """Return False in case incorrect password.
    Return True if password is correct.

    >>> is_valid_password("rtG3FG!Tr^e")
    True
    >>> is_valid_password("aA1!*!1Aa")
    True
    >>> is_valid_password("oF^a1D@y5e6")
    True

    >>> is_valid_password("пароль")
    False
    >>> is_valid_password("password")
    False
    >>> is_valid_password("qwerty")
    False
    >>> is_valid_password("lOngPa$$$W0Rd")
    False
    """
  return bool(re.match(pattern, password))


if __name__ == "__main__":
    import doctest
    doctest.testmod()