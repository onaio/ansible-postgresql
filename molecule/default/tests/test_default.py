import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_backups(host):
    backupDir = host.file("/backups/postgresql")
    assert backupDir.exists
    assert backupDir.user == "postgres"
    assert backupDir.group == "postgres"
    assert backupDir.is_directory
    assert oct(backupDir.mode) == "0o750"

    # Create the database and insert data into it
    testString = "fddsafds test string fddadsfd"
    with host.sudo("postgres"):
        host.run("psql -c 'create database test'")
        host.run(
            "psql -c 'create table t1(c1 text null)' test"
        )
        host.run((
            "psql -c \"insert into t1(c1) values('" +
            testString +
            "')\" test"
        ))

    # Check if duply can backup and restore into a file
    # Don't use host.sudo() since it doesn't do sudo -i
    restorePath = "/tmp/test-restore.sql"
    # Full backup
    assert host.run_expect([0], "sudo -i -u postgres duply postgresql backup")
    # Incremental backup
    assert host.run_expect([0], "sudo -i -u postgres duply postgresql backup")
    assert host.run_expect([0], (
        "sudo -i -u postgres duply postgresql restore " +
        restorePath
    ))

    # Check if duply restore is OK
    restoreFile = host.file(restorePath)
    assert restoreFile.exists
    assert restoreFile.is_file
    assert restoreFile.contains(testString)
