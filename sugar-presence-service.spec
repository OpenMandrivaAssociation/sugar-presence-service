# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Name:		sugar-presence-service
Version:	0.90.2
Release:	3
Summary:	The Sugar presence service
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://sugarlabs.org/

Source0:	http://download.sugarlabs.org/sources/sucrose/glucose/sugar-presence-service/sugar-presence-service-%{version}.tar.bz2

Requires:	avahi  
Requires:	gnutls >= 2.4
Requires:	python2
Requires:	sugar-base >= 0.88.0
Requires:	telepathy-gabble >= 0.7.21
Requires:	python2-telepathy >= 0.15.7
Requires:	telepathy-salut >= 0.3.8

BuildRequires: python-devel  

%description
The Sugar presence service.

%prep
%setup -q


%build
%define __libtoolize true
%configure2_5x
%make

%install
%makeinstall_std
chmod 755 %{buildroot}%{_datadir}/sugar-presence-service/main.py

%files 
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/sugar-presence-service
%{_datadir}/dbus*/services/*
%{_bindir}/*
%doc COPYING NEWS

