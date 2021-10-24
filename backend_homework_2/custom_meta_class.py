"""
File with custom meta class
"""
from copy import copy


class CustomMeta(type):
    """
    Meta class
    """
    def __call__(cls, *args, **kwargs):
        """
        custom names
        :param args:
        :param kwargs:
        :return:
        """
        cls.__init__(cls)
        new_attrs = copy(dir(cls))
        for i in range(len(new_attrs)):
            if new_attrs[i][0] != '_' and 'custom_' not in new_attrs[i]:
                setattr(cls, 'custom_' + new_attrs[i], getattr(cls, new_attrs[i]))
                delattr(cls, new_attrs[i])

        custom_class = super(CustomMeta, cls).__call__(cls, *args, **kwargs)
        delattr(custom_class, 'val')

        return custom_class

class CustomClass(metaclass=CustomMeta):
    """
    Custom class
    """
    x = 50

    def __init__(self, val=99):
        """
        Constructor for custom class
        :param val:
        """
        self.val = val

    def line(self):
        """
        funny fun
        :return:
        """
        return 100
