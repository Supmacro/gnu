Name:           unixODBC 
Version:        2.3.7
Release:        1%{?dist}
Summary:        unixODBC is an Open Source ODBC sub-system and an ODBC SDK for Linux 

License:        LGPL 
URL:            http://www.unixodbc.org/ 
Source0:        %{name}-%{version}.tar.gz 

# If the package is not architecture dependent, for example, if written entirely 
# in an interpreted programming language, set this to BuildArch: noarch. 
# If not set, the package automatically inherits the Architecture of the machine 
# on which it is built, for example x86_64.
BuildArch: x86_64

#BuildRequires:  
Requires: bash

%description
  Open Database Connectivity (ODBC) is a standard software API specification for using 
database management systems (DBMS). ODBC is independent of programming language, 
database system and operating system.
  The ODBC API is a library of ODBC functions that let ODBC-enabled applications 
connect to any database for which an ODBC driver is available, execute SQL statements, 
and retrieve results.

# Pre-processing script, this section is the pre-processing section, usually used 
# to execute some commands to unpack the open source program package in 
# preparation for the next step of compilation and installation. 
# In addition to executing the macro commands defined by RPM (starting with %), 
# you can also execute the SHELL command, which can have many lines
%prep
# Unzip and put the source code package, usually from the package in 
# ~/rpmbuild/SOURCES to ~/rpmbuild/BUILD/%{name}-%{version},such as:
#   %setup -q %{name}-%{version}
# Other rules:
#   %setup           /* Do not add any options, only open the package */
#   %setup -q        /* In quiet mode with minimal output, 'tar -xof *.tar.gz' */
#   %setup -a number /* Unzip only the source code of the given number */ 
#   %setup -n %{dir} /* Unzip the package to %{dir} */
#   %setup -c        /* Generate %{name}-%{version} directory before decompression */
#
%setup -c

%build


%install

install -m 0755 COPYING %{buildroot}

mkdir -p %{buildroot}%{_prefix}/local/lib
install -m 0755 lib/libodbccr.la %{buildroot}%{_prefix}/local/lib
install -m 0755 lib/libodbccr.so.2.0.0 %{buildroot}%{_prefix}/local/lib
install -m 0755 lib/libodbcinst.la %{buildroot}%{_prefix}/local/lib
install -m 0755 lib/libodbcinst.so.2.0.0 %{buildroot}%{_prefix}/local/lib
install -m 0755 lib/libodbc.la %{buildroot}%{_prefix}/local/lib
install -m 0755 lib/libodbc.so.2.0.0 %{buildroot}%{_prefix}/local/lib

mkdir -p %{buildroot}%{_prefix}/local/lib/pkgconfig
install -m 0644 lib/pkgconfig/odbccr.pc %{buildroot}%{_prefix}/local/lib/pkgconfig
install -m 0644 lib/pkgconfig/odbcinst.pc %{buildroot}%{_prefix}/local/lib/pkgconfig
install -m 0644 lib/pkgconfig/odbc.pc %{buildroot}%{_prefix}/local/lib/pkgconfig

mkdir -p %{buildroot}%{_prefix}/local/include
install -m 0644 include/autotest.h %{buildroot}%{_prefix}/local/include
install -m 0644 include/odbcinstext.h %{buildroot}%{_prefix}/local/include
install -m 0644 include/odbcinst.h %{buildroot}%{_prefix}/local/include
install -m 0644 include/sqlext.h %{buildroot}%{_prefix}/local/include
install -m 0644 include/sql.h %{buildroot}%{_prefix}/local/include
install -m 0644 include/sqlspi.h %{buildroot}%{_prefix}/local/include
install -m 0644 include/sqltypes.h %{buildroot}%{_prefix}/local/include
install -m 0644 include/sqlucode.h %{buildroot}%{_prefix}/local/include
install -m 0644 include/unixodbc_conf.h %{buildroot}%{_prefix}/local/include
install -m 0644 include/uodbc_extras.h %{buildroot}%{_prefix}/local/include
install -m 0644 include/uodbc_stats.h %{buildroot}%{_prefix}/local/include

mkdir -p %{buildroot}%{_prefix}/local/etc/ODBCDataSources
mkdir -p %{buildroot}%{_prefix}/local/bin
install -m 0755 bin/dltest %{buildroot}%{_prefix}/local/bin
install -m 0755 bin/isql %{buildroot}%{_prefix}/local/bin
install -m 0755 bin/iusql %{buildroot}%{_prefix}/local/bin
install -m 0755 bin/odbc_config %{buildroot}%{_prefix}/local/bin
install -m 0755 bin/odbcinst %{buildroot}%{_prefix}/local/bin
install -m 0755 bin/slencheck %{buildroot}%{_prefix}/local/bin

