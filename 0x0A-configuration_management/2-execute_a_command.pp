# Kill a process named killmenow

exec { 'Kill a process':
  path        => '/usr/bin',
  command     => 'pkill -f killmenow',
  refreshonly => true,
  onlyif      => 'pgrep -f killmenow',
}
