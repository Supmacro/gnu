
# Replace the entire content with the '' character 
:<<SEOF
sed -e 's///' $1 > $2
SEOF

# General operation of string variables 
:<<STRV
var='/snv/nothing/snv'

# Delete the first'/' and the left substring in the string 
${var#*/}
# Delete the last '/' and the left substring in the string
${var##*/}

# Delete the first'/' and the right substring in the string
${var%%/*}
# Delete the last '/' and the right substring in the string
${var%/*}

# Extract the characters of index 1-7
${var:1:7}

# Replace the first 'svn' in the string with 'nvs'
${var/snv/vns}
# Replace all 'svn' in the string with 'nvs'
${var//snv/vns}
STRV

# Input and output redirection general operation
:<<IO
stdin  :  0
stdout :  1
stderr :  2

# Output redirection
>, >>
# Input redirection
<, <<

# Redirect standard output to /dev/null device
out > /dev/null 2>&1

# Truncate the file to 0 bytes, if the file does not exist, 
# create the file
:> file

# Redirect the pipe to file descriptor 6 in read-write mode
exec 6<>fifo

IO
