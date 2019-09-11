hosted-ce-tools
===============
Tools for maintaining an OSG Hosted CE

This repo contains scripts, services, timers, etc. that are useful for managing an OSG Hosted CE.


update-remote-wn-client
-----------------------

This script does the following for a single remote host:

- download and extract a worker node tarball
- set up the worker node paths to work on the remote host
- download the latest CA certs and CRLs into the worker node installation
- rsync the above to the remote host

Run it as the user that will be doing bosco submission.
An SSH key already needs to be set up on the remote host.
Run `update-remote-wn-client --help` for a list of arguments and defaults.


update-all-remote-wn-clients
----------------------------

This service periodically runs `update-remote-wn-client` for a list of endpoints.
The endpoints are specified as sections in `/etc/hosted-ces.ini`.
An example endpoint is provided in the default config file.

This can be run as a script or as a systemd service.
To run it as a service:

```
# systemctl enable --now update-all-remote-wn-clients
```

Logs will be in `/var/log/updatewn`.
Each endpoint will have its own logfile.


Known issue(s)
--------------

- `update-all-remote-wn-clients` separately downloads the tarball, CAs, and CRLs
  for each endpoint in the configuration

