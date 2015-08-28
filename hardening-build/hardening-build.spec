#
# spec file for package hardening-build
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


Name:           hardening-build
Version:        0.1
Release:        0
Summary:        Collection of build hardening helpers
License:        GPL-2.0
Group:          System/Development
Source:         macros.hardening
Source1:        checksec
Source2:        README
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Collection of build hardening helpers, eg. build macros with PIE, RELRO flags,
compiler or linker wrappers.

%prep

%build

%install
install -d -m 755 %{buildroot}%{_sysconfdir}/rpm
install -m 644 %{_sourcedir}/macros.hardening %{buildroot}%{_sysconfdir}/rpm

install -d -m 755 %{buildroot}%{_libexecdir}/%{name}
install -m 755 %{SOURCE1} %{buildroot}%{_libexecdir}/%{name}

%files
%defattr(-,root,root)
#%doc README
%dir %{_sysconfdir}/rpm
%{_sysconfdir}/rpm/macros.hardening
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/checksec

%changelog
