#
# spec file for package gradm
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


%define upstream_release	201408301734
Name:           gradm
Version:        3.0
Release:        0
Summary:        Grsecurity administration tools
License:        GPL-2.0
Group:          System/Base
Url:            http://grsecurity.net
Source:         gradm-%{version}-%{upstream_release}.tar.gz
Patch1:         make-grsec_pam-with-pie.diff
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pam-devel
BuildRequires:  udev
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         permissions
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Grsecurity is a set of patches for the Linux kernel with an emphasis on
enhancing security. Its typical application is in computer systems that accept
remote connections from untrusted locations, such as web servers and systems
offering shell access to its users.

%prep
%setup -q -n %{name}
%patch1

%build
# fixme - taken from AUR build
sed -i -e 's/^CFLAGS :=/CFLAGS += /' Makefile
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d
# devnodes are not allowed here
%make_install MKNOD=/bin/true

%post
%set_permissions /sbin/gradm_pam

%verifyscript
%verify_permissions -e /sbin/gradm_pam

%files
%defattr(-,root,root)
# suid binary, not approved yet, suid dropped for now
%verify(not mode) %attr(0755, root, root) /sbin/gradm_pam
/sbin/gradm
/sbin/grlearn
%dir %{_sysconfdir}/grsec
%config %{_sysconfdir}/grsec/learn_config
%config %{_sysconfdir}/grsec/policy
%{_mandir}/man8/gradm.8*
%dir %{_sysconfdir}/udev/
%dir %{_sysconfdir}/udev/rules.d/
%config %{_sysconfdir}/udev/rules.d/80-grsec.rules
%dev(c,1,3,/dev/grsec)

%changelog
