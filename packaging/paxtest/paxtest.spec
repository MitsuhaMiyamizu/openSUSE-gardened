#
# spec file for package paxtest
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

Name:           paxtest
Version:	0.9.11
Release:	0
License:	GPLv2
Summary:	Test suite for the PaX kernel patch
Url:		http://pax.grsecurity.net
Group:		System/Aministration
Source:		%{name}-%{version}.tar.bz2
# from http://www.trapkit.de/tools/checksec.html
Source2:        checksec.sh
Patch1:         openSUSE.results.patch
PreReq:         binutils
BuildRequires:	make gcc binutils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PaX is a Linux kernel patch which adds much stricter control on how memory is
being used by applications. A normal Linux kernel leaves the control to the
application and does not implement any enforcement. Especially buffer overflow
attacks benefit from the absense of kernel enforced memory control. PaX tries
to do its best to enforce this control of memory used by applications, thereby
making it harder to successfully exploit buffer overflows.

Paxtest provides a regression test suite that covers most (but not all) of PaX
functionality. It can also be used to test other memory protection patches.

For more information about PaX, see http://pax.grsecurity.net/.

Additionally, checksec.sh utility is packaged: The checksec.sh script is
designed to test what standard Linux OS and PaX security features are being
used.

Source: http://www.trapkit.de/tools/checksec.html

%prep
%setup -q
%patch1 -p1

%build
make %{?_smp_mflags} BINDIR=%{_bindir} RUNDIR=%{_libdir}/%{name} linux

%install
install -d -m 755 $RPM_BUILD_ROOT/%{_libdir}/%{name}
%make_install -f Makefile.psm BINDIR=%{_bindir} RUNDIR=%{_libdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/%{name}/
install -m 644 results/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/

install -d -m 755 $RPM_BUILD_ROOT/%{_bindir}
install %{S:2} -m 755 $RPM_BUILD_ROOT/%{_bindir}

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING
%{_bindir}/paxtest
%{_bindir}/checksec.sh
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
