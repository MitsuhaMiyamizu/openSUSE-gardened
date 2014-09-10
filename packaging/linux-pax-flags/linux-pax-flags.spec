#
# spec file for package linux-pax-flags
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           linux-pax-flags
Version:	2.0.16
Release:	3
License:	GPLv3
Summary:	Deactivates PaX flags for several binaries to work with PaX enabled kernels
Url:		https://github.com/kdave/linux-pax-flags
Group:		System/Administration
Source:		%{name}.tar.bz2
Requires:	ruby paxctl elfix sudo
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deactivates PaX flags for several binaries to work with PaX enabled kernels.

%prep
%setup -q -n %{name}

%build

%install
install -d -m755 $RPM_BUILD_ROOT/%{_sbindir}
install -m755 linux-pax-flags.sh $RPM_BUILD_ROOT/%{_sbindir}/%{name}
install -m755 linux-pax-flags.rb $RPM_BUILD_ROOT/%{_sbindir}/%{name}.rb
install -d -m755 $RPM_BUILD_ROOT/%{_mandir}/man8
install -m644 linux-pax-flags.8 $RPM_BUILD_ROOT/%{_mandir}/man8
ls $RPM_BUILD_ROOT/%{_mandir}/man8
install -d -m750 $RPM_BUILD_ROOT/etc/pax-flags

install -d -m750 $RPM_BUILD_ROOT/usr/share/%{name}
for conf in *.conf; do
	install -m600 "$conf" $RPM_BUILD_ROOT/usr/share/%{name}
done

%files
%defattr(-,root,root)
%dir /etc/pax-flags
%dir /usr/share/%{name}
%{_sbindir}/%{name}
%{_sbindir}/%{name}.rb
%{_mandir}/man8/%{name}.8*
/usr/share/%{name}/*
