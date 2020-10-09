Name:           AdwaitaColors
Version:        1.0
Release:        1%{?dist}
Summary:        A package that contains variations of Adwaita in different colors

Group:		Utilities
License:        GPL
URL:            https://github.com/Gnostiphage/adwaita-color-gen
Source0:        AdwaitaColors-%{version}.tar.xz
BuildArch:	noarch   

%description
A package that contains variations of Adwaita in different colors

%prep


%build


%install
cp -r Adwaita-blue $RPM_BUILD_ROOT/usr/share/themes/Adwaita-blue
cp -r Adwaita-blue-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-blue-dark
cp -r Adwaita-cyan $RPM_BUILD_ROOT/usr/share/themes/Adwaita-cyan
cp -r Adwaita-cyan-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-cyan-dark
cp -r Adwaita-grass $RPM_BUILD_ROOT/usr/share/themes/Adwaita-grass
cp -r Adwaita-grass-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-grass-dark
cp -r Adwaita-gray $RPM_BUILD_ROOT/usr/share/themes/Adwaita-gray
cp -r Adwaita-gray-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-gray-dark
cp -r Adwaita-green $RPM_BUILD_ROOT/usr/share/themes/Adwaita-green
cp -r Adwaita-green-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-green-dark
cp -r Adwaita-indigo $RPM_BUILD_ROOT/usr/share/themes/Adwaita-indigo
cp -r Adwaita-indigo-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-indigo-dark
cp -r Adwaita-magenta $RPM_BUILD_ROOT/usr/share/themes/Adwaita-magenta
cp -r Adwaita-magenta-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-magenta-dark
cp -r Adwaita-orange $RPM_BUILD_ROOT/usr/share/themes/Adwaita-orange
cp -r Adwaita-orange-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-orange-dark
cp -r Adwaita-pink $RPM_BUILD_ROOT/usr/share/themes/Adwaita-pink
cp -r Adwaita-pink-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-pink-dark
cp -r Adwaita-red $RPM_BUILD_ROOT/usr/share/themes/Adwaita-red
cp -r Adwaita-red-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-red-dark
cp -r Adwaita-teal $RPM_BUILD_ROOT/usr/share/themes/Adwaita-teal
cp -r Adwaita-teal-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-teal-dark
cp -r Adwaita-violet $RPM_BUILD_ROOT/usr/share/themes/Adwaita-violet
cp -r Adwaita-violet-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-violet-dark
cp -r Adwaita-yellow $RPM_BUILD_ROOT/usr/share/themes/Adwaita-yellow
cp -r Adwaita-yellow-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-yellow-dark

%files
%defattr(-,root,root,-)
/usr/share/themes/Adwaita-blue
/usr/share/themes/Adwaita-blue-dark
/usr/share/themes/Adwaita-cyan
/usr/share/themes/Adwaita-cyan-dark
/usr/share/themes/Adwaita-grass
/usr/share/themes/Adwaita-grass-dark
/usr/share/themes/Adwaita-gray
/usr/share/themes/Adwaita-gray-dark
/usr/share/themes/Adwaita-green
/usr/share/themes/Adwaita-green-dark
/usr/share/themes/Adwaita-indigo
/usr/share/themes/Adwaita-indigo-dark
/usr/share/themes/Adwaita-magenta
/usr/share/themes/Adwaita-magenta-dark
/usr/share/themes/Adwaita-orange
/usr/share/themes/Adwaita-orange-dark
/usr/share/themes/Adwaita-pink
/usr/share/themes/Adwaita-pink-dark
/usr/share/themes/Adwaita-red
/usr/share/themes/Adwaita-red-dark
/usr/share/themes/Adwaita-teal
/usr/share/themes/Adwaita-teal-dark
/usr/share/themes/Adwaita-violet
/usr/share/themes/Adwaita-violet-dark
/usr/share/themes/Adwaita-yellow
/usr/share/themes/Adwaita-yellow-dark
%doc


%changelog
* Fri Sep 18 2020 GustavoPeredo <gustavomperedo@gmail.com>
- 
