%if 0%{?fedora} && 0%{?fedora} >= 20
%global develdocdir %{_docdir}/%{name}-devel
%else
%global develdocdir %{_docdir}/%{name}-devel-%{version}
%endif

Name:           libevent
Version:        2.0.21
Release:        8%{?dist}
Summary:        Abstract asynchronous event notification library

License:        BSD
URL:            http://sourceforge.net/projects/levent/        
Source0:        http://downloads.sourceforge.net/levent/%{name}-%{version}-stable.tar.gz

BuildRequires: doxygen openssl-devel

Patch00: libevent-2.0.10-stable-configure.patch
# Disable network tests
Patch01: libevent-nonettests.patch

%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. libevent is meant to replace the asynchronous event
loop found in event driven network servers. An application just needs
to call event_dispatch() and can then add or remove events dynamically
without having to change the event loop.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and libraries for developing
with %{name}.

%package doc
Summary: Development documentation for %{name}
BuildArch: noarch

%description doc
This package contains the development documentation for %{name}.

%prep
%setup -q -n libevent-%{version}-stable

# 477685 -  libevent-devel multilib conflict
%patch00 -p1
%patch01 -p1 -b .nonettests

%build
%configure \
    --disable-dependency-tracking --disable-static
make %{?_smp_mflags} all

# Create the docs
make doxygen

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

mkdir -p $RPM_BUILD_ROOT/%{develdocdir}/html
(cd doxygen/html; \
	install -p -m 644 *.* $RPM_BUILD_ROOT/%{develdocdir}/html)

mkdir -p $RPM_BUILD_ROOT/%{develdocdir}/sample
(cd sample; \
	install -p -m 644 *.c Makefile* $RPM_BUILD_ROOT/%{develdocdir}/sample)

%clean
rm -rf $RPM_BUILD_ROOT

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc ChangeLog LICENSE README
%{_libdir}/libevent-*.so.*
%{_libdir}/libevent_core-*.so.*
%{_libdir}/libevent_extra-*.so.*
%{_libdir}/libevent_openssl-*.so.*
%{_libdir}/libevent_pthreads-*.so.*

%files devel
%{_includedir}/event.h
%{_includedir}/evdns.h
%{_includedir}/evhttp.h
%{_includedir}/evrpc.h
%{_includedir}/evutil.h
%dir %{_includedir}/event2
%{_includedir}/event2/*.h
%{_libdir}/libevent.so
%{_libdir}/libevent_core.so
%{_libdir}/libevent_extra.so
%{_libdir}/libevent_openssl.so
%{_libdir}/libevent_pthreads.so
%{_libdir}/pkgconfig/libevent.pc
%{_libdir}/pkgconfig/libevent_openssl.pc
%{_libdir}/pkgconfig/libevent_pthreads.pc
%{_bindir}/event_rpcgen.*

%files doc
%{develdocdir}/

%changelog
* Sat Oct 24 2015 builder - 2.0.21-8
- Rebuild for new 4.0 release.

