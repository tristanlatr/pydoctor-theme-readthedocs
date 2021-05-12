class Foo:
    
    """Docstring for class Foo.
    This text tests for the formatting of docstrings generated from output
    ``sphinx.ext.autodoc``. Which contain reST, but sphinx nests it in the
    ``<dl>``, and ``<dt>`` tags. Also, ``<tt>`` is used for class, method names
    and etc, but those will *always* have the ``.descname`` or
    ``.descclassname`` class.
    Normal ``<tt>`` (like the <tt> I just wrote here) needs to be shown with
    the same style as anything else with ````this type of markup````.
    It's common for programmers to give a code example inside of their
    docstring::
        from test_py_module import Foo
        myclass = Foo()
        myclass.dothismethod('with this argument')
        myclass.flush()
        print(myclass)
    Here is a link to `capitalize`.
    Here is a link to `__init__`.
    """

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1

    flox = 1.5   #: Doc comment for Foo.flox. One line only.

    baz = 2
    """Docstring for class attribute Foo.baz."""

    def __init__(self, qux, spam=False):
        """Start the Foo.
        :param qux: The first argument to initialize class.
        :type qux: string
        :param spam: Spam me yes or no...
        :type spam: bool
        """
        #: Doc comment for instance attribute qux.
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam."""

    def add(self, val1, val2):
        """Return the added values.
        :param val1: First number to add.
        :type val1: int
        :param val2: Second number to add.
        :type val2: int
        :rtype: int
        """

        return val1 + val2

    def capitalize(self, myvalue):
        """Return a string as uppercase.
        :param myvalue: String to change
        :type myvalue: string
        :rtype: string
        """

        return myvalue.upper()

    def another_function(self, a, b, **kwargs):
        """
        Here is another function.
        :param a: The number of green hats you own.
        :type a: int
        :param b: The number of non-green hats you own.
        :type b: int
        :param kwargs: Additional keyword arguments. Each keyword parameter
                       should specify the name of your favorite cuisine.
                       The values should be floats, specifying the mean price
                       of your favorite dish in that cooking style.
        :type kwargs: float
        :returns: A 2-tuple.  The first element is the mean price of all dishes
                  across cuisines.  The second element is the total number of
                  hats you own: :math:`a + b`.
        :rtype: tuple
        :raises ValueError: When ``a`` is not an integer.

        """
        return sum(kwargs.values()) / len(kwargs), a + b

"""
This is a module demonstrating reST code documentation features.

Most part of this documentation is using Python type hinting.
"""

def demo_fields_docstring_arguments(m, b):  # type: ignore
    """
    Fields are used to describe specific properties of a documented object.

    This function can be used in conjuction with L{demo_typing_arguments} to
    find an arbitrary function's zeros.

    :type  m: number
    :param m: The slope of the line.
    :type  b: number
    :param b: The y intercept of the line.
    :rtype:   number
    :return:  the x intercept of the line M{y=m*x+b}.
    """
    return -b/m

def demo_consolidated_fields(a:float, b):  # type: ignore
    """
    Fields can be condensed into one "consolidated" field. Looks better in plain text.

    :Parameters:
        - `a`: The size of the fox (in meters)
        - `b`: The weight of the fox (in stones)
    :rtype: str
    :return: The number of foxes
    """
    return -b/a

def demo_typing_arguments(name: str, size: bytes) -> bool:
    """
    Type documentation can be extracted from standard Python type hints.

    :param name: The human readable name for something.
    :param size: How big the name should be.
    :return: Always `True`.
    """
    return True


def demo_cross_reference() -> None:
    r"""
    The inline markup construct ```object``` is used to create links to the documentation for other Python objects.
    'text' is the text that should be displayed for the link, and 'object' is the name of the Python object that should be linked to.

    If you wish to use the name of the Python object as the text for the link, you can simply write ```object``` -> `object`.

    - `demo_typing_arguments`
    """



class _PrivateClass:
    """
    This is the docstring of a private class.
    """

    def method_inside_private(self) -> bool:
        """
        A public method inside a private class.

        :return: Something.
        """
        return True


    def _private_inside_private(self) -> bool:
        """
        A private method inside a private class.

        :return: Something.
        """
        return True


class DemoClass:
    """
    This is the docstring of this class.
    """

    def __init__(self, one: str, two: bytes) -> None:
        """
        Documentation for class initialization.

        :param one: Docs for first argument.
        :param two: Docs for second argument.
        """

    @property
    def read_only(self) -> int:
        """
        This is a read-only property.
        """
        return 1

    @property
    def read_and_write(self) -> int:
        """
        This is a read-write property.
        """
        return 1

    @read_and_write.setter
    def read_and_write(self, value: int) -> None:
        """
        This is a docstring for setter.
        """

    @property
    def read_and_write_delete(self) -> int:
        """
        This is a read-write-delete property.
        """
        return 1

    @read_and_write_delete.setter
    def read_and_write_delete(self, value: int) -> None:
        """
        This is a docstring for setter.
        """

    @read_and_write_delete.deleter
    def read_and_write_delete(self) -> None:
        """
        This is a docstring for deleter.
        """

