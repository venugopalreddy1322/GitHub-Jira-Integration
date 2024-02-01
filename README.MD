Github-JIRA intergration Project

Project Description:
For the actions(ex:issues/pull req, etc) on GitHub repository by the QE team or Dev team on a particular repository, which is refered by the developer who is associated with that particular task, if he feels it is a genuine action, then he wants to create a Jira Ticket/issue directly from the gitHub.

In this project we achieved by the following steps:
1. Webhooks activated on the particular action on the Repository the the developer.
2. A python script which talks to Jira API and creates Jira issue in Jira Software account.
3. By using Flaske module made the above python application into API.
4. Whenever specified action happens on a Git repository webhooks sends POST request to the URL given in the webhooks settings, this POST request from webhooks triggers python-Flask API then this APT talks to Jira and creates issue in the corresponding Project.

We hosted the python-flask application on AWS ubuntu-instance.
 - Remember to open necessary ports for communication.

github_python_jira.py -- python-flaske Source Code.

[
Other applications:
.list_jira_projects.py -- will lists the Project names in the provided Jira account.
.create_jira_issue.py -- will create the new issue in Jira using python program, connects to Jira API. 
(Note: while creating issue, "The issue type id : will change from project to project"
    to get issue_id Dashboard--->issue types)
]
 
