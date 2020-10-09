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
cp Adwaita-blue -a -r  %{build_root}/usr/share/themes/Adwaita-blue
cp Adwaita-blue-dark -a -r  %{build_root}/usr/share/themes/Adwaita-blue-dark
cp Adwaita-cyan -a -r  %{build_root}/usr/share/themes/Adwaita-cyan
cp Adwaita-cyan-dark -a -r  %{build_root}/usr/share/themes/Adwaita-cyan-dark
cp Adwaita-grass -a -r  %{build_root}/usr/share/themes/Adwaita-grass
cp Adwaita-grass-dark -a -r  %{build_root}/usr/share/themes/Adwaita-grass-dark
cp Adwaita-gray -a -r  %{build_root}/usr/share/themes/Adwaita-gray
cp Adwaita-gray-dark -a -r  %{build_root}/usr/share/themes/Adwaita-gray-dark
cp Adwaita-green -a -r  %{build_root}/usr/share/themes/Adwaita-green
cp Adwaita-green-dark -a -r  %{build_root}/usr/share/themes/Adwaita-green-dark
cp Adwaita-indigo -a -r  %{build_root}/usr/share/themes/Adwaita-indigo
cp Adwaita-indigo-dark -a -r  %{build_root}/usr/share/themes/Adwaita-indigo-dark
cp Adwaita-magenta -a -r  %{build_root}/usr/share/themes/Adwaita-magenta
cp Adwaita-magenta-dark -a -r  %{build_root}/usr/share/themes/Adwaita-magenta-dark
cp Adwaita-orange -a -r  %{build_root}/usr/share/themes/Adwaita-orange
cp Adwaita-orange-dark -a -r  %{build_root}/usr/share/themes/Adwaita-orange-dark
cp Adwaita-pink -a -r  %{build_root}/usr/share/themes/Adwaita-pink
cp Adwaita-pink-dark -a -r  %{build_root}/usr/share/themes/Adwaita-pink-dark
cp Adwaita-red -a -r  %{build_root}/usr/share/themes/Adwaita-red
cp Adwaita-red-dark -a -r  %{build_root}/usr/share/themes/Adwaita-red-dark
cp Adwaita-teal -a -r  %{build_root}/usr/share/themes/Adwaita-teal
cp Adwaita-teal-dark -a -r  %{build_root}/usr/share/themes/Adwaita-teal-dark
cp Adwaita-violet -a -r  %{build_root}/usr/share/themes/Adwaita-violet
cp Adwaita-violet-dark -a -r  %{build_root}/usr/share/themes/Adwaita-violet-dark
cp Adwaita-yellow -a -r  %{build_root}/usr/share/themes/Adwaita-yellow
cp Adwaita-yellow-dark -a -r  %{build_root}/usr/share/themes/Adwaita-yellow-dark

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
