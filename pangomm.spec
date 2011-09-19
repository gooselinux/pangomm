%define apiver 1.4

Name:           pangomm
Version:        2.26.0
Release:        1%{?dist}
Summary:        C++ interface for Pango

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/pangomm/2.26/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  glibmm24-devel >= 2.14.1
BuildRequires:  cairomm-devel >= 1.2.2
BuildRequires:  pango-devel >= 1.23.0
BuildRequires:  doxygen graphviz

Obsoletes:      gtkmm24 < 2.13.5


%description
pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm24-devel
Requires:       cairomm-devel
Requires:       pango-devel
Requires:       pkgconfig gtk-doc


%description devel
This package contains the libraries and header files needed for
developing pangomm applications.


%prep
%setup -q


%build
%configure %{!?_with_static: --disable-static}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

# Fix documentation installation, put everything under gtk-doc and fix
# relative paths.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/pangomm-%{apiver}
mv ${RPM_BUILD_ROOT}%{_docdir}/pangomm-%{apiver}/* ${RPM_BUILD_ROOT}%{_datadir}/gtk-doc/html/pangomm-%{apiver}/
mv ${RPM_BUILD_ROOT}%{_datadir}/devhelp/books/pangomm-%{apiver}/*.devhelp2 ${RPM_BUILD_ROOT}%{_datadir}/gtk-doc/html/pangomm-%{apiver}
# Fix broken devhelp base tag
sed -i 's:base="[^\"]*":base="/usr/share/gtk-doc/html/pangomm-1.4/reference/html":' $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/pangomm-1.4/*.devhelp2
# Remove old doc directory
rm -r ${RPM_BUILD_ROOT}%{_docdir}/pangomm-%{apiver}


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*


%files devel
%defattr(-, root, root, -)
%{_includedir}/pangomm-%{apiver}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/pangomm-%{apiver}
%{_datadir}/gtk-doc/html/pangomm-%{apiver}


%changelog
* Fri Sep 25 2009 Denis Leroy <denis@poolshark.org> - 2.26.0-1
- Update to upstream 2.26.0

* Mon Sep 14 2009 Denis Leroy <denis@poolshark.org> - 2.25.1.3-1
- Update to upstream 2.25.1.3
- Package pangomm libdir directory with config include header
- Fix documentation location

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  1 2009 Denis Leroy <denis@poolshark.org> - 2.24.0-1
- Update to upstream 2.24.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Denis Leroy <denis@poolshark.org> - 2.14.1-1
- Update to 2.14.1
- Devhelp patch upstreamed

* Sun Oct 12 2008 Denis Leroy <denis@poolshark.org> - 2.14.0-2
- Added patch to fix devhelp main page

* Tue Sep 23 2008 Denis Leroy <denis@poolshark.org> - 2.14.0-1
- Update to stable 2.14.0

* Fri Aug 29 2008 Denis Leroy <denis@poolshark.org> - 2.13.7-3
- Obsoletes older gtkmm to avoid libpangomm conflict 

* Wed Aug 27 2008 Denis Leroy <denis@poolshark.org> - 2.13.7-2
- Spec review fixes

* Mon Aug 25 2008 Denis Leroy <denis@poolshark.org> - 2.13.7-1
- First version
