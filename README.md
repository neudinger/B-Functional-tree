# Binary-Decision-Functional-Tree

Functional Binary Decision Tree.

-----

## Requirement

> Python3 minimun </br>
> OR</br>
> Docker python:3.8-alpine preferred

### Dependencies

This script CAN connect to web server.</br>
You ***CAN*** setup:
- _Host_ of web service: `(DefaultHost)`
- _Port_ of web service: `(DefaultPort)`
- _User_ of web service: `(DefaultUser)`
- _Password_ web service: `(DefaultPassword)`

Everything in env variable:

**As Follow:**
```bash
> export LocalHost="el.on.4.x.tesla"
> env | grep LocalHost
LocalHost=el.on.4.x.tesla
```

This script need some dirs and files.</br>
You _SHOULD_ setup:
- Dir `(Bundles)` OR `(name of $dirname)` in same dir as the python script
- With some bundle dir inside
```bash
> export dirname="rocketmars"
> env | grep dirname
dirname=rocketmars
```
**OR**
```bash
> export dirname="rocketmars"
> env | grep dirname
dirname=rocketmars
```


----

IN Developement