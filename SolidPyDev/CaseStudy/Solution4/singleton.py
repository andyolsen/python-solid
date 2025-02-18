# Class decorator, which designates the target class as a singleton.
def singleton(cls):

    def innerFunc(*args, **kwargs):
        if innerFunc.instance is None:
            innerFunc.instance = cls(*args, **kwargs)
        return innerFunc.instance

    innerFunc.instance = None

    return innerFunc