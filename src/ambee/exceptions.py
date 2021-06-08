"""Exceptions for Ambee."""


class AmbeeError(Exception):
    """Generic Ambee exception."""


class AmbeeConnectionError(AmbeeError):
    """Ambee connection exception."""


class AmbeeConnectionTimeoutError(AmbeeConnectionError):
    """Ambee connection Timeout exception."""
