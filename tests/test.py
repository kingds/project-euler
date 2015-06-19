# Tests all of the solutions in the Solved folder

import answers
import os
import sys
import importlib
import time
from timeout import Timeout
from supress_print import Supress

# Set up the solutions directory
solved_dir = "../solved/"
sys.path.append(solved_dir)
os.chdir(solved_dir)

# Set up the timeout time
timeout_seconds = 5

# Get the list of solutions to check from command line arguments
if len(sys.argv) > 1:
    solutions = sys.argv[1:]

# Use all solutions if no command line parameters exist
else:
    solutions = sorted([filename[:-3] for filename in os.listdir(solved_dir) if filename[-3:] == ".py"])

# Test each solution against the answer
for solution in solutions:
    print "%s: " % solution , 
    try:
        expected_answer = answers.get_answer(solution)
        start_time = time.time()
        # Add a timeout to the method execution
        with Timeout(seconds=timeout_seconds):
            # Supress output from the imported method
            with Supress():
                solution_answer = importlib.import_module(solution).main()
        execute_time = time.time() - start_time
        if expected_answer == solution_answer:
            pass_status = "PASS"
        else:
            pass_status = "FAIL"
        print "Expected %s, Got %s, in %s seconds, %s" % (expected_answer, solution_answer, execute_time, pass_status)
    except Timeout.Timeout:
        print "Execution timed out after %s second%s. FAIL" % (str(timeout_seconds), ["s", ""][timeout_seconds==1])
    except AttributeError:
        print "No main method. FAIL"
    except KeyError:
        print "No answer found. FAIL"
    except Exception, e:
        print "Error during execution: %s. FAIL" % (e)

