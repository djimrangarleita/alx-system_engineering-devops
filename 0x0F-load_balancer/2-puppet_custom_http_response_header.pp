# Install new nginx, configure and create 301 redirection
exec { 'Update system':
  path        => '/usr/bin',
  command     => 'apt-get update',
  refreshonly => true,
}

package { 'nginx':
  ensure => installed
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n"
}

$hostname_output = $facts['networking']['hostname']

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	location / {
		add_header X-Served-By ${hostname_output};
		try_files \$uri \$uri/ =404;
	}
}
"
}

exec { 'Restart server':
  command => '/usr/sbin/service nginx restart'
}
