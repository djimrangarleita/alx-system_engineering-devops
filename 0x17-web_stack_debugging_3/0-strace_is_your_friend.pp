# Replace all occurences of phpp with php in wp-settings.php
exec { 'Replace':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
