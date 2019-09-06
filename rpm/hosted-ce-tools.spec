%global debug_package %{nil}
Summary: Tools for managing OSG Hosted CEs
Name: hosted-ce-tools
Version: 0.1
Release: 2%{?dist}
License: Apache 2.0
Url: https://github.com/opensciencegrid/hosted-ce-tools
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: python-six


%description
%{summary}


%prep
%setup -q


%build
%py2_build


%install
%py2_install
rm -rf %{buildroot}%{python2_sitelib}/*.egg-info
install -D -m 0644 config/hosted-ces.ini %{buildroot}/etc/hosted-ces.ini
mkdir -p %{buildroot}/var/log/updatewn


%files
%{_bindir}/update-remote-wn-client
%{_bindir}/update-all-remote-wn-clients
%config(noreplace) /etc/hosted-ces.ini
%dir /var/log/updatewn


%changelog
* Fri Sep 06 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-2
- update-all-remote-wn-clients script and associated config file and log dir

* Thu Sep 05 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-1
- Initial


# vim:ft=spec
