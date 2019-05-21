#!/usr/bin/env python3

import sys
import subprocess

    # By default this is the VisualStudio2017 Path for MSBuild Change if you using lower versions
    sys.path.append("C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin")
    """Publish the web application"""
    filename1 = "(Your CSPROJ WebApplication Project. {for instance {WebApplication.csproj}) "
    # By default this is the VisualStudio2017 Path for MSBuild Change if you using lower versions
    p1 = subprocess.Popen(['C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\MSBuild.exe', filename1], shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line1 in p1.stdout.readlines():
        if line1.find(b"Published successfully,") != -1:
            print("Contains substring" "Published successfully")
        else:
            print("Doesn't contain substring")
    ret1 = p1.wait()
