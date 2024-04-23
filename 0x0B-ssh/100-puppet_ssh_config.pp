# Create config params for ssh connection

file { 'Create file':
  path    => '/etc/ssh/ssh_config',
  content => "Host 54.160.125.191
	  HostName 54.160.125.191
	  User ubuntu
	  IdentityFile '~/.ssh/school'
	  PasswordAuthentication no\n"
}
