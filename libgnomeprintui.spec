Summary:	GUI support for libgnomeprint
Summary(pl):	Obsługa GUI dla libgnomeprint
Name:		libgnomeprintui
Version:	2.4.2
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	5a28283f32efaa6fa401c5e9385b9634
URL:		http://www.gnome.org/
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomecanvas-devel >= 2.4.0
BuildRequires:	libgnomeprint-devel >= 2.4.2
BuildRequires:	rpm-build >= 4.1-10
Requires:	libgnomeprint >= 2.4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libgnomeprintui package contains GTK+ widgets related to printing.

%description -l pl
Pakiet libgnomeprintui zawiera widgety GTK+ związane z drukowaniem.

%package devel
Summary:	Headers for libgnomeprintui
Summary(pl):	Pliki nagłówkowe libgnomeprintui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+2-devel >= 2.2.0
Requires:	libgnomecanvas-devel >= 2.1.5
Requires:	libgnomeprint-devel >= 2.4.2

%description devel
The libgnomeprintui package contains GTK+ widgets related to printing.

You should install the libgnomeprintui-devel package if you would like
to compile applications that use the widgets in libgnomeprintui. You
do not need to install it if you just want to use precompiled
applications.

%description devel -l pl
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających libgnomeprintui.

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

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
