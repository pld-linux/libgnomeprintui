%define gtk2_version 1.3.13
%define libgnomeprint_version 1.110.0
%define libgnomecanvas_version 1.110.0

Summary: GUI support for libgnomeprint
Name: libgnomeprintui
Version: 1.110.0
Release: 1
URL: ftp://ftp.gnome.org
Source0: %{name}-%{version}.tar.gz
License: LGPL
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root

Requires:  gtk2 >= %{gtk2_version}
Requires:  libgnomeprint >= %{libgnomeprint_version}
Requires:  libgnomecanvas >= %{libgnomecanvas_version}

BuildRequires:	gtk2-devel >= %{gtk2_version}
BuildRequires:  libgnomeprint-devel >= %{libgnomeprint_version}
BuildRequires:  libgnomecanvas-devel >= %{libgnomecanvas_version}

%description

The libgnomeprintui package contains GTK+ widgets related to printing.

%package devel
Summary: Libraries and headers for libgnomeprintui
Group: Development/Libraries
Requires:	%name = %{version}

Requires:  gtk2-devel >= %{gtk2_version}
Requires:  libgnomeprint-devel >= %{libgnomeprint_version}
Requires:  libgnomecanvas-devel >= %{libgnomecanvas_version}

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
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)

%doc AUTHORS COPYING ChangeLog NEWS README

%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)

%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.110.0

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jan  7 2002 Havoc Pennington <hp@redhat.com>
- hmm, didn't get all the libgnomeui dependency lines

* Mon Jan  7 2002 Havoc Pennington <hp@redhat.com>
- 1.109.0.90 snap, remove libgnomeui dep that's now gone

* Tue Nov 27 2001 Havoc Pennington <hp@redhat.com>
- new snap 1.106.0.90
- explicitly require certain versions of dependent libs

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- rebuild for glib 1.3.10, new cvs snap

* Tue Oct  9 2001 Havoc Pennington <hp@redhat.com>
- Initial build
