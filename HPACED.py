# Highest Peak Aligment for Capillary Electrophoresis Data
# (c) Dr. Adam Streck 2016
# adam.streck@gmail.com

import sys


class ArgumentException(Exception):
    def __init__(self, message):

        message += "\n\nusage: HPACED.py location template_file" \
                   "\n\tlocation: filesystem path to where the data are stores" \
                   "\n\ttemplate_file: the name of the file found in the location based on which the files are aligned"

        # Call the base class constructor with the parameters it needs
        super(Exception, self).__init__(message)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise ArgumentException("Too few arguments.")
    if len(sys.argv) > 3:
        raise ArgumentException("Too many arguments.")
