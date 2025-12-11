Name:           plasma-workspace-sonic
Version:        6.5.3
Release:        1%{?dist}
Summary:        SonicDE Plasma Workspace

License:        LGPL-2.0-or-later
URL:            https://github.com/Sonic-DE/plasma-workspace-sonic
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
Requires:       libplasma-sonic

%description
Workspace components forked from KDE Plasma, optimized for SonicDE.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE*
%doc README.md
%{_bindir}/*
%{_datadir}/plasma-workspace/*
