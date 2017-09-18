#!/usr/bin/python
# from https://stackoverflow.com/a/29308524
# and https://stackoverflow.com/a/46156177/4588453

WorldPublic = True
TrivialName = "Vertex2017"

import git
import os
toplevel = subprocess.check_output(["git","rev-parse","--show-toplevel"],os.path.dirname(__file__))
sub = os.path.relpath(os.path.dirname(__file__),toplevel)
r = git.Repo(toplevel)

if not TrivialName in [remote.name for remote in r.remotes()]:

    from subprocess import check_output
    if WorldPublic:
        out = check_output(["curl","--header","PRIVATE-TOKEN: ASDF","-X","POST","https://gitlab.cern.ch/api/v3/projects?name=foobartest3&visibility_level=20"])
    else:
        out = check_output(["curl","--header","PRIVATE-TOKEN: ASDF","-X","POST","https://gitlab.cern.ch/api/v3/projects?name=foobartest3&visibility_level=0"])
        # TODO share with LHCb

    import json
    response = json.load(out)
    try:
        response["message"]["name"]
    else:
        import re
        check_output(["git","remote","add",TrivialName+"remote",re.sub("7999","8443",re.sub('ssh://git','https://:',out["ssh_url_to_repo"]))])


# todo unprotect master
check_output(["git","branch","-D","TrivialName"])
check_output(["git","subtree","split","--prefix="+sub,"-b",TrivialName])
check_output(["git","filter-branch","-f","--index-filter","rm -rf proceedings",TrivialName])
check_output(["git","push",TrivialName+"remote",TrivialName+":"+TrivialName,"-f"]

# publication script for pseyfert/gitlab-slide-publisher.
# Copyright (C) 2017  Paul Seyfert <pseyfert@cern.ch>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
