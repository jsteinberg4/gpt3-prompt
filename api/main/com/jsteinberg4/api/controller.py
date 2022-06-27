import abc

class Controller(abc.ABC):
    """Abstract class for flask controllers.

    Subclasses should implement the register() method to 
    register routes with some arguments.
    """

    def __init__(self):
        pass

    @abc.abstractclassmethod
    def register(cls, *args, **kwargs):
        pass

