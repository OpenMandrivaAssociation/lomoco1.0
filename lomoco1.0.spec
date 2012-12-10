%define libname %mklibname lomoco 0
%define libnamed %mklibname lomoco -d

Name:           lomoco1.0
Version:        1.0
Release:        %mkrel 6
Summary:        Logitech mouse control tool
License:        GPL
Group:          System/Configuration/Hardware
URL:            http://www.lomoco.org/
Source0:        http://www.lomoco.org/lomoco-%{version}.tar.gz
BuildRequires:  libusb-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Lomoco can configure vendor-specific options on Logitech USB mice (or
dual-personality mice plugged into the USB port). A number of recent devices
are supported. The program is mostly useful in setting the resolution to 800
cpi or higher on mice that boot at 400 cpi (such as the MX500, MX510, MX1000
etc.), and disabling SmartScroll or Cruise Control for those who would rather
use the two extra buttons as ordinary mouse buttons.

Supported devices:

Cordless Mouse Receiver
Cordless MouseMan Optical
Cordless Optical Mouse
Cordless TrackMan Wheel
G3 Gaming Laser Mouse
G5 Gaming Laser Mouse
MX Revolution Mouse
MX1000 Laser Cordless Mouse
MX300 Optical Mouse
MX310 Optical Mouse
MX500 Optical Mouse
MX510 Optical Mouse
MX518 Optical Mouse
MX900 Cordless Mouse
MouseMan Dual Optical
MouseMan Traveler
Optical Wheel Mouse
USB Receiver
UltraX Optical Mouse
V200 Cordless Notebook Mouse
VX Revolution Mouse
Wheel Mouse Optical
diNovo Media Desktop Receiver
iFeel Mouse

%prep
%setup -q -n lomoco-%{version}
./autogen.sh

%build
%{configure2_5x}
%{make}
                                                        
%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/lomoco
%{_mandir}/man1/lomoco.1*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2011.0
+ Revision: 620256
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2010.0
+ Revision: 433732
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 251375
- rebuild

* Fri Feb 08 2008 David Walluck <walluck@mandriva.org> 1.0-1mdv2008.1
+ Revision: 164320
- import lomoco1.0


