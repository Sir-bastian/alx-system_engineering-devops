#A puppet manifest that creates a file in /tmp

file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
  }
