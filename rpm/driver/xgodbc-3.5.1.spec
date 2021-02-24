Name:           xgodbc 
Version:        3.5.1
Release:        1%{?dist}
Summary:        Support ODBC access interface of xugu database 

License:        none 
URL:            http://www.unixodbc.org/ 
Source0:        %{name}-%{version}.tar.gz 

# If the package is not architecture dependent, for example, if written entirely 
# in an interpreted programming language, set this to BuildArch: noarch. 
# If not set, the package automatically inherits the Architecture of the machine 
# on which it is built, for example x86_64.
BuildArch: x86_64

#BuildRequires:  
Requires: bash unixODBC 

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
#   %setup -n %{dir} /* Unzip the package to %{dir} */
#   %setup -c        /* Generate %{name}-%{version} directory before decompression */
#
%setup -c

%build


%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}

install -m 0755 lib%{name}.so %{buildroot}%{_libdir} 
install -m 0644 odbc.temp %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 odbcinst.temp %{buildroot}%{_sysconfdir}/%{name} 
install -m 0644 README.md %{buildroot}%{_sysconfdir}/%{name}

#rm -rf $RPM_BUILD_ROOT
#%make_install

%files
%{_libdir}/lib%{name}.so
%config %{_sysconfdir}/%{name}/odbcinst.temp
%config %{_sysconfdir}/%{name}/odbc.temp
%doc %{_sysconfdir}/%{name}/README.md

%dir %{_sysconfdir}/%{name}


%changelog
* Mon Feb 8 2021 WP Zhou <supmacro@foxmail.com> - 3.5.1
- Xugu ODBC installation package.
- xgodbc is a set of ODBC interfaces for accessing xugu database services 
