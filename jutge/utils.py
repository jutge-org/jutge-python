def extract_kwargs(**kwd_ids_and_defaults):
    """For Python 2 compatibility (**kwargs must be used instead of
    keyword-only args). Decorates functions in such a way that only
    some specified kwargs are allowed, and sets their defaults."""

    def decorator(func):

        def decorated(*args, **kwargs):
            for kwarg in kwargs:
                if kwarg not in kwd_ids_and_defaults:
                    raise NameError("Unknown kwarg '{}'".format(kwarg))
            for kwarg in kwd_ids_and_defaults:
                if kwarg not in kwargs:
                    kwargs[kwarg] = kwd_ids_and_defaults[kwarg]
            return func(*args, **kwargs)

        return decorated

    return decorator
