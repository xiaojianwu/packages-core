Summary: X.Org X11 libxkbfile runtime library
Name: libxkbfile
Version: 1.0.9
Release: 2
License: MIT/X11
URL: http://www.x.org
Source0: http://xorg.freedesktop.org/archive/individual/lib/libxkbfile-%{version}.tar.bz2

BuildRequires: xorg-x11-proto-devel
BuildRequires: libX11-devel

Obsoletes: XFree86-libs, xorg-x11-libs

%description
X.Org X11 libxkbfile runtime library

%package devel
Summary: X.Org X11 libxkbfile development package
Requires: %{name} = %{version}-%{release}
Requires(pre): xorg-x11-filesystem >= 0.99.2-3

Obsoletes: XFree86-devel, xorg-x11-devel

%description devel
X.Org X11 libxkbfile development package

%prep
%setup -q -n libxkbfile-%{version}

%build
%configure \
	--disable-static

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libxkbfile.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*
%{_libdir}/libxkbfile.so
%{_libdir}/pkgconfig/xkbfile.pc

%changelog
* Fri Oct 23 2015 cjacker - 1.0.9-2
- Rebuild for new 4.0 release

* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

