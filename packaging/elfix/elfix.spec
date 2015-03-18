#
# spec file for package elfix
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

Name:           elfix
Version:	0.9
Release:	0
%define         git_version 666190ea1a94
License:	GPL-2.0
Summary:	Utilities to modify Elf binaries to work with PaX hardened kernel
Url:		http://www.gentoo.org
#GitUrl:	git://git.overlays.gentoo.org/proj/elfix.git
Group:		System/Administration
Source:         %{name}-%{version}_g%{git_version}.tar.bz2
Provides:	paxctl-ng
BuildRequires:	automake make autoconf libtool libelf-devel attr-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Utilities to modify Elf binaries to work with PaX hardened kernel.

%prep
%setup -q

%build
sh ./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING
%{_sbindir}/migrate-pax
%{_sbindir}/paxctl-ng
%{_sbindir}/paxmark.sh
%{_sbindir}/pypaxctl
%{_sbindir}/revdep-pax
%{_mandir}/man1/paxctl-ng.1*
%{_mandir}/man1/revdep-pax.1*
