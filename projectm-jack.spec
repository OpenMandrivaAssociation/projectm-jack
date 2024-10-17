%define oname projectM


Name:		projectm-jack
Version:	2.1.0
Release:	1
Summary:	The projectM visualization plugin for jack
Group:		Sound
License:	GPLv2+ and MIT
URL:		https://projectm.sourceforge.net/
Source0:	http://downloads.sourceforge.net/projectm/projectM-complete-%{version}-Source.tar.gz
BuildRequires:	cmake projectm-qt-devel jackit-devel desktop-file-utils

%description
This package allows the use of the projectM visualization plugin through any
JACK compatible applications.

%prep
%setup -q -n %{oname}-complete-%{version}-Source/

%build
pushd src/projectM-jack
%cmake 
%make
popd

%install
pushd src/projectM-jack
%makeinstall_std -C build/
popd

%files
#%doc ChangeLog COPYING
%{_bindir}/%{oname}-jack
%{_datadir}/applications/%{oname}-jack.desktop
