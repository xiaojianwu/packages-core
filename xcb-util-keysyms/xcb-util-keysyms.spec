Name:		xcb-util-keysyms
Version:	0.4.0
Release: 3 
Summary:	Standard X key constants and keycodes conversion on top of libxcb
License:	MIT
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	m4

%description
XCB util-keysyms module provides the following library:

  - keysyms: Standard X key constants and conversion to/from keycodes.


%package 	devel
Summary:	Development and header files for xcb-util-keysyms
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-keysyms.


%prep
%setup -q


%build
%configure --with-pic --disable-static --disable-silent-rules
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm %{buildroot}%{_libdir}/*.la

%check
make check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_libdir}/*.so.*


%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h


%changelog
* Fri Oct 23 2015 cjacker - 0.4.0-3
- Rebuild for new 4.0 release

