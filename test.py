# pylint: disable=missing-function-docstring
# pylint: disable=unused-import

"""
This is a module-level docstring that describes the purpose of the neke module.
"""

import cProfile
import program

if __name__ == "__main__":
    cProfile.run('program.greet()')