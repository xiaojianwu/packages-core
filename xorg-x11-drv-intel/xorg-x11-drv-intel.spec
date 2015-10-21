%define tarball xf86-video-intel
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir %{moduledir}/drivers

Summary:   Xorg intel video driver
Name:      xorg-x11-drv-intel
Version:   2.99.917
Release:   32.git
URL:       http://www.x.org
License:   MIT
Source0:   %{tarball}-ef859c8..tar.xz
Patch0:     intel-gcc-pr65873.patch

BuildRequires: autoconf automake libtool
BuildRequires: flex bison
BuildRequires: xorg-x11-server-devel
BuildRequires: libX11-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXtst-devel
BuildRequires: libXvMC-devel
BuildRequires: libXfont-devel
BuildRequires: mesa-libGL-devel >= 6.5-9
BuildRequires: libdrm-devel >= 2.4.25
BuildRequires: kernel-headers >= 2.6.32.3
BuildRequires: libudev-devel
BuildRequires: libxcb-devel >= 1.5 
BuildRequires: xcb-util-devel
BuildRequires: cairo-devel
BuildRequires: python

Requires: xorg-x11-server-Xorg >= 1.1.0-1
Requires: polkit

%description 
X.Org X11 Intel video driver.

%prep
%setup -q -n xf86-video-intel
%patch0 -p1

%build
./autogen.sh
%configure \
    --enable-kms-only \
    --enable-tools \
    --with-default-dri=3

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT 

find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libexecdir}/*
%{driverdir}/*.so
%{_libdir}/lib*.so*
%{_mandir}/man4/intel*
%{_datadir}/polkit-1/actions/org.x.xf86-video-intel.backlight-helper.policy

%changelog
* Wed Oct 21 2015 Cjacker <cjacker@foxmail.com> - 2.99.917-32.git
- update to ef859c8
* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5a9a3e7

* Sat Aug 08 2015 Cjacker <cjacker@foxmail.com>
- update to 611ec7d

* Thu Jul 30 2015 Cjacker <cjacker@foxmail.com>
- update to 4246c63

* Tue Jul 28 2015 Cjacker <cjacker@foxmail.com>
- update to 4f0a58c

* Fri Jul 24 2015 Cjacker <cjacker@foxmail.com>
- update to ad20fd4

* Thu Jul 23 2015 Cjacker <cjacker@foxmail.com>
- update to a29e765
* Wed Jul 22 2015 Cjacker <cjacker@foxmail.com>
- update to git 7301516
* Sun Jul 19 2015 Cjacker <cjacker@foxmail.com>
- 2c50639..2cd7cb9
