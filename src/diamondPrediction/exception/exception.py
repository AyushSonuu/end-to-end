import sys


class customexception(Exception):

    def __init__(self, error_message: str, error_details: sys):
        self.error_message = error_message
        _, _, exec_tb = error_details.exc_info()

        self.lineno = exec_tb.tb_lineno
        self.filename = exec_tb.tb_frame.f_code.co_filename

    def __str__(self) -> str:
        return "Error Occured in Python Script Name [{0}] Line Number [{1}] Error Message [{2}]".format(self.filename, self.lineno, str(self.error_message))


if __name__ == '__main__':

    try:
        a = 1/0
    except Exception as e:
        print(e)
        raise customexception(e, sys)
