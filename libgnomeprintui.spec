Summary:	GUI support for libgnomeprint
Summary(pl):	Obs³uga GUI dla libgnomeprint
Name:		libgnomeprintui
Version:	2.6.1
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	cc0d51e8b4b188d22ed1d16e43a8a6bd
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gnome-icon-theme >= 1.2.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libglade2-devel >= 1:2.3.6
BuildRequires:	libgnomecanvas-devel >= 2.6.1
BuildRequires:	libgnomeprint-devel >= 2.6.1
BuildRequires:	libtool
BuildRequires:	rpm-build >= 4.1-10
Requires:	gnome-icon-theme >= 1.2.0
Requires:	gtk+2 >= 2:2.4.0
Requires:	libgnomeprint >= 2.6.1
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
Requires:	gtk+2-devel >= 2:2.4.0
Requires:	libgnomecanvas-devel >= 2.6.1
Requires:	libgnomeprint-devel >= 2.6.1

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
%patch0 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
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
