Name:           pdo_xugusql  
Version:        7.2.34 
Release:        1%{?dist}
Summary:        PDO that supports xugu database service access 

License:        none 
URL:            www.xugucn.com  
Source0:        %{name}-%{version}.tar.gz 

BuildArch:      x86_64
#BuildRequires:  
Requires:       bash xugusql

%description    
    The PHP Data Objects (PDO) extension defines a lightweight, consistent interface 
for accessing databases in PHP. Each database driver that implements the PDO interface 
can expose database-specific features as regular extension functions.

%prep
%setup -c


%build


%install
mkdir -p %{buildroot}%{_prefix}/local/lib/pdo_xugusql
install -m 0755 pdo_xugusql.so %{buildroot}%{_prefix}/local/lib/pdo_xugusql

%files
%{_prefix}/local/lib/pdo_xugusql/pdo_xugusql.so
%dir %{_prefix}/local/lib/pdo_xugusql

%changelog
* Mon Feb 8 2021 WP Zhou <supmacro@foxmail.com> - 7.2.34 
- pdo_xugusql installation package.
- PDO that supports xugu database service access 