mkdir -p %{buildroot}%{_prefix}/local/share/man/man1
install -m 0644 man/dltest.1  %{buildroot}%{_prefix}/local/share/man/man1 
install -m 0644 man/isql.1  %{buildroot}%{_prefix}/local/share/man/man1 
install -m 0644 man/iusql.1  %{buildroot}%{_prefix}/local/share/man/man1 
install -m 0644 man/odbc_config.1  %{buildroot}%{_prefix}/local/share/man/man1 
install -m 0644 man/odbcinst.1  %{buildroot}%{_prefix}/local/share/man/man1 

mkdir -p %{buildroot}%{_prefix}/local/share/man/man5
install -m 0644 man/odbc.ini.5 %{buildroot}%{_prefix}/local/share/man/man5
install -m 0644 man/odbcinst.ini.5 %{buildroot}%{_prefix}/local/share/man/man5

mkdir -p %{buildroot}%{_prefix}/local/share/man/man7
install -m 0644 man/unixODBC.7 %{buildroot}%{_prefix}/local/share/man/man7

%define  _unpackaged_files_terminate_build 0
#rm -rf $RPM_BUILD_ROOT
#%make_install

%post
cd %{_prefix}/local/lib
{ ln -s -f libodbcinst.so.2.0.0 libodbcinst.so.2 || \
{ rm -f libodbcinst.so.2 && ln -s libodbcinst.so.2.0.0 libodbcinst.so.2; }; }
{ ln -s -f libodbcinst.so.2.0.0 libodbcinst.so || \
{ rm -f libodbcinst.so && ln -s libodbcinst.so.2.0.0 libodbcinst.so; }; }
{ ln -s -f libodbc.so.2.0.0 libodbc.so.2 || \
{ rm -f libodbc.so.2 && ln -s libodbc.so.2.0.0 libodbc.so.2; }; }
{ ln -s -f libodbc.so.2.0.0 libodbc.so || \
{ rm -f libodbc.so && ln -s libodbc.so.2.0.0 libodbc.so; }; }
{ ln -s -f libodbccr.so.2.0.0 libodbccr.so.2 || \
{ rm -f libodbccr.so.2 && ln -s libodbccr.so.2.0.0 libodbccr.so.2; }; }
{ ln -s -f libodbccr.so.2.0.0 libodbccr.so || \
{ rm -f libodbccr.so && ln -s libodbccr.so.2.0.0 libodbccr.so; }; }

touch %{_prefix}/local/etc/odbcinst.ini
touch %{_prefix}/local/etc/odbc.ini

%postun
rm -f %{_prefix}/local/lib/libodbcinst.so.2
rm -f %{_prefix}/local/lib/libodbcinst.so
rm -f %{_prefix}/local/lib/libodbc.so.2
rm -f %{_prefix}/local/lib/libodbc.so
rm -f %{_prefix}/local/lib/libodbccr.so.2
rm -f %{_prefix}/local/lib/libodbccr.so
rm -f %{_prefix}/local/etc/odbcinst.ini
rm -f %{_prefix}/local/etc/odbc.ini


%files
%{_prefix}/local/lib/libodbccr.la
%{_prefix}/local/lib/libodbccr.so.2.0.0
%{_prefix}/local/lib/libodbcinst.la
%{_prefix}/local/lib/libodbcinst.so.2.0.0
%{_prefix}/local/lib/libodbc.la
%{_prefix}/local/lib/libodbc.so.2.0.0

%{_prefix}/local/include/autotest.h
%{_prefix}/local/include/odbcinstext.h
%{_prefix}/local/include/odbcinst.h
%{_prefix}/local/include/sqlext.h
%{_prefix}/local/include/sql.h
%{_prefix}/local/include/sqlspi.h
%{_prefix}/local/include/sqltypes.h
%{_prefix}/local/include/sqlucode.h
%{_prefix}/local/include/unixodbc_conf.h
%{_prefix}/local/include/uodbc_extras.h
%{_prefix}/local/include/uodbc_stats.h

%{_prefix}/local/bin/dltest
%{_prefix}/local/bin/isql
%{_prefix}/local/bin/iusql
%{_prefix}/local/bin/odbc_config
%{_prefix}/local/bin/odbcinst
%{_prefix}/local/bin/slencheck

%{_prefix}/local/share/man/man1/dltest.1
%{_prefix}/local/share/man/man1/isql.1
%{_prefix}/local/share/man/man1/iusql.1
%{_prefix}/local/share/man/man1/odbc_config.1
%{_prefix}/local/share/man/man1/odbcinst.1
%{_prefix}/local/share/man/man5/odbc.ini.5
%{_prefix}/local/share/man/man5/odbcinst.ini.5
%{_prefix}/local/share/man/man7/unixODBC.7

%license COPYING
%config %{_prefix}/local/lib/pkgconfig/odbccr.pc 
%config %{_prefix}/local/lib/pkgconfig/odbcinst.pc
%config %{_prefix}/local/lib/pkgconfig/odbc.pc

%dir %{_prefix}/local/etc/ODBCDataSources 

%changelog
* Mon Feb 8 2021 WP Zhou <supmacro@foxmail.com> - 3.5.1
- Xugu ODBC installation package.
- unixODBC is a set of ODBC interfaces for accessing xugu database services 
