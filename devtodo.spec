Summary:	Todo list managment
Summary(pl):	Zarz±dzanie list± spraw do zrobienia
Name:		devtodo
Version:	0.1.13
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://devtodo.sourceforge.net/?0.1.13/%{name}-%{version}.tar.gz
Patch0:		%{name}-include.patch
URL:		http://devtodo.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Developer Todo is a program to display and manage a hierarchical,
prioritised list of outstanding work, or just reminders.

The program itself is assisted by a few shell scripts that override
default builtins. Specifically, cd, pushd and popd are overridden so
that when using one of these commands to enter a directory, the todo
will display any outstanding items in that directory.

%description -l pl
Developer Todo jest programem do wy¶wietlania i zarz±dzania
hierarchiczn±, list± zaleg³ych prac z wyznaczonymi priorytetami, lub
po prostu przypomnieniami.

Sam program jest wspomagany kilkoma skryptami pow³oki, które zastêpuj±
domy¶lne, wbudowane polecenia, takie jak cd, pushd i popd. Jest to
potrzebne aby podczas wchodzenia do katalogu, przy u¿yciu wymienionych
komend, wypisywana by³a lista zaleg³ych rzeczy do zrobienia w danym
katalogu.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{tda,tdd,tde,tdr,todo}.1.gz
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tda.1
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tdd.1
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tde.1
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tdr.1
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/todo.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QuickStart README TODO doc/todorc.example doc/*sh
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/*
