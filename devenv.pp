package {'python-setuptools': ensure=>installed}

exec {'install-pip':
  command => '/usr/bin/easy_install pip',
  creates => '/usr/local/bin/pip',
  require => Package['python-setuptools'],
}

exec {'install-virtualenv':
  command => '/usr/local/bin/pip install virtualenv',
  creates => '/usr/local/bin/virtualenv',
  require => Exec['install-pip'],
}

exec {'install-virtualenvwrapper':
  command => '/usr/local/bin/pip install virtualenvwrapper',
  creates => '/usr/local/bin/virtualenvwrapper.sh',
  require => [Exec['install-pip'], Exec['install-virtualenv']],
}
