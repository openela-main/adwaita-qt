
Name:           adwaita-qt
Version:        1.4.1
Release:        3%{?dist}
License:        LGPLv2+ and GPLv2+
Summary:        Adwaita theme for Qt-based applications

Url:            https://github.com/FedoraQt/adwaita-qt
Source0:        https://github.com/FedoraQt/adwaita-qt/archive/%{version}/adwaita-qt-%{version}.tar.gz

BuildRequires:  cmake

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  libxcb-devel

Obsoletes:      adwaita-qt4 < 1.1.90
Obsoletes:      adwaita-qt-common < 1.1.90

Requires:       adwaita-qt5

%description
Theme to let Qt applications fit nicely into Fedora Workstation

# Use -qt5 naming in case we provide -qt6 version in the future
%package -n adwaita-qt5
Summary:        Adwaita Qt5 theme
Requires:       libadwaita-qt5%{?_isa} = %{version}-%{release}

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
%cmake

%cmake_build

%install
%cmake_install

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
* Fri Apr 22 2022 Jan Grulich <jgrulich@redhat.com> - 1.4.1-3
- Bump build to build against correct Qt version
  Resolves: bz#2061416

* Fri Apr 01 2022 Jan Grulich <jgrulich@redhat.com> - 1.4.1-2
- Rebuild (Qt 5.15.3)
  Resolves: bz#2061416

* Tue Nov 16 2021 Jan Grulich <jgrulich@redhat.com> - 1.4.1-1
- 1.4.1
  Resolves: bz#2023181

* Wed Aug 25 2021 Jan Grulich <jgrulich@redhat.com> - 1.4.0-1
- 1.4.0
  Resolves: bz#1968275

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.1-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.1-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Mar 22 2021 Jan Grulich <jgrulich@redhat.com> - 1.2.1-1
- 1.2.1

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Jan Grulich <jgrulich@redhat.com> - 1.2.0-1
- 1.2.0

* Wed Sep 30 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.90-1
- 1.1.90

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.3-2
- Views: do not set color to views which don't use our palette

* Fri May 15 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.3-1
- 1.1.3

* Mon May 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.2-1
- 1.1.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.1-2
- Set correct Light, Midlight, Dark and Mid colors

* Wed Nov 20 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Mon Oct 21 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-5
- Actually apply all the fixes

* Mon Sep 02 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-4
- Pull in upstream fixes

* Tue Aug 13 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-3
- Pull in upstream fixes

* Tue Jul 30 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-2
- Pull in upstream fixes

* Mon Jul 29 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Jan Grulich <jgrulich@redhat.com> - 1.0.91-1
- Update to 1.0.91

* Mon Jul 08 2019 Jan Grulich <jgrulich@redhat.com> - 1.0.90-2
- Fix Qt4 item view widgets

* Tue Jul 02 2019 Jan Grulich <jgrulich@redhat.com. - 1.0.90-1
- Update to 1.0.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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
