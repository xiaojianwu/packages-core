%define tarball xf86-video-sisusb
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

%undefine _hardened_build

Summary:    Xorg X11 sisusb video driver
Name:	    xorg-x11-drv-sisusb
Version:    0.9.6
Release:    21%{?dist}
URL:	    http://www.x.org
License:    MIT
Group:	    User Interface/X Hardware Support

Source0:    ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Patch0: 0001-Remove-mibstore.h.patch 

ExcludeArch: s390 s390x %{?rhel:ppc ppc64}

BuildRequires: xorg-x11-server-devel >= 1.10.99.902
BuildRequires: autoconf automake libtool

Requires:  xorg-x11-server-Xorg

%description 
X.Org X11 sisusb video driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch0 -p1

%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
# FIXME: This should be using makeinstall macro instead.  Please test
# makeinstall with this driver, and if it works, check it into CVS. If
# it fails, fix it in upstream sources and file a patch upstream.
make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/sisusb_drv.so
%{_mandir}/man4/*.4*

%changelog
