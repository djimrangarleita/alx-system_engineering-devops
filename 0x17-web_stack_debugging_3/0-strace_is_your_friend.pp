# Replace all occurences of phpp with php in wp-settings.php

exec {'Replace':
  path    => '/usr/bin',
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
