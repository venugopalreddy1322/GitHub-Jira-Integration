# Github-JIRA intergration using Python(flask) Project

Project Description:
For the actions(ex:issues/pull req, etc) on GitHub repository by the QE team or Dev team on a particular repository, which is refered by the developer who is associated with that particular task, if he feels it is a genuine action, then he wants to create a Jira Ticket/issue directly from the gitHub.

<<<<<<< HEAD
In this project is achieved by the following steps:

=======
In this project we achieved by the following steps:
>>>>>>> cf769a4b882dbf88ab84dcb564b100b3e230f059
1. Webhooks activated on the particular action on the Repository by the developer.
2. A python script which talks to Jira API and creates Jira issue in Jira Software account.
3. By using Flask module made the above python application into API, so GitHub can directly invoke this API( If not API, and just a python application, to invoke/execute this application the invokee needs to log into the server.)
4. Deploy the application on AWS EC2 instance (Ubuntu).
5. Whenever specified action happens on a Git repository webhooks sends POST request to the URL( Application deployed on EC2 instance ) given in the webhooks settings, this POST request from webhooks triggers python-Flask API then this APT talks to Jira and creates issue in the corresponding Project.

 - Remember to open necessary ports for communication.
 - Install flask package

-- python-flaske Source Code: github_python_jira.py 

[
Other applications:
.list_jira_projects.py -- will lists the Project names in the provided Jira account.
.create_jira_issue.py -- will create the new issue in Jira using python program, connects to Jira API. 
(Note: while creating issue, "The issue type id : will change from project to project"
    to get issue_id Dashboard--->issue types)
]
 
