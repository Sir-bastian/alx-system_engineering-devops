file { '/tmp/schol':
  ensure  => present,
  mode    => '0744',
  group   => 'www-data',
  owner   => www-data,
  content => "I love puppet\n",
  }
