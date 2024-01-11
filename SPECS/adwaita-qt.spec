
Name:           adwaita-qt
Version:        1.2.1
Release:        4%{?dist}
License:        LGPLv2+ and GPLv2+
Summary:        Adwaita theme for Qt-based applications

Url:            https://github.com/FedoraQt/adwaita-qt
Source0:        https://github.com/FedoraQt/adwaita-qt/archive/%{version}/adwaita-qt-%{version}.tar.gz

BuildRequires:  cmake

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  libxcb-devel

Obsoletes:      adwaita-qt4 < 1.0-5

Provides:       adwaita-qt-common = %{version}-%{release}
Obsoletes:      adwaita-qt-common < 1.0-5

Requires:       adwaita-qt5

%description
Theme to let Qt applications fit nicely into Fedora Workstation

# Use -qt5 naming in case we provide -qt6 version in the future
%package -n adwaita-qt5
Summary:        Adwaita Qt5 theme
Requires:       libadwaita-qt5%{?_isa} = %{version}-%{release}
Provides:       adwaita-qt = %{version}-%{release}
Obsoletes:      adwaita-qt < 1.2.1

%description -n adwaita-qt5
Adwaita theme variant for applications utilizing Qt5.

%package -n libadwaita-qt5
Summary:        Adwaita Qt5 library

%description -n libadwaita-qt5
%{summary}.

%package -n libadwaita-qt5-devel
Summary:        Development files for libadwaita-qt5
Requires:       libadwaita-qt5%{?_isa} = %{version}-%{release}

%description -n libadwaita-qt5-devel
The libadwaita-qt5-devel package contains libraries and header files for
developing applications that use libadwaita-qt5.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%{cmake} .

%make_build

%install
make install/fast DESTDIR=%{buildroot}

%files -n adwaita-qt5
%doc LICENSE.LGPL2 README.md
%{_qt5_plugindir}/styles/adwaita.so

%files -n libadwaita-qt5
%{_libdir}/libadwaitaqt.so.*
%{_libdir}/libadwaitaqtpriv.so.*

%files -n libadwaita-qt5-devel
%dir %{_includedir}/AdwaitaQt
%{_includedir}/AdwaitaQt/*.h
%dir %{_libdir}/cmake/AdwaitaQt
%{_libdir}/cmake/AdwaitaQt/*.cmake
%{_libdir}/pkgconfig/adwaita-qt.pc
%{_libdir}/libadwaitaqt.so
%{_libdir}/libadwaitaqtpriv.so


%changelog
* Fri Apr 01 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.1-4
- Rebuild (Qt 5.15.3)
  Resolves: bz#2061414

* Wed Apr 28 2021 Jan Grulich <jgrulich@redhat.com> - 1.2.1-3
- Rebuild (binutils)
  Resolves: bz#1930074

* Fri Apr 16 2021 Jan Grulich <jgrulich@redhat.com> - 1.2.1-2
- Adwaita-qt5 replaces adwaita-qt
  Resolves: bz#1930074

* Thu Apr 08 2021 Jan Grulich <jgrulich@redhat.com> - 1.2.1-1
- 1.2.1
  Resolves: bz#1930074

* Mon May 14 2018 Jan Grulich <jgrulich@redhat.com> - 1.0-5
- Drop Qt4 variant

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 26 2017 Martin Bříza <mbriza@redhat.com> - 1.0-1
- Update to 1.0

* Mon Feb 27 2017 Martin Briza <mbriza@redhat.com> - 0.98-1
- Update to 0.98
- Fixes #1410597

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.97-2
- drop hardcoded Requires: qt4/qt5-qtbase

* Wed Dec 14 2016 Martin Briza <mbriza@redhat.com> - 0.97-1
- Update to 0.97

* Tue Dec 13 2016 Martin Briza <mbriza@redhat.com> - 0.95-1
- Update to 0.95

* Thu Jun 30 2016 Jan Grulich <jgrulich@redhat.com> - 0.4-3
- Properly fix missing menubar in QtCreator

* Wed Jun 22 2016 Jan Grulich <jgrulich@redhat.com> - 0.4-2
- Attempt to fix missing menubar issue in QtCreator

* Thu Apr 21 2016 Jan Grulich <jgrulich@redhat.com> - 0.4-1
- Update to version 0.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Martin Briza <mbriza@redhat.com> - 0.3-1
- Updated to the latest release
- Added a Qt5 build

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20141216git024b00bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.6.20141216git024b00bf
- Rebuilt for GCC 5 C++11 ABI change

* Fri Jan 16 2015 Martin Briza <mbriza@redhat.com> - 0-0.5
- Package review cleanup
- Split into a base and a subpackage
- Fedora import

* Tue Dec 16 2014 Martin Briza <mbriza@redhat.com> - 0-0.4.copr
- Update to latest commit

* Fri Dec 05 2014 Martin Briza <mbriza@redhat.com> - 0-0.3.copr
- Update to latest commit

* Mon Sep 15 2014 Martin Briza <mbriza@redhat.com> - 0-0.2.copr
- Update to latest commit

* Mon Sep 15 2014 Martin Briza <mbriza@redhat.com> - 0-0.1.copr
- Initial build
