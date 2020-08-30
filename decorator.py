def decorator(validator):
    def dec(func):
        def ret(*args, **kwargs):
            if validator(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                return 'error'
        return ret
    return dec

