class BaseError(Exception):
    """Base package error."""


class InvalidModelInputError(BaseError):
    """Model input contains an error."""
