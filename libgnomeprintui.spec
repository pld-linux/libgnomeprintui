Summary:	GUI support for libgnomeprint
Summary(pl.UTF-8):	Obsługa GUI dla libgnomeprint
Name:		libgnomeprintui
Version:	2.18.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnomeprintui/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	bea9871059cabee9d108bab32d58d2af
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 2.7.2
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-icon-theme >= 2.17.91
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomecanvas-devel >= 2.14.0
BuildRequires:	libgnomeprint-devel >= 2.17.92
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gnome-icon-theme >= 2.17.91
Requires:	gtk+2 >= 2:2.10.9
Requires:	libgnomecanvas >= 2.14.0
Requires:	libgnomeprint >= 2.17.92
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libgnomeprintui package contains GTK+ widgets related to printing.

%description -l pl.UTF-8
Pakiet libgnomeprintui zawiera widgety GTK+ związane z drukowaniem.

%package devel
Summary:	Headers for libgnomeprintui
Summary(pl.UTF-8):	Pliki nagłówkowe libgnomeprintui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.9
Requires:	libgnomecanvas-devel >= 2.14.0
Requires:	libgnomeprint-devel >= 2.17.92

%description devel
The libgnomeprintui package contains GTK+ widgets related to printing.

You should install the libgnomeprintui-devel package if you would like
to compile applications that use the widgets in libgnomeprintui. You
do not need to install it if you just want to use precompiled
applications.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających libgnomeprintui.

%package static
Summary:	Static libgnomeprintui libraries
Summary(pl.UTF-8):	Biblioteki statyczne libgnomeprintui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnomeprintui libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek libgnomeprintui.

%package apidocs
Summary:	libgnomeprintui API documentation
Summary(pl.UTF-8):	Dokumentacja API libgnomeprintui
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgnomeprintui API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgnomeprintui.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pkgconfigdir=%{_pkgconfigdir} \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

%find_lang %{name}-2.2

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-2.2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/gnome-print-job-preview.xml

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgnomeprintui

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
