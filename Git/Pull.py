#!/usr/bin/env python3

import git

class GitBuild:
    repo = git.Repo("{Your clone PATH}")
    repo.git.pull("{Name of repo}", "{Which Branch}")

# the {} just marking where you need to replace, switch with your value.
