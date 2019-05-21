#!/usr/bin/env python3

import sys
import subprocess

class Build:
    filename = "<Your .NET Solution Path>"
    p = subprocess.Popen(['<Your MSBuild.exe path (by default: C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\MSBuild.exe)>', filename], shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        if line.find(b"Build succeeded,") != -2:
            print("Contains substring", "Build succeeded")
        else:
            print("Doesn't contain substring")
    ret = p.wait()
