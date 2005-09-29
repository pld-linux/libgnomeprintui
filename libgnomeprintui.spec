Summary:	GUI support for libgnomeprint
Summary(pl):	Obs³uga GUI dla libgnomeprint
Name:		libgnomeprintui
Version:	2.12.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnomeprintui/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	fa0b0410c3ba8b6899c5ed278f02cbe5
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 2.7.2
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-icon-theme >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomecanvas-devel >= 2.12.0
BuildRequires:	libgnomeprint-devel >= 2.12.1
BuildRequires:	libtool
BuildRequires:	pkgconfig 
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gnome-icon-theme >= 2.12.0
Requires:	gtk+2 >= 2:2.8.3
Requires:	libgnomeprint >= 2.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libgnomeprintui package contains GTK+ widgets related to printing.

%description -l pl
Pakiet libgnomeprintui zawiera widgety GTK+ zwi±zane z drukowaniem.

%package devel
Summary:	Headers for libgnomeprintui
Summary(pl):	Pliki nag³ówkowe libgnomeprintui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.8.3
Requires:	libgnomecanvas-devel >= 2.12.0
Requires:	libgnomeprint-devel >= 2.12.0

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
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnomeprintui libraries.

%description static -l pl
Statyczna wersja bibliotek libgnomeprintui.

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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no 

%find_lang %{name}-2.2

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-2.2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/gnome-print-job-preview.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
