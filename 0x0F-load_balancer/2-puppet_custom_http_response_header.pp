# Install new nginx, configure and create 301 redirection
exec { 'Update system':
  path        => '/usr/bin',
  command     => 'apt-get -y update',
  refreshonly => true,
}

package { 'nginx':
  ensure => installed
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n"
}

file { '/usr/share/nginx/html/c_404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n\n"
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	error_page 404 /c_404.html;
	add_header X-Served-By ${hostname};
	location = /c_404.html {
		root /usr/share/nginx/html;
		internal;
	}
}
"
}

exec { 'Restart server':
  command => '/usr/sbin/service nginx restart'
}