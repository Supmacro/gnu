
# Options
Name:           demo 
Version:        0.0.1
Release:        1%{?dist}
Summary:        A xugu DB driver supporting ODBC standard interface.

License:        NONE 
URL:            http://www.xugucn.com
Source0:        %{name}-%{version}.tar.gz 

# If the package is not architecture dependent, for example, if written entirely 
# in an interpreted programming language, set this to BuildArch: noarch. 
# If not set, the package automatically inherits the Architecture of the machine 
# on which it is built, for example x86_64.
BuildArch: x86_64

#BuildRequires:  
Requires: bash     

%description
Open Database Connectivity (ODBC) is a standard software API specification
for using database management systems (DBMS).
ODBC is independent of programming language, database system and operating
system.
The ODBC API is a library of ODBC functions that let ODBC-enabled
applications connect to any database for which an ODBC driver is available,
execute SQL statements, and retrieve results.

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
%setup -q


%build


%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 lib%{name}.so %{buildroot}%{_bindir}/lib%{name}.so

#rm -rf $RPM_BUILD_ROOT
#%make_install


%files
%{_bindir}/lib%{name}.so
#%doc


%changelog
* Wed Jan 20 2021 WP Zhou <supmacro@foxmail.com> - 3.5.0
- Xugu ODBC installation package.
- https://rpm-packaging-guide.github.io/#more-on-macros
