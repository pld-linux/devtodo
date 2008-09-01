Summary:	Todo list managment
Summary(pl.UTF-8):	Zarządzanie listą spraw do zrobienia
Name:		devtodo
Version:	0.1.20
Release:	1
License:	GPL
Group:		Development/Tools
#Source0Download: http://swapoff.org/DevTodo
Source0:	http://swapoff.org/files/devtodo/%{name}-%{version}.tar.gz
# Source0-md5:	4a6241437cb56f237f850bcd2233c3c4
Patch0:		devtodo-stdlib_fix.patch
URL:		http://swapoff.org/DevTodo
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Developer Todo is a program to display and manage a hierarchical,
prioritised list of outstanding work, or just reminders.

The program itself is assisted by a few shell scripts that override
default builtins. Specifically, cd, pushd and popd are overridden so
that when using one of these commands to enter a directory, the todo
will display any outstanding items in that directory.

%description -l pl.UTF-8
Developer Todo jest programem do wyświetlania i zarządzania
hierarchiczną, listą zaległych prac z wyznaczonymi priorytetami, lub
po prostu przypomnieniami.

Sam program jest wspomagany kilkoma skryptami powłoki, które zastępują
domyślne, wbudowane polecenia, takie jak cd, pushd i popd. Jest to
potrzebne aby podczas wchodzenia do katalogu, przy użyciu wymienionych
komend, wypisywana była lista zaległych rzeczy do zrobienia w danym
katalogu.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses" \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{tda,tdd,tde,tdl,tdr,todo}.1*
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tda.1
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tdd.1
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tde.1
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tdl.1
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tdr.1
echo ".so devtodo.1" > $RPM_BUILD_ROOT%{_mandir}/man1/todo.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QuickStart README doc/todorc.example doc/*sh
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
