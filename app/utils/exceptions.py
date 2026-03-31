
class ConversionError(Exception):
    """
    Exception raised for errors that occur during the file conversion process.

    Attributes:
        message (str): Description of the error that occurred during conversion.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ValidationError(Exception):
    """
    Exception raised for validation errors in user input or file formats.

    Attributes:
        message (str): Description of the validation error encountered.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
