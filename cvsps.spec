Summary:	Patchsets for CVS
Summary(pl.UTF-8):	Zestawy łatek dla CVS
Name:		cvsps
Version:	2.1
Release:	2
License:	GPL
Group:		Development/Version Control
Source0:	http://www.cobite.com/cvsps/%{name}-%{version}.tar.gz
# Source0-md5:	bde2110ed9f5d14de8f8cb04e9d596fe
# Fixes made by git people, see:
# http://ydirson.free.fr/en/software/scm/cvsps.html
Patch0:		%{name}-fixes.patch
URL:		http://www.cobite.com/cvsps/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVSps is a program for generating 'patchset' information from a CVS
repository. A patchset in this case is defined as a set of changes
made to a collection of files, and all committed at the same time
(using a single 'cvs commit' command). This information is valuable to
seeing the big picture of the evolution of a cvs project. While cvs
tracks revision information, it is often difficult to see what changes
were committed 'atomically' to the repository.

%description -l pl.UTF-8
CVSps jest programem do generowania informacji o 'zestawie łatek'
(ang. patchset) z repozytorium CVS. Patchset w tym przypadku jest
zdefiniowany jako zbiór zmian dokonanych na kolekcji plików wysłanych
w tym samym momencie (za pomocą jednego wywołania 'cvs commit'). Ta
informacja jest przydatna do śledzenia procesu rozwoju projektu w CVS.
Choć CVS śledzi informacje o rewizjach, obejrzenie zmian wysłanych
'atomowo' do repozytorium nie jest rzeczą łatwą.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

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
