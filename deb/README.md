
# Deb 
    The deb format is a dedicated installation package format for Debian systems (including Debian and Ubuntu), 
    and with the APT software management system, it has become a very popular installation package currently 
    under Linux.

# Usage
```
    apt-get install -y dh-make devscripts dpkg

```

# Dpkg
    *dpkg* is the abbreviation of Debian package, a package management system specially developed for the "Debian" 
    operating system, used for software installation, update and removal
| command | syntax | description |
| :-- | :-- | :-- |
| dpkg | dpkg -i | install |
| dpkg | dpkg -L | view where the package is installed |
| dpkg | dpkg -r | remove package (keep configuration) |
| dpkg | dpkg -P | remove package (Do not keep configuration) | 
| dpkg | dpkg --unpack | Unpack the contents of the deb package |


## .bashrc
```
DEBEMAIL="supmacro@foxmail.com"
DEBFULLNAME="WP Zhou"
```

# Debian
* control
```
    Source: package
    Section: software category (admin | games | web | utils | devel | libs...)
    Priority: software priority (optional | required | important | standard)
    Maintainer: zwp <supmacro@foxmail.com>
    Build-Depends: ...
    Standards-Version: ...
    Homepage: https:www.xugucn.com

    Package: pachage
    Architecture: amd64 (i386, powerpc)
    Depends: ...
    Description: 
```

* copyright
```
    Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
    Upstream-Name: xgci
    Upstream-Contact: <URL>
    Source: <text/URL> Explain the source of upstream software

    Files: debian/*
    Copyright: 2021 user <user@addr>
    License: GPL-2+
```

* changelog
```
    package (version) distribution; urgency=medium

    * change details
    [empty line]
    -- maintainer <email> [2 space] Fri, 05 Feb 2021 14:36:47 +0900
```


# Reference
* https://www.debian.org/doc/manuals/maint-guide/dreq.zh-cn.html
