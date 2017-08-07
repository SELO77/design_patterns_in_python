def check_authenticated(user):
    print(check_authenticated.__name__)
    if user:
        return True
    else:
        return False


def check_authorized(user, action):
    print(check_authorized.__name__)
    if user and action:
        return True
    else:
        return False


class UnauthenticatedError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


def authenticated_only(method):
    def decorated(*args, **kwargs):
        if check_authenticated(kwargs['user']):
            return method(*args, **kwargs)
        else:
            raise UnauthenticatedError
    return decorated


def authorized_only(method):
    def decorated(*args, **kwargs):
        if check_authorized(kwargs['user'], kwargs['action']):
            return method(*args, **kwargs)
        else:
            raise UnauthorizedError
    return decorated


def smoke(user):
    print('{} is smoking'.format(user))


@authenticated_only
@authorized_only
def execute(action, *args, **kwargs):
    return action(*args, **kwargs)


if __name__ == '__main__':
    execute(user='selo', action=smoke)
