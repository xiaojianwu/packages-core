Name: wayland-protocols 
Version: 1.0 
Release: 2
Summary: Wayland protocols 

License: MIT 
URL: http://cgit.freedesktop.org/wayland/wayland-protocols
Source0: http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig gawk 
BuildRequires: autoconf automake libtool
BuildArch: noarch

%description
wayland-protocols contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%prep
%setup -q

%build
if [ ! -f "configure" ]; then ./autogen.sh; fi
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%files
%doc README COPYING
%{_datadir}/pkgconfig/wayland-protocols.pc
%{_datadir}/wayland-protocols/unstable/fullscreen-shell/fullscreen-shell-unstable-v1.xml
%{_datadir}/wayland-protocols/unstable/input-method/input-method-unstable-v1.xml
%{_datadir}/wayland-protocols/unstable/linux-dmabuf/linux-dmabuf-unstable-v1.xml
%{_datadir}/wayland-protocols/unstable/pointer-gestures/pointer-gestures-unstable-v1.xml
%{_datadir}/wayland-protocols/unstable/text-input/text-input-unstable-v1.xml
%{_datadir}/wayland-protocols/unstable/xdg-shell/xdg-shell-unstable-v5.xml

%changelog
* Thu Nov 26 2015 Cjacker <cjacker@foxmail.com> - 1.0-2
- Update to 1.0 release

* Wed Nov 18 2015 Cjacker <cjacker@foxmail.com> - 0.1.0-2.git
- Initial build


