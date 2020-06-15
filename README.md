onaio - PostgreSQL ![CI](https://github.com/onaio/ansible-postgresql/workflows/CI/badge.svg?master)
=========

Installs PostgreSQL and optionally configures encrypted backups.

Role Variables
--------------

- `postgresql_backup_enabled` - Whether to configure backups or not. Default is `true`
- `postgresql_backup_import_gpg_keys` - Whether to import PGP keys if backups are enabled. Default is `true`
- `postgresql_backup_gpg_private_key` - Path to the PGP private key to import. Key will be used to decrypt the backups.
- `postgresql_backup_gpg_public_key` - Path to the PGP public key to import. Key will be used to encrypt the backups.
- `postgresql_backup_gpg_trust_file` - Path to the PGP trust file that adds trust for the keypair being imported.
- `postgresql_backup_database` - The database that will be backed up.
- `postgresql_backup_gpg_key_id` - The ID of the PGP private key to be used to encrypt the backups.
- `postgresql_backup_gpg_pass` - The passphrase for the private PGP key to be used to decrypt backups.
- `postgresql_enable_ssl` - Whether to install a TLS certificate for the PostgreSQL server. This is set to true by default.
- `postgresql_ssl_domain` - The hostname/domain name to set as the common name in the TLS certificate.
- `postgresql_ssl_ca_key` - The contents of the TLS CA key to sign the PostgreSQL server's certificate.
- `postgresql_ssl_ca_cert` - The contents of the TLS CA certificate who's key signed the PostgreSQL server's certificate.
- `postgresql_ssl_server_cert_expiry_days` - The number of days after creation before the PostgreSQL server's TLS certificate expires.

Dependencies
------------

- ANXS.postgresql
- [onaio.gpg-import](https://github.com/onaio/ansible-gpg-import)
- [onaio.backup](https://github.com/onaio/ansible-backup)
- [onaio.ssl-certificate](https://github.com/onaio/ansible-ssl-certificate)

Testing
-------

You can test the role locally using Molecule by following these steps:

```sh
pip install molecule docker-py
molecule test
```

Note that the secrets in the molecule directory are intended to be used for testing purposes only. Please do not use them in actual deployments.

> Note: Please make sure the repository on your host is named exactly `ansible-postgresql`.

License
-------

Apache 2
