Summary: The GNU versions of find utilities (find and xargs)
Name: findutils
Version: 4.5.14
Release: 1
Epoch: 1
License: GPLv3+
Group:  Core/Runtime/Utility 
URL: http://www.gnu.org/software/findutils/
Source0: ftp://alpha.gnu.org/gnu/findutils/%{name}-%{version}.tar.gz

# do not build locate
Patch1: findutils-4.4.0-no-locate.patch

# learn find to recognize autofs file system by reading /proc/mounts
# as autofs mount points are not listed in /etc/mtab
Patch2: findutils-4.4.2-autofs.patch

# add a new option -xautofs to find to not descend into directories on autofs
# file systems
Patch3: findutils-4.4.2-xautofs.patch

Patch5: findutils-disable-doc.patch

Conflicts: filesystem < 3
Provides: /bin/find
Provides: bundled(gnulib)

BuildRequires: automake
BuildRequires: gettext-devel
%description
The findutils package contains programs which will help you locate
files on your system.  The find utility searches through a hierarchy
of directories looking for files which match a certain set of criteria
(such as a file name pattern).  The xargs utility builds and executes
command lines from standard input arguments (usually lists of file
names generated by the find command).

You should install findutils because it includes tools that are very
useful for finding things on your system.

%prep
%setup -q
rm -rf locate
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1

# needed because of findutils-4.4.0-no-locate.patch
autoreconf -iv

%build
%configure

# uncomment to turn off optimizations
#find -name Makefile | xargs sed -i 's/-O2/-O0/'

make %{?_smp_mflags}

%check
export TZ=posix
LANG=C make check

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_infodir}

%find_lang %{name}

rpmclean
%files -f %{name}.lang
%{_bindir}/find
%{_bindir}/oldfind
%{_bindir}/xargs
%{_mandir}/man1/find.1*
%{_mandir}/man1/oldfind.1*
%{_mandir}/man1/xargs.1*

%changelog
