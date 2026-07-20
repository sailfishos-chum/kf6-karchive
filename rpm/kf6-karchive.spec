%global kf_version 6.24.0

Name:           kf6-karchive
Version: 6.24.0
Release:        0%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with archive functions
License:        LGPL-2.0-or-later AND BSD-2-Clause
URL:            https://invent.kde.org/frameworks/karchive
Source0:    %{name}-%{version}.tar.bz2

# Compile Tools
BuildRequires:  cmake
BuildRequires:  clang

BuildRequires:  kf6-rpm-macros

# KDE Frameworks
BuildRequires:  kf6-extra-cmake-modules

# Qt
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel

# Compression
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

BuildRequires:  pkgconfig(openssl)

%description
KDE Frameworks 6 Tier 1 addon with archive functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 karchive6_qt

%files -f karchive6_qt.lang
%doc AUTHORS README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Archive.so.*

%files devel
%{_kf6_includedir}/KArchive/
%{_kf6_libdir}/cmake/KF6Archive/
%{_kf6_libdir}/libKF6Archive.so
