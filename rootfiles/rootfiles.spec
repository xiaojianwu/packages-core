Summary: The basic required files for the root user's directory.
Name: rootfiles
Version: 8.1
Release: 8.1 
License: Public Domain
Group:  Core/Runtime/Data
 
Source0: dot-bashrc
Source1: dot-bash_profile
Source2: dot-bash_logout
Source3: dot-tcshrc
Source4: dot-cshrc
Source5: dot-vimrc
Source6: dot-Xresources
BuildRoot: %{_tmppath}/%{name}%{name}-root
BuildArchitectures: noarch

%description
The rootfiles package contains basic required files that are placed
in the root user's account.  These files are basically the same
as those in /etc/skel, which are placed in regular
users' home directories.

%prep

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/root

for file in %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6}; do 
  f=`basename $file`
  install -m 644 $file $RPM_BUILD_ROOT/root/${f/dot-/.}
done
mkdir -p $RPM_BUILD_ROOT/etc/skel
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT/etc/skel/.Xresources
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) /root/.[A-Za-z]*
%config(noreplace) /etc/skel/.Xresources
%changelog
