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
