%global debug_package %{nil}
Summary: Tools for managing OSG Hosted CEs
Name: hosted-ce-tools
Version: 1.0
Release: 4%{?dist}
License: Apache 2.0
Url: https://github.com/opensciencegrid/hosted-ce-tools
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: fetch-crl
Requires: sudo
Requires: wget
Requires: rsync
Requires: perl
Requires: /usr/bin/git
%systemd_requires


%description
%{summary}


%prep
%setup -q


%build
exit 0


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/cvmfsexec-osg-wrapper
%{_bindir}/make-cvmfsexec-tarball
%{_bindir}/update-remote-wn-client
%{_bindir}/update-all-remote-wn-clients
%config(noreplace) %{_sysconfdir}/endpoints.ini
%{_unitdir}/update-all-remote-wn-clients.service
%{_unitdir}/update-all-remote-wn-clients.timer
%dir /var/log/update-remote-wn-client


%post
%systemd_post update-all-remote-wn-clients.service update-all-remote-wn-clients.timer
systemctl daemon-reload


%preun
%systemd_preun update-all-remote-wn-clients.service update-all-remote-wn-clients.timer


%changelog
* Thu Jun 08 2023 Matt Westphall <westphall@wisc.edu> - 1.0-4
- Add missing dependencies on perl and rsync to spec file (SOFTWARE-5131)

* Fri Jun 02 2023 Matt Westphall <westphall@wisc.edu> - 1.0-3
- Remove dependency on python-six (SOFTWARE-5131)

* Mon Mar 06 2023 Brian Lin <blin@cs.wisc.edu> - 1.0-2
- Fix missed conversion to python3 (SOFTWARE-5131)

* Thu Feb 09 2023 Carl Edquist <edquist@cs.wisc.edu> - 1.0-1
- Release hosted-ce-tools 1.0 (SOFTWARE-5130)
- Convert scripts to python3 (SOFTWARE-5131)
- Timeout rsync in update-remote-wn-client (SOFTWARE-4670)
- Dereference hardlinks when extracting tarball (SOFTWARE-5254)

* Wed Mar 02 2022 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.11-1
- Generalize cvmfsexec-osg-wrapper (SOFTWARE-4722)
- Have make-cvmfsexec-tarball generate a multiplatform tarball

* Mon Oct 25 2021 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.10-1
- Add cvmfsexec-osg-wrapper and make-cvmfsexec-tarball

* Tue Nov 03 2020 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.9-1
- Fix reversed test

* Wed Sep 09 2020 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.8-2
- Fix python-six dependency for EL8

* Wed Sep 09 2020 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.8-1
- Download osg-ca-manage from GitHub instead of using a tarball client for fetching CAs (SOFTWARE-4242)

* Tue May 05 2020 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.7-1
- Fix bug in timeout where sudo would prompt the user for a password (SOFTWARE-4081)

* Thu Apr 30 2020 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.6-1
- Have update-all-remote-wn-ce run updaters with a timeout (SOFTWARE-4081)
- If one update fails, keep going with the other updates instead of bailing out

* Fri Dec 20 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.5-2
- Require sudo (SOFTWARE-3954)

* Wed Nov 13 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.5-1
- Don't run updaters in parallel (PR #1)

* Tue Sep 17 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.4-1
- Add --dry-run option to update-all-remote-wn-clients script
- Allow more characters in endpoint names in endpoints.ini

* Wed Sep 11 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.3-1
- Use system fetch-crl
- Change config file name and log directory name

* Tue Sep 10 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.2-1
- Fixes

* Tue Sep 10 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-3
- Add systemd timer and service

* Fri Sep 06 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-2
- update-all-remote-wn-clients script and associated config file and log dir

* Thu Sep 05 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-1
- Initial


# vim:ft=spec
