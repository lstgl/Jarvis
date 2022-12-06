from colorama import Fore

import speedtest as st
from plugin import plugin, require
import subprocess
import platform
import os


@require(network=True)
@plugin('speedtest')
def speedtest(jarvis, s):
    """Runs a speedtest on your internet connection"""
    working_dir = os.getcwd()
    print(working_dir)
    my_os = platform.platform()
    if "Linux" in my_os:
        process = subprocess.run(
            ["./env/lib/python3.10/site-packages/speedtest/linux/speedtest"])
        return ("")
    if "Windows" in my_os:
        cmd = working_dir + "/env/lib/python3.10/site-packages/speedtest/win/speedtest.exe"
        process = subprocess.call([cmd])
        return("")
    if "mac_OS" in my_os:
        process = subprocess.run(
            ["./env/lib/python3.10/site-packages/speedtest/macos/speedtest"])
        return ("")
