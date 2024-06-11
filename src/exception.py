import sys
import logging

## create custome exceptional handling

def error_message_detail(error,error_details:sys):
    """
    This function returns detailed information about an error.

    Parameters:
    error: Exception object
        The exception that was raised.
    error_details: sys
        The sys module, used to get details about the exception.
    
    Returns:
    str: A detailed error message.
    """
    # Get the traceback object
    _, _, exc_tb = error_details.exc_info()
    
    # Extract information about error message
    file_name =  exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    # Create the detailed error message

    error_message = f"Error occured in script : {file_name} at line number: {line_number} with error message : [{str(error)}]"

    return error_message

class CustomeException(Exception):
    def __init__(self,error_message, error_details:sys):
           """
        Custom exception class to capture and display detailed error information.
        """
           super().__init__(error_message)
           self.error_message = error_message_detail(error_message,error_details)
    
    def __str__(self):
         return self.error_message
 

""" if __name__ == "__main__":
     try:
          a = 1/0
     except Exception as e:
          logging.info("Divide by Zero exception")
          raise CustomeException(e,sys) """

     
       