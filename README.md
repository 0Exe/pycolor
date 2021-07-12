pycolor2

# Installation:

For Windows:
```py
pip install pycolor2 --upgrade
```

For MacOS and Linux:
```py
pip3 install pycolor2 --upgrade
```

# Usage Examples:

```py
from pycolor2 import color


# Colorful Text

print(color("green", "Hello World")) # print "Hello World" in green
print(color("l-red", "This is light red!")) # print "This is light red!" in light red

# Background Colors

print(color("bg-cyan", "This has a cyan background!")) # prints text with a cyan background
print(color("bg-green", "This has a green background!")) # prints text with green background


```

A list of all available colors:
- gray
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white

##

you can prefix "l-" to any color to make it light.


you can also prefix "bg-" to any color to make it background.


for a light background, you can use "l-bg-" as a prefix.


`NOTE: there isn't a "l-" prefix for white.`

#
License: The MIT License (MIT)
#
By [github.com/0Exe](https://github.com/0Exe)
