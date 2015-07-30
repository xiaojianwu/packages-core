Name:           itstool
Version:        2.0.0 
Release:        1
Summary:        ITS-based XML translation tool

Group:          CoreDev/Development/Utility/Documentation
License:        GPLv3+
URL:            http://itstool.org/
Source0:        http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2

BuildArch:      noarch
Requires:       python-libxml2

%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING COPYING.GPL3 NEWS
%{_bindir}/itstool
%{_datadir}/itstool
%doc %{_mandir}/man1/itstool.1.gz

%changelog
* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

