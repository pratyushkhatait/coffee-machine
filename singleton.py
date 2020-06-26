def singleton(class_):
    """
    This is an implementation of singleton decorator.
    Is it used to create a singleton class when required
    :param class_:
    :return:
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance
