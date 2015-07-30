%define     gitdate
 
Name:           wayland
Version:        1.8.1
Release:        1%{?gitdate:.git%{gitdate}}
Summary:        Wayland Compositor Infrastructure

Group:          Core/Runtime/Library 
License:        MIT
URL:            http://%{name}.freedesktop.org/
Source0:        http://wayland.freedesktop.org/releases/%{name}-%{?gitdate:}%{!?gitdate:%{version}}.tar.xz
BuildRequires:  autoconf automake libtool
BuildRequires:  pkgconfig(libffi)
BuildRequires:  expat-devel
BuildRequires:  libxslt

Provides:       %{name}-common = %{version}-%{release}
Obsoletes:      %{name}-common < 0.85.0

%description
Wayland is a protocol for a compositor to talk to its clients as well as a C
library implementation of that protocol. The compositor can be a standalone
display server running on Linux kernel modesetting and evdev input devices,
an X application, or a wayland client itself. The clients can be traditional
applications, X servers (rootless or fullscreen) or other display servers.

%package devel
Summary: Common headers for wayland
License: MIT
Group:   Core/Development/Library 
%description devel
Common headers for wayland

%package -n libwayland-client
Summary: Wayland client library
License: MIT
Group:   Core/Runtime/Library 
%description -n libwayland-client
Wayland client library

%package -n libwayland-cursor
Summary: Wayland cursor library
License: MIT
Group:   Core/Runtime/Library 
%description -n libwayland-cursor
Wayland cursor library

%package -n libwayland-server
Summary: Wayland server library
License: MIT
Group:   Core/Runtime/Library 
%description -n libwayland-server
Wayland server library

%package -n libwayland-client-devel
Summary: Headers and symlinks for developing wayland client applications
License: MIT
Group:   Core/Development/Library 
Requires: libwayland-client%{?_isa} = %{version}-%{release}
Requires: wayland-devel%{?_isa} = %{version}-%{release}
%description -n libwayland-client-devel
Headers and symlinks for developing wayland client applications.

%package -n libwayland-cursor-devel
Summary: Headers and symlinks for developing wayland cursor applications
License: MIT
Group:   Core/Development/Library 
Requires: libwayland-cursor%{?_isa} = %{version}-%{release}
Requires: wayland-devel%{?_isa} = %{version}-%{release}
%description -n libwayland-cursor-devel
Headers and symlinks for developing wayland cursor applications.

%package -n libwayland-server-devel
Summary: Headers and symlinks for developing wayland server applications
License: MIT
Group:   Core/Development/Library 
Requires: libwayland-server%{?_isa} = %{version}-%{release}
Requires: wayland-devel%{?_isa} = %{version}-%{release}
%description -n libwayland-server-devel
Headers and symlinks for developing wayland server applications.

%prep
%setup -q -n %{name}-%{?gitdate:}%{!?gitdate:%{version}}
%build
%configure --disable-static --disable-documentation
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libwayland-client -p /sbin/ldconfig
%postun -n libwayland-client -p /sbin/ldconfig

%post -n libwayland-server -p /sbin/ldconfig
%postun -n libwayland-server -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README TODO

%files devel
%defattr(-,root,root,-)
%{_bindir}/wayland-scanner
%{_includedir}/wayland-util.h
%{_includedir}/wayland-egl.h
%{_includedir}/wayland-egl-core.h
%{_includedir}/wayland-version.h
%{_datadir}/aclocal/wayland-scanner.m4
%{_libdir}/pkgconfig/wayland-scanner.pc
%{_datadir}/wayland/wayland-scanner.mk
%{_datadir}/wayland/wayland.xml
%{_datadir}/wayland/wayland.dtd

#%{_mandir}/man3/*.3*

%files -n libwayland-client
%defattr(-,root,root,-)
%{_libdir}/libwayland-client.so.0*

%files -n libwayland-cursor
%defattr(-,root,root,-)
%{_libdir}/libwayland-cursor.so.0*

%files -n libwayland-server
%defattr(-,root,root,-)
%{_libdir}/libwayland-server.so.0*

%files -n libwayland-client-devel
%defattr(-,root,root,-)
%{_includedir}/wayland-client*.h
%{_libdir}/libwayland-client.so
%{_libdir}/pkgconfig/wayland-client.pc

%files -n libwayland-cursor-devel
%defattr(-,root,root,-)
%{_includedir}/wayland-cursor*.h
%{_libdir}/libwayland-cursor.so
%{_libdir}/pkgconfig/wayland-cursor.pc

%files -n libwayland-server-devel
%defattr(-,root,root,-)
%{_includedir}/wayland-server*.h
%{_libdir}/libwayland-server.so
%{_libdir}/pkgconfig/wayland-server.pc

