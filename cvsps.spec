Summary:	Patchsets for CVS
Summary(pl.UTF-8):	Zestawy łatek dla CVS
Name:		cvsps
Version:	3.10
Release:	0.1
License:	GPL v2+
Group:		Development/Version Control
Source0:	http://www.catb.org/~esr/cvsps/%{name}-%{version}.tar.gz
# Source0-md5:	eafd64ba9359105d950462552750cc51
URL:		http://www.catb.org/~esr/cvsps/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVSps is a program for collecting patchsets from a CVS repository. The
original use case was that its reports were useful for human
inspection by developers working on projects using CVS, but nowadays
the --fast-export option (which emits the history as a git-style
fast-import stream) is more interesting.

This tool was written and maintained until 2.2b1 by David Manfield,
who reported his "thanks to my employer Cobite and Robert Lippman,
who've given me time to develop this tool". The 3.x versions with
fast-export dumping are maintained by Eric S. Raymond.

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

%build
%{__make} cvsps cvsps.1 \
	CC="%{__cc} -Wall" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p cvsps $RPM_BUILD_ROOT%{_bindir}
cp -p cvsps.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/cvsps
%{_mandir}/man1/cvsps.1*
