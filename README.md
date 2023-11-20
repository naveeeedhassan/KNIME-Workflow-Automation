# KNIME-Workflow-Automation

## Objective and Approach
The objective of this project is to Automate workflows in KNIME without accessing the premium (paid) KNIME server. The approach taken to try and achieve this was by executing the workflow through the command line. This was done by running a batch file. Now, to automate this, the methods possible identified were by using scheduling. There was multiple possibilities to implement this: Windows Task Scheduler, Node-RED or building a low-code scheduler from scratch on Python. All 3 of the methods were implemented and tested out and are illustrated below.


## Process
### Designing Workflows
A simple workflow was designed on KNIME Analytics Platform to figure out how a workflow runs on KNIME and to test out the automation of workflows.


## Batch File and Commands
A simple command was put into the batch file as shown below.

*"C:\Program Files\KNIME\knime.exe" -nosplash -application org.knime.product.KNIME_BATCH_APPLICATION 
-workflowDir="C:/Users/<user>/knime-workspace/WF" -reset*

Arguments:

-"*C:\Program Files\KNIME\knime.exe*": Launches KNIME.

-*consoleLog*: Causes a new window to be opened containing the log messages and will keep the window open after the execution has finished.

*-reset*: Reset workflow prior to execution.

*-workflowDir="C:/Users/<user>/knime-workspace/workflow"*: 
Shows the directory of the workflow to be executed.

We can edit the command line to switch between different workflows when required.

Enter the command into a file and save as a .bat file.


When this file is executed, it will run the workflow and output a return code to show Successful/Unsuccessful execution in a prompt which will read as follows:

Return Code = 0 upon successful execution

Return Code = 2 if parameters are wrong or missing

Return Code = 3 when an error occurs during loading a workflow

Return Code = 4 if an error during execution occurred

## Scheduling for Automation
### Windows Task Scheduler Method

This method uses the built in Windows Task Scheduler to schedule the computer to run the batch file after a specific interval for a certain amount of time. This allows the program to run in the background and can even wake the computer to begin the task.

### Node-RED Method

Node-RED allows us to build flows to inject & repeat at intervals to replicate automation. Although, one downside is that Node-RED must be open at all times for the flow to be running and injecting.

### Designing a Scheduler using Python

A low-code simple scheduler was built from scratch using python to clone the process of automation. Again, the batch file was used in order to execute the workflow.


## Conclusion

To conclude, there exists multiple methods of achieving the goal of automate the KNIME workflows without the use of the KNIME server. The infrastructure of the process is based on the command line in the batch file which is used in every method. The automation part has multiple options in terms of scheduling including building a scheduler from scratch.

## References
*KNIME FAQ. Available at: https://www.knime.com/faq#q12*
*KNIME (2019) Execute workflow in batch mode Windows 10, KNIME Community Forum. Available at: https://forum.knime.com/t/execute-workflow-in-batch-mode-windows-10/13986*
