Summary:	Patchsets for CVS
Name:		cvsps
Version:	2.0rc1
Release:	1
Group:		Development/Version Control
License:	GPL
Source0:	http://www.cobite.com/cvsps/%{name}-%{version}.tar.gz
# Source0-md5:	016cdaee3d33811f1d9264b5d3739647
URL:		http://www.cobite.com/cvsps/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVSps is a program for generating 'patchset' information from a CVS
repository. A patchset in this case is defined as a set of changes
made to a collection of files, and all committed at the same time
(using a single 'cvs commit' command). This information is valuable to
seeing the big picture of the evolution of a cvs project. While cvs
tracks revision information, it is often difficult to see what changes
were committed 'atomically' to the repository.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install cvsps $RPM_BUILD_ROOT%{_bindir}
install cvsps.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
