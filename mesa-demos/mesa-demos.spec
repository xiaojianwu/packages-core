%global tarball mesa-demos
%global xdriinfo xdriinfo-1.0.4
%global demodir %{_libdir}/mesa

Summary: Mesa demos
Name: mesa-demos
Version: 8.2.0
Release: 4
License: MIT
Group: System Environment/Libraries
URL: http://www.mesa3d.org
Source0: ftp://ftp.freedesktop.org/pub/mesa/demos/8.1.0/%{tarball}-%{version}.tar.bz2
Source1: http://www.x.org/pub/individual/app/%{xdriinfo}.tar.bz2

# Patch pointblast/spriteblast out of the Makefile for legal reasons
Patch0: mesa-demos-8.0.1-legal.patch
Patch1: mesa-demos-as-needed.patch

BuildRequires: pkgconfig autoconf automake libtool
BuildRequires: freeglut-devel
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: libglew-devel
Group: Development/Libraries

%description
This package provides some demo applications for testing Mesa.

%package -n glx-utils
Summary: GLX utilities
Group: Development/Libraries
Provides: glxinfo

%description -n glx-utils
The glx-utils package provides the glxinfo and glxgears utilities.

%prep
%setup -q -n %{tarball}-%{version} -b1
%patch0 -p1 -b .legal
%patch1 -p1 -b .asneeded

# These two files are distributable, but non-free (lack of permission to modify).
rm -rf src/demos/pointblast.c
rm -rf src/demos/spriteblast.c

%build
autoreconf -i
%configure --bindir=%{demodir} --with-system-data-files
make %{?_smp_mflags}

pushd ../%{xdriinfo}
%configure
make %{?_smp_mflags}
popd

%install
make install DESTDIR=%{buildroot}

pushd ../%{xdriinfo}
make %{?_smp_mflags} install DESTDIR=%{buildroot}
popd

install -m 0755 src/xdemos/glxgears %{buildroot}%{_bindir}
install -m 0755 src/xdemos/glxinfo %{buildroot}%{_bindir}
install -m 0755 src/xdemos/glxinfo %{buildroot}%{_bindir}/glxinfo%{?__isa_bits}

%files
%{demodir}
%{_datadir}/%{name}/

%files -n glx-utils
%{_bindir}/glxinfo*
%{_bindir}/glxgears
%{_bindir}/xdriinfo
%{_datadir}/man/man1/xdriinfo.1*

%changelog
