#!/usr/bin/env ruby

txtfrom = ARGV[0].scan(/from:(\+?[a-zA-Z0-9]{1,})?/).join;
txtto = ARGV[0].scan(/to:(\+?[a-zA-Z0-9]{1,})?/).join;
txtflag = ARGV[0].scan(/flags:([-:01]{1,})/).join;

output = txtfrom + ',' + txtto + ',' + txtflag;

puts output
