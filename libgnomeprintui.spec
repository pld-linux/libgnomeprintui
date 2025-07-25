Summary:	GUI support for libgnomeprint
Summary(pl.UTF-8):	Obsługa GUI dla libgnomeprint
Name:		libgnomeprintui
Version:	2.18.6
Release:	5
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libgnomeprintui/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	cbfab252ec7e9dc25bb1fe1610c3270b
Patch0:		%{name}-buildtime.patch
Patch1:		%{name}-gettext.patch
URL:		https://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.7.2
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomecanvas-devel >= 2.19.2
BuildRequires:	libgnomeprint-devel >= 2.18.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gnome-icon-theme >= 2.19.91
Requires:	gtk+2 >= 2:2.12.0
Requires:	libglade2 >= 1:2.6.2
Requires:	libgnomecanvas >= 2.19.2
Requires:	libgnomeprint >= 2.18.2
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
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	libglade2-devel >= 1:2.6.2
Requires:	libgnomecanvas-devel >= 2.19.2
Requires:	libgnomeprint-devel >= 2.18.2

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
BuildArch:	noarch

%description apidocs
libgnomeprintui API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgnomeprintui.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

for f in libgnomeprintui/gpaui/gpa-spinbutton.{c,h} ; do
	iconv -f iso-8859-1 -t utf-8 "$f" -o "${f}.tmp"
	%{__mv} "${f}.tmp" "$f"
done

%build
%{__gtkdocize}
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}-2.2

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-2.2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libgnomeprintui-2-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomeprintui-2-2.so.0
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/gnome-print-job-preview.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomeprintui-2-2.so
%{_pkgconfigdir}/libgnomeprintui-2.2.pc
%{_includedir}/libgnomeprintui-2.2

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomeprintui-2-2.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgnomeprintui
