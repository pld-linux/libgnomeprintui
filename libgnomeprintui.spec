%define gtk2_version 1.3.13
%define libgnomeprint_version 1.110.0
%define libgnomecanvas_version 1.110.0

Summary:	GUI support for libgnomeprint
Name:		libgnomeprintui
Version:	1.110.0
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libgnomeprintui/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
Requires:	gtk2 >= %{gtk2_version}
Requires:	libgnomeprint >= %{libgnomeprint_version}
Requires:	libgnomecanvas >= %{libgnomecanvas_version}
BuildRequires:	gtk2-devel >= %{gtk2_version}
BuildRequires:	libgnomeprint-devel >= %{libgnomeprint_version}
BuildRequires:	libgnomecanvas-devel >= %{libgnomecanvas_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libgnomeprintui package contains GTK+ widgets related to printing.

%package devel
Summary:	Libraries and headers for libgnomeprintui
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%name = %{version}

Requires:	gtk2-devel >= %{gtk2_version}
Requires:	libgnomeprint-devel >= %{libgnomeprint_version}
Requires:	libgnomecanvas-devel >= %{libgnomecanvas_version}

%description devel
The libgnomeprintui package contains GTK+ widgets related to printing.

You should install the libgnomeprintui-devel package if you would like
to compile applications that use the widgets in libgnomeprintui. You
do not need to install it if you just want to use precompiled
applications.

%prep
%setup -q

%build

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%poost   -p /sbin/ldconfig
%poostun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*
