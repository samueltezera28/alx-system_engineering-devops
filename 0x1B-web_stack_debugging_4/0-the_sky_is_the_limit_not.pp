# Increase nginx user limit

exec {'increase Ulimit':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin/',
}

exec { 'nginx':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
