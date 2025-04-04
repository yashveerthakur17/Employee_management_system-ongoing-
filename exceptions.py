import sys
from logger import logging

#generic exception handling script , can be used in any project

def error_message_detail(error, error_detail: sys):
    #ONLY 3RD PART IS RELEVANT,
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        "Error occurred in python script name [{0}] line number [{1}] error message [{2}]"
        .format(file_name, exc_tb.tb_lineno, str(error))
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        # Store the detailed error message
        self.error_message = error_message_detail(error_message, error_details)
        # Log the error message to the logging file
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
