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
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-blue
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-blue-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-cyan
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-cyan-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-grass
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-grass-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-gray
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-gray-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-green
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-green-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-indigo
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-indigo-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-magenta
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-magenta-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-orange
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-orange-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-pink
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-pink-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-red
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-red-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-teal
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-teal-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-violet
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-violet-dark
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-yellow
install -d $RPM_BUILD_ROOT/usr/share/themes/Adwaita-yellow-dark

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
