#A puppet manifest that installs flask from pip3


exec { 'pkill':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0',
}
