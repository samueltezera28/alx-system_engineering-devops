# Removes erroneous wordpress file extensions from phpp to php

exec { 'wordpress site running on apache':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
