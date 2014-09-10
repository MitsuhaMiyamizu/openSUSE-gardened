#
# spec file for package zypp-plugin-pax-flags
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


Name:           zypp-plugin-pax-flags
Version:        0.2
Release:        0
Summary:        ZYpp plugin to refresh PaX flags after update
License:        GPL-2.0
Group:          System Environment/Base
Source1:        pax-flags-plugin.py
Source2:        pax-plugin.logrotate
BuildArch:      noarch
Requires:       python
Requires:       zypp-plugin-python
Recommends:     logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This plugin refreshes system-wide PaX flags after zypper update finishes.

%prep

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/%{_prefix}/lib/zypp/plugins/commit
install -m 755 %{S:1} $RPM_BUILD_ROOT/%{_prefix}/lib/zypp/plugins/commit
install -d -m 755 $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d
install -m 644 %{S:2} $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/pax-plugin

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/zypp/
%dir %{_prefix}/lib/zypp/plugins
%dir %{_prefix}/lib/zypp/plugins/commit
%{_prefix}/lib/zypp/plugins/commit/pax-flags-plugin.py
%dir %{_sysconfdir}/logrotate.d
%{_sysconfdir}/logrotate.d/pax-plugin
