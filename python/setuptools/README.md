
## Description
```
----setuptools
  |
  |__ /usr/bin/easy_install
  |__ /usr/bin/easy_install-2.7
  |__ /usr/lib/python2.7/site-packages/...
  |__ /usr/share/doc/python-setuptools-0.9.8/...

```

## Usage
| command | desc |
| :-- | :-- |
| easy\_install pkg | Find the latest version from PyPI through the package name, automatically download, compile and install |
| easy\_install -f url | Find the link from the designated download page by the package name to install or upgrade the package |
| easy\_install xxx.egg | Install from a local .egg file |
| easy\_install --upgrade pkg | Search and upgrade packages from pypi |
| easy\_install -m pkg | remove package |


## egg and wheel
  The Egg format was introduced by setuptools in 2004, and the Wheel format was defined by PEP427 in 2012. 
Wheel appeared to replace Egg. Its essence is a zip package, which is now considered as the standard format 
of Python binary package.

| format | suffix | import |
| :-- | :-- | :-- |
| egg | .egg | yes |
| wheel | .wheel | no |


## Build package
| command | desc |
| :-- | :-- |
| python setup.py sdist | build src package |
| python setup.py bdist\_wininst | build binary package(.exe) |
| python setup.py bdist\_rpm | build binary package(.rpm) |
| python setup.py bdist\_egg | build binary package(.egg) |


## Reference
https://zhuanlan.zhihu.com/p/276461821?utm\_source=qq
