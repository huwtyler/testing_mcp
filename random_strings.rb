# Write a script that outputs a list of random 5 alphanumeric strings,
# containing uppercase letters and numbers only. The script outputs 20 at a time.

CHARS = ('A'..'Z').to_a + ('0'..'9').to_a

20.times do
  puts Array.new(5) { CHARS.sample }.join
end
