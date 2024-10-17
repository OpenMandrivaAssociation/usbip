%define name usbip
%define version 0.1.7
%define release 4
%define libname %mklibname usbip 0
%define develname %mklibname -d usbip 0
%define develname_static %mklibname -d -s usbip 0

Name: %name
Summary: USB device sharing system over IP network
Version: %version
Release: %release
License: GPLv2+
Group: System/Configuration/Networking
Source0: http://downloads.sourceforge.net/project/usbip/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0: usbip-0.1.7-aux_dir.patch
Patch1:	usbip-0.1.7-usb.ids_dir.patch
URL: https://%name.sourceforge.net/

BuildRequires: glib2-devel >= 2.6.0
BuildRequires: sysfsutils-devel

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
programs which make use of %name.


%package -n %develname_static
Summary: Development files for %libname
Group: Development/C
Provides: lib%name-static-devel = %version-%release
Requires: %name-devel = %version-%release
Provides: %{name}-static-devel = %version-%release

%description -n %develname_static
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
programs which make use of %name.


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

%install
rm -rf %buildroot
%makeinstall -C src

%files -n %libname
%doc src/AUTHORS NEWS README
%_libdir/*.so.*

%files client
%doc src/README
%_bindir/%name

%files server
%doc src/README
%_bindir/%{name}d
%_bindir/bind_driver

%files -n %develname
%_libdir/*.so
%_includedir/*

%files -n %develname_static
%_libdir/*.a
