Summary: libevdev is a wrapper library for evdev devices. 
Name: libevdev
Version: 1.4.2
Release: 1
License: GPL
Group:  Core/Runtime/Library 
Source0: http://www.freedesktop.org/software/libevdev/%{name}-%{version}.tar.xz

%description
libevdev is a wrapper library for evdev devices. it moves the common tasks when dealing with evdev devices into a library and provides a library interface to the callers, thus avoiding erroneous ioctls, etc.

The eventual goal is that libevdev wraps all ioctls available to evdev devices, thus making direct access unnecessary.

%package devel
Summary: Libraries and headers for %{name} 
Group:   Core/Development/Library
Requires: %name = %{version}

%description devel
Libraries and headers for %{name}

%prep
%setup -q
%build
%configure \
    --disable-static
make %{?_smp_flags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rpmclean

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/touchpad-edge-detector
%{_bindir}/libevdev-tweak-device
%{_bindir}/mouse-dpi-tool
%{_libdir}/*.so.*
%{_mandir}/man3/libevdev.3.gz

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

