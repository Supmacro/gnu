

# RPM
    > Redhat package manager.  
    > The Red Hat Linux distribution is specially used to manage the programs of various Linux packages. 
    > Because it follows the GPL rules and is powerful and convenient, it is very popular. 
    > It is gradually adopted by other distributions. The emergence of RPM package management makes Linux 
    > easy to install and upgrade, which indirectly improves the applicability of Linux. 

## Usage
```shell
    yum install rpm-build rpmdevtools
    rpmdev-setuptree
    
    |__ BUILD
    |__ RPMS
    |__ SOURCES
    |__ SPECS
    |__ SRPMS

    rpmdev-newspec
    |
    |__ newpackage.spec

```
   
# Macro Analogues of Autoconf Variables

    Several macro definitions provided by the default rpm macro set have uses in packaging similar to the 
    autoconf variables that are used in building packages:

| name | value |
|:-- |:-- |
| %\_prefix | /usr |
| %\_exec\_prefix | %{\_prefix} |
| %\_bindir | %{\_exec\_prefix}/bin |
| %\_sbindir | %{\_exec\_prefix}/sbin |
| %\_datadir | %{\_prefix}/share |
| %\_sysconfdir | %{\_prefix}/etc |
| %\_libdir | %{\_exec\_prefix}/lib |
| %\_includedir | %{\_prefix}/include |


# Build RPM
```
rpmbuild -bb --sign *.spec
/* rpm --checksig *.rpm */
```

# Qusetion
- Found installed (but unpackaged) files 
`%define _unpackaged_files_terminate_build 0`

- Ignore rpath check
```
vim ~/.rpmmacros
#%__arch_install_post /usr/lib/rpm/check-rpaths /usr/lib/rpm/check-buildroot
```


