Summary: A portable x86 assembler which uses Intel-like syntax.
Name:   nasm
Version: 2.11.08
Release: 2
License: LGPL
Source: http://www.nasm.us/pub/nasm/releasebuilds/2.11.05/nasm-%{version}.tar.xz
URL: http://www.nasm.us
BuildRequires: perl

%package rdoff
Summary: Tools for the RDOFF binary format, sometimes used with NASM.

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%prep
%setup

%build
%configure
echo 'all:'>doc/Makefile
echo 'install:'>>doc/Makefile
make everything CFLAGS="$RPM_OPT_FLAGS -I. -I`pwd` -pedantic -Wall"

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

cp nasm $RPM_BUILD_ROOT/usr/bin
cp ndisasm $RPM_BUILD_ROOT/usr/bin
cp rdoff/ldrdf $RPM_BUILD_ROOT/usr/bin
cp rdoff/rdf2bin $RPM_BUILD_ROOT/usr/bin
cp rdoff/rdf2com $RPM_BUILD_ROOT/usr/bin
cp rdoff/rdf2ihx $RPM_BUILD_ROOT/usr/bin
cp rdoff/rdfdump $RPM_BUILD_ROOT/usr/bin
cp rdoff/rdflib $RPM_BUILD_ROOT/usr/bin
cp rdoff/rdx $RPM_BUILD_ROOT/usr/bin


%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_bindir}/nasm
%{_bindir}/ndisasm

%files rdoff
%defattr(-,root,root)
%{_bindir}/ldrdf
%{_bindir}/rdf2bin
%{_bindir}/rdf2com
%{_bindir}/rdf2ihx
%{_bindir}/rdfdump
%{_bindir}/rdflib
%{_bindir}/rdx

%changelog
* Fri Oct 23 2015 cjacker - 2.11.08-2
- Rebuild for new 4.0 release

* Thu Jul 30 2015 Cjacker <cjacker@foxmail.com>
- update to 2.11.08
