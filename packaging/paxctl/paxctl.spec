#
# spec file for package paxctl
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

Name:           paxctl
Version:	0.8
Release:	0
License:	GPLv2
Summary:	User-space utility to control PaX flags
Url:		http://pax.grsecurity.net
Group:		System/Administration
Source:		%{name}-%{version}.tar.bz2
Patch1:		makefile-no-install-perms.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The tool named paxctl allows PaX flags to be modified on a per-binary basis.
PaX is part of common security-enhancing kernel patches and secure
distributions, such as GrSecurity and Hardened Gentoo, respectively.  Your
system needs to be running a properly patched and configured kernel for this
program to have any effect.

%prep
%setup -q
%patch1

%build
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_sbindir}/paxctl
%{_mandir}/man1/paxctl.*
