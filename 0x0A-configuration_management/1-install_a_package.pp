# Using Puppet, install flask from pip3.
package { 'flask from pip3':
  ensure          =>  'installed',
  install_options =>  ['-v', '2.1.0'],
}
