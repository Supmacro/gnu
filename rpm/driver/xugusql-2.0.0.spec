Name:           xugusql  
Version:        2.0.0 
Release:        1%{?dist}
Summary:        Xugu database C/C++ programming language general interface 

License:        none 
URL:            www.xugucn.com  
Source0:        %{name}-%{version}.tar.gz 

BuildArch:      x86_64
#BuildRequires:  
Requires:       bash 

%description   
    xugusql is a general interface of C/C++ programming language, and it is 
usually used as the underlying interface of its PHP, C#, Go and other 
programming languages.

%prep
%setup -c


%build


%install
mkdir -p %{buildroot}%{_libdir}
install -m 0755 lib%{name}.so %{buildroot}%{_libdir}
install -m 0644 xugusql.h %{buildroot}%{_libdir}

%files
%{_libdir}/lib%{name}.so
%{_libdir}/xugusql.h


%changelog
* Fri Mar 5 2021 WP Zhou <supmacro@foxmail.com> - 2.0.0 
- xugusql installation package.
- Xugu database C/C++ programming language general interface
