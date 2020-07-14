#!/usr/bin/env python3

__author__ = "Barre Kevin (neudinger)"
__maintainer__ = "Barre kevin"
__version__ = "1.1.0"
__email__ = "kevin.barre@epitech.eu"
__status__ = "DEV"

import json
import logging
import traceback
from typing import Dict, Generator, AnyStr
from os import getenv, path, walk, getcwd

logLevel = {"ERROR": 40,
            "WARNING": 30,
            "INFO": 20,
            "DEBUG": 10
            }


logging.basicConfig(format='%(asctime)s: %(levelname)s - %(message)s',
                    level=logLevel.get(
                        getenv("loglevel"), "DEBUG"),
                    datefmt='%d/%m/%Y %I:%M:%S %p')


def isFile():
    pass


def envCheck(nodeName: str):
    logging.info(f"Check {nodeName}")
    nodeVal = getenv(f"{nodeName}")
    logging.debug(f"{nodeName} is {nodeVal if nodeVal else None}")
    return bool(nodeName)

def fileCheck(nodeName: str, module:dict):
    logging.info(f"Check {nodeName}")
    nodeVal = module.get(nodeName, None)
    logging.debug(f"{nodeName} is {nodeVal if nodeVal else None}")
    return bool(nodeName)

# --- Binary Tree Func Decision (Function Nodes) ---


def isHost(module: dict):
    return bool(fileCheck(nodeName=str(traceback.extract_stack()[0][3])
                         .replace("()", "")
                         .replace("is", ""), module=module))


def isPort(module: dict):
    return bool(fileCheck("Port", module=module))


def isUser(module: dict):
    return bool(fileCheck("User", module=module))


def isPassord(module: dict):
    return bool(fileCheck("Password",module=module))


def isDefaultHost(*args):
    return bool(envCheck("DefaultHost"))


def isDefaultPort(*args):
    return bool(envCheck("DefaultPort"))


def isDefaultUser(*args):
    return bool(envCheck("DefaultUser"))


def isDefaultPassord(*args):
    return bool(envCheck("DefaultPassword"))


# --- End  ---


def isConnected():
    pass

# only for debug
# pathTree = [True]


def out(*args) -> None:
    # btreePath = bool2int(list(reversed(pathTree)))
    # logging.debug(f"Got out on node nb:{btreePath} vectors : {btreePath:0b}")
    return None


    #      1
btree = (isHost,
         # 2 -- 3
         isDefaultHost, isPort,
         # 4 -- 5 | 6 -- 7
         out, isPort, isDefaultPort, isUser,
         # 8 -- 9 | 10 -- 11 | 12 -- 13 | 14 -- 15
         isDefaultPort, isUser, out, out, out, out, isDefaultUser, isPassord,
         # 16 -- 17 | 18 -- 19 | 20 -- 21 | 22 -- 23 | 24 -- 25 | 26 -- 27 | 28 -- 29 | 30 -- 31
         out, isPassord, out, out, out, out, out, out, out, out, out, out, out, out, isDefaultPassord, isConnected,
         # 32--33|  34--35|   36--37|   38--39|   40--41|   42--43|   44--45|   46--47|   48--49|   50--51|   52--53|   54--55|   56--57|   58--59|   60--61|    62 -- 63 |
         out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, isConnected, out,
         # 64--65|   66--67|   68--69|   70--71|   72--73|   74--75|   76--77|   78--79|   80--81|   82--83|   84--85|   86--87|   88--89|   90--91|   92--93|   94--95|   96--97|   98--99|   100--101|   102--103|   104--105|   106--107|   108--109|   110--111|   112--113|   114--115|   116--117|   118--119|   120--121|   122--123|   124--125|   126--127|
         out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out, out)


# tuple is good for learning
# but prefer dict for saving
# memory space and speed access

# btree = {1:isHost,
# 3:isPort}

# NUM
#         1
#        / \
#       /   \
#      /     \
#     2       3
#    / \     / \
#   4   5   6   7
#  /   / \     / \
# 8   10 11   14 15
#        /
#       22

# BITS
#         1
#        / \
#       /   \
#      /     \
#     0       1
#    / \     / \
#   0   1   0   1
#  /   / \     / \
# 0   0   1   0   1
#        /
#       0


def getFiles() -> Generator:
    pwd = getcwd()
    dirname = getenv("dirname", "Bundles")
    for files in walk(path.join(pwd, dirname)):
        for nameFile in files[2]:
            if '.json' in nameFile or '.csv' in nameFile:
                yield path.join(pwd, dirname, nameFile)
    pass


def deployObject(deployfiles: Generator = getFiles()) -> Generator:
    for filepath in deployfiles:
        with open(filepath, "r") as jsonfile:
            jsonstr = jsonfile.read()
            # logging.debug(f"Files in {filepath} = {jsonstr}")
            processName = filepath.split('/')[-1].split('.')[0]
            yield {processName: json.loads(jsonstr)}
    pass


def bool2int(x: list) -> int:
    y = 0
    for i, j in enumerate(x):
        if j:
            y += 1 << i
    return y


def main() -> int:
    try:
        for nb, obj in enumerate(deployObject(), 1):
            # file level
            for bundleName, values in obj.items():
                # Objects levels
                # Clean bundleName 'idProcess' in 'contextProcess'
                for nb, value in enumerate(values, 1):
                    logging.debug(
                        f"bundleName {bundleName} object n {nb} = {value.items()}")
                    # cleanContextData(key=value["key"]) use for test
                    pathTree = [True]
                    while (pathTree):
                        node = list(reversed(pathTree))
                        # tuple version
                        vector = btree[bool2int(node)-1](value, bundleName)
                        # dict version
                        # vector = btree.get(bool2int(node)-1, out)(value, bundleName)
                        if vector is None:
                            break
                        pathTree.append(vector)
    except Exception as identifier:
        logging.fatal(repr(identifier))
        return -1
    else:
        logging.info(f"{bundleName} Deployed")
        return 0


if __name__ == "__main__":
    exit(main())
