# Create config params for ssh connection

file { 'Create file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => "${file('/etc/ssh/ssh_config')}Host 54.160.125.191
	  HostName 54.160.125.191
	  User ubuntu
	  IdentityFile '~/.ssh/school'
	  PasswordAuthentication no\n"
}
