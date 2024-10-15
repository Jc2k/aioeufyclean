class EufyCleanException(Exception):
    pass


class ConnectionFailed(EufyCleanException):
    pass


class AuthenticationFailed(EufyCleanException):
    pass
