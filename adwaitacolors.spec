Name:           AdwaitaColors
Version:        1.0
Release:        1
Summary:        A package that contains variations of Adwaita in different colors

Group:		Utilities
License:        GPL
URL:            https://github.com/Gnostiphage/adwaita-color-gen
Source0:        https://github.com/GustavoPeredo/adwaita-color-gen/raw/master/AdwaitaColors-1.0.tar.xz
BuildArch:	noarch   

%description
A package that contains variations of Adwaita in different colors

%prep
%setup -n AdwaitaColors-1.0

%install
mkdir -p %{buildroot}/usr/share/themes/
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-blue %{buildroot}/usr/share/themes/Adwaita-blue
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-blue-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-blue-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-cyan $RPM_BUILD_ROOT/usr/share/themes/Adwaita-cyan
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-cyan-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-cyan-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-grass $RPM_BUILD_ROOT/usr/share/themes/Adwaita-grass
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-grass-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-grass-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-gray $RPM_BUILD_ROOT/usr/share/themes/Adwaita-gray
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-gray-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-gray-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-green $RPM_BUILD_ROOT/usr/share/themes/Adwaita-green
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-green-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-green-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-indigo $RPM_BUILD_ROOT/usr/share/themes/Adwaita-indigo
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-indigo-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-indigo-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-magenta $RPM_BUILD_ROOT/usr/share/themes/Adwaita-magenta
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-magenta-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-magenta-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-orange $RPM_BUILD_ROOT/usr/share/themes/Adwaita-orange
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-orange-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-orange-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-pink $RPM_BUILD_ROOT/usr/share/themes/Adwaita-pink
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-pink-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-pink-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-red $RPM_BUILD_ROOT/usr/share/themes/Adwaita-red
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-red-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-red-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-teal $RPM_BUILD_ROOT/usr/share/themes/Adwaita-teal
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-teal-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-teal-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-violet $RPM_BUILD_ROOT/usr/share/themes/Adwaita-violet
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-violet-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-violet-dark
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-yellow $RPM_BUILD_ROOT/usr/share/themes/Adwaita-yellow
cp -r -a %{_builddir}/AdwaitaColors-1.0/Adwaita-yellow-dark $RPM_BUILD_ROOT/usr/share/themes/Adwaita-yellow-dark

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
