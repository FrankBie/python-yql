#!/usr/bin/env python3

import traceback

__all__ = [ 'new_issue', 'setup_issue' ]

IssuesUrl = 'http://github.com/{user}/{project}/issues'

class Issue(object):
    User = None
    Project = None

    def __init__(_):
        _.tb = traceback.format_exc().replace('\n', '\n  ').strip()

    def __str__(_):
        return """\
An unexpected exception has been caught:

  {}

Please log this exception and details about the YQL you are executing at:

  {}
""".format(_.tb, IssuesUrl.format(user=_.User, project=_.Project))

def set_user(user):
    Issue.User = user

def set_project(project):
    Issue.Project = project

def setup_issue(user, project):
    set_user(user)
    set_project(project)

def new_issue():
    return Issue()
