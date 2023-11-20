__author__ = "Naveed Hassan"

import os
import time
import datetime as dt
import sys

def knime() -> str:
    """
    Function to run the batch file containing the command to run the workflow in KNIME
    :Output:
        Returns the outcome of the execution (Successful or Unsuccessful)
    """
    # Execute Batch File and Check return code
    check = os.system("C:\\Users\\navee\\OneDrive\\Desktop\\Knime\\knime.bat")

    # Get current date and time
    t = dt.datetime.now()

    # Reformat Date and Time
    t = t.strftime('%d/%m/%Y %H:%M:%S') 

    # Return Code = 0 upon successful execution
    if check == 0:
        return(str("Successfully Executed at " + t))

    # Return Code = 2 if parameters are wrong or missing
    elif check == 2:
        return(str("Unsuccessful: Incorrect or Missing Parameters. Time: " + t))

    # Return Code = 3 when an error occurs during loading a workflow
    elif check == 3:
        return(str("Unsuccessful: An error occured when loading a workflow. Time: " + t)) 

    # Return Code = 4 if an error during execution occurred
    elif check == 4:
        return(str("Unsuccessful: An error occurred during execution. Time: " + t))


def schedule(interval: int, duration: int) -> None:
    """
    Function to schedule to run the knime function at specific intervals
    :Input:
        interval: int: of the amount of time between execution (given in minutes)
        duration: int: Amount of time to run this interval for (Hours)
    """
    interval = float(interval)
    duration = float(duration)
    # Convert interval (minutes) to seconds
    interval = interval * 60 - 40  
    # Convert duration (hours) to seconds
    duration = duration * 60 * 60  
    end_time = time.time() + duration
    while time.time() < end_time:
        # Run the knime workflow function
        knime()
        # Repeat after specific interval
        time.sleep(interval)


if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]](*args[2:])