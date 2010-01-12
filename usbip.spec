%define name usbip
%define version 0.1.7
%define release %mkrel 2
%define libname %mklibname usbip 0
%define develname %mklibname -d usbip 0

Name: %name
Summary: USB device sharing system over IP network
Version: %version
Release: %release
License: GPLv2+
Group: System/Configuration/Networking
Source0: http://downloads.sourceforge.net/project/usbip/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0: usbip-0.1.7-aux_dir.patch
Patch1:	usbip-0.1.7-usb.ids_dir.patch
URL: http://%name.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: glib2-devel >= 2.6.0
BuildRequires: libsysfs-devel

%description
The USB/IP Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, USB/IP encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

%package -n %libname
Summary: Shared library for USB/IP utils
Group: System/Libraries

%description -n %libname
The USB/IP Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, USB/IP encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

This package contains shared library for USB/IP utils.

%package -n %develname
Summary: Development files for %libname
Group: Development/C
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release
Requires: %libname = %version-%release

%description -n %develname
The USB/IP Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, USB/IP encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

This package contains the libraries and header files needed to develop
programs which make use of %lname.

%package client
Summary: USB/IP client utility
Group: System/Configuration/Networking
Requires: kmod(vhci-hcd)

%description client
The USB/IP Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, USB/IP encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

This package contains USB/IP client utility.


%package server
Summary: USB/IP server utils
Group: System/Configuration/Networking
Requires: kmod(usbip)

%description server
The USB/IP Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, USB/IP encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

This package contains USB/IP client utils.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
pushd src
./autogen.sh
%configure2_5x --disable-usbids-install
%make
popd

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
%makeinstall -C src

%files -n %libname
%defattr(-, root, root)
%doc src/AUTHORS NEWS README
%_libdir/*.so.*

%files client
%defattr(-, root, root)
%doc src/README
%_bindir/%name

%files server
%defattr(-, root, root)
%doc src/README
%_bindir/%{name}d
%_bindir/bind_driver

%files -n %develname
%defattr(-, root, root)
%_libdir/*.so
%_libdir/*.a
%_libdir/*.la
%_includedir/*
