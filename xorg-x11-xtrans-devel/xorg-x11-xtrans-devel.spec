
Summary: X.Org X11 developmental X transport library
Name: xorg-x11-xtrans-devel
Version: 1.3.5
Release: 2
License: MIT/X11
URL: http://www.x.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/xtrans-%{version}.tar.bz2


BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-filesystem

Requires: xorg-x11-filesystem
Requires(pre): xorg-x11-filesystem >= 0.99.2-3

BuildArch: noarch
%description
X.Org X11 developmental X transport library

%prep
%setup -q -n xtrans-%{version}

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_includedir}/X11/Xtrans
%{_includedir}/X11/Xtrans/*
%{_datadir}/aclocal/xtrans.m4
%{_docdir}/xtrans/xtrans.xml
%{_datadir}/pkgconfig/xtrans.pc

%changelog
* Fri Oct 23 2015 cjacker - 1.3.5-2
- Rebuild for new 4.0 release

* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

