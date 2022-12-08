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

## Comparing with real traceroute result
```markdown
> traceroute -w 3 -q 1 -m 16 google.com

traceroute to google.com (173.194.222.100), 16 hops max, 60 byte packets
 1  name (172.x.x.x)  0.317 ms
 2  name (192.x.x.x)  2.575 ms
 3  name (10.x.x.x)  23.911 ms
 4  name (5.x.x.x)  6.060 ms
 5  name (87.x.x.x)  15.485 ms
 6  name (87.x.x.x)  17.423 ms
 7  name (139.x.x.x)  37.862 ms
 8  name (87.x.x.x)  16.629 ms

```