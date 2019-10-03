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

    # Don't use host.sudo() since it doesn't simulate sudo -i
    restorePath = "/tmp/test-restore"
    assert host.run_expect([0], "sudo -i -u postgres duply postgresql backup")
    assert host.run_expect([0], (
        "sudo -i -u postgres duply postgresql restore " +
        restorePath
    ))

    restoreFile = host.file(restorePath)
    assert restoreFile.exists
    assert restoreFile.is_file
    assert restoreFile.contains("PostgreSQL database dump complete")
