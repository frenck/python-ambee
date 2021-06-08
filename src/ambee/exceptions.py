"""Exceptions for Ambee."""


class AmbeeError(Exception):
    """Generic Ambee exception."""


class AmbeeConnectionError(AmbeeError):
    """Ambee connection exception."""


class AmbeeAuthenticationError(AmbeeConnectionError):
    """Ambee authentication exception."""


class AmbeeConnectionTimeoutError(AmbeeConnectionError):
    """Ambee connection Timeout exception."""
