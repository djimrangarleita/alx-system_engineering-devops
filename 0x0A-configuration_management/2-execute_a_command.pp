# Kill a process named killmenow

exec { 'Kill a process':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
