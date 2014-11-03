windows console robot
=============

utils to do console application automation.
add your script in a key stroke script such as ks.py, and run it by "console_robot.py ks.py"

ks.py example:
<code>
w = find_console("robot_demo")
w.char("pushd c:\\ \n")
w.char("dir\n")
w.char("pushd d:\\ \n")
w.char("dir\n")
</code>
