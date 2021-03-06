"""
    Tests for botogram/utils.py

    Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
    Released under the MIT license
"""

import botogram.utils
import botogram.decorators


STRANGE_DOCSTRING = """ a


  b

"""


def test_strip_urls():
    # Standard HTTP url
    assert botogram.utils.strip_urls("http://www.example.com") == ""

    # Standard HTTPS url
    assert botogram.utils.strip_urls("https://www.example.com") == ""

    # HTTP url with dashes in the domain (issue #32)
    assert botogram.utils.strip_urls("http://www.ubuntu-it.org") == ""

    # HTTP url with a path
    assert botogram.utils.strip_urls("http://example.com/~john/d/a.txt") == ""

    # Standard email address
    assert botogram.utils.strip_urls("john.doe@example.com") == ""

    # Email address with a comment (+something)
    assert botogram.utils.strip_urls("john.doe+botogram@example.com") == ""

    # Email address with subdomains
    assert botogram.utils.strip_urls("john.doe@something.example.com") == ""

    # Email address with dashes in the domain name (issue #32)
    assert botogram.utils.strip_urls("pietroalbini@ubuntu-it.org") == ""


def test_format_docstr():
    # This docstring needs lots of cleanup...
    res = botogram.utils.format_docstr(STRANGE_DOCSTRING)
    assert res == "a\n\nb"

    # This instead should be left as it is
    ok = "a\nb"
    assert botogram.utils.format_docstr(ok) == ok


def test_docstring_of(bot):
    # This function will be used in the testing process
    def func():
        """docstring"""

    # Before everything, test with the default docstring
    assert botogram.utils.docstring_of(func) == "docstring"

    # Next try with an empty docstring
    func.__doc__ = ""
    assert botogram.utils.docstring_of(func) == "No description available."

    # And else try to use a custom function
    # This will also test if botogram.utils.format_docstr is called
    @botogram.decorators.help_message_for(func)
    def help_func():
        return STRANGE_DOCSTRING

    assert botogram.utils.docstring_of(func) == "a\n\nb"


def test_usernames_in():
    assert botogram.utils.usernames_in("Hi, what's up?") == []
    assert botogram.utils.usernames_in("Hi @johndoe!") == ["johndoe"]

    multiple = botogram.utils.usernames_in("Hi @johndoe, I'm @pietroalbini")
    assert multiple == ["johndoe", "pietroalbini"]

    command = botogram.utils.usernames_in("/say@saybot I'm @johndoe")
    assert command == ["johndoe"]

    email = botogram.utils.usernames_in("My address is john.doe@example.com")
    assert email == []

    username_url = botogram.utils.usernames_in("http://pwd:john@example.com")
    assert username_url == []
