%define gtk2_version 1.3.13
%define libgnomeprint_version 1.110.0
%define libgnomecanvas_version 1.110.0

Summary:	GUI support for libgnomeprint
Summary(pl):	Obs³uga GUI dla libgnomeprint
Name:		libgnomeprintui
Version:	1.110.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libgnomeprintui/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
Requires:	gtk+2 >= %{gtk2_version}
Requires:	libgnomeprint >= %{libgnomeprint_version}
Requires:	libgnomecanvas >= %{libgnomecanvas_version}
BuildRequires:	gtk+2-devel >= %{gtk2_version}
BuildRequires:	libgnomeprint-devel >= %{libgnomeprint_version}
BuildRequires:	libgnomecanvas-devel >= %{libgnomecanvas_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The libgnomeprintui package contains GTK+ widgets related to printing.

%description -l pl
Pakiet libgnomeprintui zawiera widgety GTK+ zwi±zane z drukowaniem.

%package devel
Summary:	Headers for libgnomeprintui
Summary(pl):	Pliki nag³ówkowe libgnomeprintui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk2+-devel >= %{gtk2_version}
Requires:	libgnomeprint-devel >= %{libgnomeprint_version}
Requires:	libgnomecanvas-devel >= %{libgnomecanvas_version}

%description devel
The libgnomeprintui package contains GTK+ widgets related to printing.

You should install the libgnomeprintui-devel package if you would like
to compile applications that use the widgets in libgnomeprintui. You
do not need to install it if you just want to use precompiled
applications.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do kompilacji programów
u¿ywaj±cych libgnomeprintui.

%package static
Summary:	Static libgnomeprintui libraries
Summary(pl):	Biblioteki statyczne libgnomeprintui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libgnomeprintui libraries.

%description static -l pl
Statyczna wersja bibliotek libgnomeprintui.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
