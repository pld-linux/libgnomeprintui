Summary:	GUI support for libgnomeprint
Summary(pl):	Obs³uga GUI dla libgnomeprint
Name:		libgnomeprintui
Version:	1.116.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org:/pub/GNOME/sources/libgnomeprintui/1.116/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	gtk+2-devel >= 2.0.2
BuildRequires:	libgnomeprint-devel >= %{version}
BuildRequires:	libgnomecanvas-devel >= 2.0.1
BuildRequires:	libglade2-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2

%description
The libgnomeprintui package contains GTK+ widgets related to printing.

%description -l pl
Pakiet libgnomeprintui zawiera widgety GTK+ zwi±zane z drukowaniem.

%package devel
Summary:	Headers for libgnomeprintui
Summary(pl):	Pliki nag³ówkowe libgnomeprintui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+2-devel >= 2.0.2
Requires:	libgnomeprint-devel >= %{version}
Requires:	libgnomecanvas-devel >= 1.110

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
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pkgconfigdir=%{_pkgconfigdir} \
	DESTDIR=$RPM_BUILD_ROOT


%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
