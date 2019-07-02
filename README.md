Easy-RSA
=========

This Ansible role installs and configures EasyRSA. Use this role to create your
PKI. If you are rolling out your own OpenVPN server, this could be the first step.

https://www.techchorus.net/blog/run-your-own-openvpn-server/

Requirements
------------
For CentOS, EPEL repository must be enabled. You can do it using
[bngsudheer.centos_base](https://galaxy.ansible.com/bngsudheer/centos_base) or
another means.

In order to build a CA server and an OpenVPN server using gavika.easy_rsa and
gavika.openvpn, you have to execute the roles a few times depending on your
needs. You are responsible to execute them the required number of times and in
required order. Examples are provided in gavika.openvpn documentation.

Example contents of ca_open_vpn_extra_vars.yml
```yml
---
easy_rsa_server_request_to_import: server.req
```

Role Variables
--------------
```yml
easy_rsa_ca_server_mode: true
easy_rsa_req_country: ""
easy_rsa_req_province: ""
easy_rsa_req_city: ""
easy_rsa_req_org: ""
easy_rsa_req_email: ""
easy_rsa_req_ou: ""
easy_rsa_dn: ""
```


Dependencies
------------
EPEL must be enabled on CentOS. No dependencies for Ubuntu.

Example Playbook
----------------
```yml
---
  - hosts: my_ca_server
    vars:
      easy_rsa_req_country: "IN"
      easy_rsa_req_province: "KA"
      easy_rsa_req_city: "Bangalore"
      easy_rsa_req_org: "My Organization"
      easy_rsa_req_email: "admin@example.com"
      easy_rsa_req_ou: "My Organization Unit"
      easy_rsa_dn: "vpn.example.com"
      easy_rsa_build_ca: true
    roles:
      - role: gavika.easy_rsa
```

License
-------
Apache License, Version 2.0


Author Information
------------------

Sudheera Satyanarayana


* Gavika: https://www.gavika.com

* Blog: https://www.techchorus.net
* Twitter: https://www.twitter.com/bngsudheer
* Github: https://github.com/bngsudheer
