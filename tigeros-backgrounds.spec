Name:           tigeros-backgrounds
Version:        1.0
Release:        20%{?dist}
Summary:        Desktop images for the TigerOS Fedora Remix

License:        CC-BY-SA-4.0
URL:            https://github.com/RITlug/tigeros-backgrounds
Source0:        %{name}-%{version}-%{release}.tar.gz

BuildArch:      noarch
Requires:       glib2
Requires:       dconf

%description
The tigeros-backgrounds package contains
tigeros related artwork intended to be used 
as a desktop background image.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_datadir}/backgrounds/tigeros/wallpapers
mkdir -p %{buildroot}%{_datadir}/backgrounds/tigeros/lockscreens
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas

for i in wallpapers/*
do
	install -m 644 $i %{buildroot}%{_datadir}/backgrounds/tigeros/wallpapers
done

for i in lockscreens/*
do
	install -m 644 $i %{buildroot}%{_datadir}/backgrounds/tigeros/lockscreens
done

install -D -m 644 tigeros-backgrounds.xml %{buildroot}%{_datadir}/gnome-background-properties/tigeros-backgrounds.xml
install -m 644 20_tigeros.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/20_tigeros.gschema.override
install -m 644 tigeros.xml %{buildroot}%{_datadir}/backgrounds/tigeros/tigeros.xml

%post
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null
dconf update

%postun
rm %{_datadir}/glib-2.0/schemas/20_tigeros.gschema.override
rm -rf %{_datadir}/backgrounds/tigeros
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null
dconf update

%files
%defattr(-,root,root,-)
%doc LICENSE
/usr/share/gnome-background-properties
/usr/share/glib-2.0/schemas/20_tigeros.gschema.override
/usr/share/backgrounds/tigeros/tigeros.xml
# Wallpapers
/usr/share/backgrounds/tigeros/wallpapers/orange_simple-1920x1080.png
/usr/share/backgrounds/tigeros/wallpapers/orange_colorful-1920x1080.png
/usr/share/backgrounds/tigeros/wallpapers/white_simple-1920x1080.png
/usr/share/backgrounds/tigeros/wallpapers/black_and_white-1920x1080.png
/usr/share/backgrounds/tigeros/wallpapers/dark_colorful-1920x1080.png
/usr/share/backgrounds/tigeros/wallpapers/dark_simple-1920x1080.png
# Lockscreens
/usr/share/backgrounds/tigeros/lockscreens/dark_left-1920x1080.png
/usr/share/backgrounds/tigeros/lockscreens/dark_no_tiguin-1920x1080.png
/usr/share/backgrounds/tigeros/lockscreens/dark_right-1920x1080.png
/usr/share/backgrounds/tigeros/lockscreens/orange_left-1920x1080.png
/usr/share/backgrounds/tigeros/lockscreens/orange_no_tiguin-1920x1080.png
/usr/share/backgrounds/tigeros/lockscreens/orange_right-1920x1080.png

%changelog
* Mon Aug 13 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-20
- Fix filename error

* Sat Aug 11 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-19
- Add lockscreen images
- Rename images to match view

* Thu May 24 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-18
- Change images to PNG
- update files

* Tue May 8 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-17
- Fixed post uninstall
- Added tigeros.xml

* Wed Aug 30 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-16
- rebuilt for Fedora 26

* Wed May 31 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-15
- fix typo in wallpaper override

* Thu May 25 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-14
- add wallpaper override

* Sun May 14 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-13
- fix xml so wallpapers are zoomed

* Wed Apr 26 2017 Regina Locicero <rtl3971@rit.edu> - 1.0-12
- Added wallpapers
