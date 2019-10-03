onaio - PostgreSQL [![Build Status](https://travis-ci.org/onaio/ansible-postgresql.svg?branch=master)](https://travis-ci.org/onaio/ansible-postgresql)
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

Dependencies
------------

- ANXS.postgresql
- onaio.gpg-import
- Stouts.backup 

License
-------

Apache 2
