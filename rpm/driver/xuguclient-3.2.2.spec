Name:           xuguclient  
Version:        3.2.2 
Release:        1%{?dist}
Summary:        .Net core cross-platform xugu client tool. 

License:        none 
URL:            www.xugucn.com  
Source0:        %{name}-%{version}.tar.gz 

BuildArch:      x86_64
#BuildRequires:  
Requires:       bash xugusql 

%description    
Xuguclient supports the system.data.common interface, you can use the 
system.data.common interface to access the xugu database.

%prep
%setup -c


%build


%install
mkdir -p %{buildroot}%{_prefix}/local/share/%{name}

install -m 0755 XuguClient.%{version}.nupkg %{buildroot}%{_prefix}/local/share\
/%{name}/XuguClient.%{version}.nupkg
install -m 0644 README.md %{buildroot}%{_prefix}/local/share/%{name}/README.md


%files
%doc %{_prefix}/local/share/%{name}/README.md
%{_prefix}/local/share/%{name}/XuguClient.%{version}.nupkg

%dir %{_prefix}/local/share/%{name}

%changelog
* Mon Feb 8 2021 WP Zhou <supmacro@foxmail.com> - 3.2.2
- xuguclient installation package.
- .Net core cross-platform
