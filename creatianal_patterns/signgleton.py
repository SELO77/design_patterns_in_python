class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger


# These are the alternatives to using a Singleton in Python:
#
# * Use a module.
# * Create one instance somewhere at the top-level of your application, perhaps in the config file.
# * Pass the instance to every object that needs it.
# * That’s a dependency injection and it’s a powerful and easily mastered mechanism.
