# Traceroute-like tool
Developed as part of the computer networking course.

This tool is a manual implementation of **tracert** which is computer network diagnostic 
command for displaying possible routes (paths) of packets across an Internet Protocol (IP) network.

## Usage
1. `python traceroute.py <flag> <value> target`
2. `python traceroute.py target`

There is one supported flag `-m` or `--max-hops` for maximum hops, e.g. `-m 5`. Default value is 16.

## Examples
* traceroute.py google.com
```markdown
1 172.x.x.x
2 172.x.x.x
3 192.x.x.x
4 10.x.x.x
5 5.x.x.x
6 87.x.x.x
...
```
* traceroute.py -m 8 google.com
```markdown
1 172.x.x.x
2 172.x.x.x
3 192.x.x.x
4 10.x.x.x
5 5.x.x.x
6 87.x.x.x
7 87.x.x.x
8 139.x.x.x
```
## Requirements
* Python 3