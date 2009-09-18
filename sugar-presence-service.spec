# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name: sugar-presence-service
Version: 0.85.3
Release: %mkrel 1
Summary: The Sugar presence service
License: GPLv2+
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/glucose/sugar-presence-service/sugar-presence-service-0.85.3.tar.bz2

Requires: avahi  
Requires: gnutls >= 2.4
Requires: python  
Requires: sugar-base >= 0.85.6
Requires: telepathy-gabble >= 0.7.21
Requires: python-telepathy >= 0.15.7
Requires: telepathy-salut >= 0.3.8

BuildRequires: libpython-devel  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
The Sugar presence service.

%prep
%setup -q -n sugar-presence-service-0.85.3


%build
%define __libtoolize true
%configure
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install


%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/sugar-presence-service
%attr(755,root,root) %{_datadir}/sugar-presence-service/main.py
%{_datadir}/dbus*/services/*
%{_bindir}/*
%doc COPYING NEWS

