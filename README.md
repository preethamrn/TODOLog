# TODOLog
A few Sublime text files that help me create a TODO.txt file with a special color coding and a plugin that autocorrects numbering.

## ColorScheme
**T**odo | 1. (Red)<br/>
**D**one (Green)<br/>
**PROG**ress | **IP** (Orange)<br/>
**B**acklog (Blue)<br/>
**N**ope (Magenta)<br/>

## Fix Numbering
This plugin fixes the numbering of items in your log when it is saved. That way, when you rearrange tasks, you don't have to worry about fixing the numbering. It is automatically handled for you.<br/>
You can additionally have lines that start with `-` or subscripts (`1a`, `1b`) and these numbers will be accounted for as well.<br/>
Blocks of tasks are separated by double newlines and will restart the numbering.

### Known Issues
1. When a multi-digit number is replaced with a single digit number (or vice-versa), it messes up the spacing in later line which messes with the number tracking. Saving multiple times will fix this.
1. Subscripts aren't managed by this script. The letters in 2a, 2b, 2c, etc. need to be ordered manually.
