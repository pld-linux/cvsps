%define		_extraver	rc1
Summary:	Patchsets for CVS
Summary(pl):	Zestawy ³atek dla CVS
Name:		cvsps
Version:	2.0
Release:	0.%{_extraver}.1
License:	GPL
Group:		Development/Version Control
Source0:	http://www.cobite.com/cvsps/%{name}-%{version}%{_extraver}.tar.gz
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

%description -l pl
CVSps jest programem do generowania informacji o 'zestawie ³atek'
(ang. patchset) z repozytorium CVS. Patchset w tym przypadku jest
zdefiniowany jako zbiór zmian dokonanych na kolekcji plików wys³anych
w tym samym momencie (za pomoc± jednego wywo³ania 'cvs commit'). Ta
informacja jest przydatna do ¶ledzenia procesu rozwoju projektu w CVS.
Choæ CVS ¶ledzi informacje o rewizjach, obejrzenie zmian wys³anych
'atomowo' do repozytorium nie jest rzecz± ³atw±.

%prep
%setup -q -n %{name}-%{version}%{_extraver}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I. -DVERSION=%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install cvsps $RPM_BUILD_ROOT%{_bindir}
install cvsps.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
