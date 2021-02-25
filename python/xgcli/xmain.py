
import click
import sys
import getpass
import os

from configobj import ConfigObj

class XCli(object):
    
    options = {
        'host' : None,
        'port' : None,
        'database' : None,
        'user': None,
        'password': None,
        'charset': None,

        'login' : {
            'config' : None,
            'user' : None,
            'home' : None,
        }
    }
 
    version = '0.0.0'

    def __init__(self, host=None, port=None, database=None, user=None, 
                        passwd=None, charset=None):
        '''XCli's constructor'''
        self.options['login']['user'] = getpass.getuser()
        self.options['login']['home'] = os.environ.get('HOME')
        self.options['login']['config'] = '/home/xgcli/configrc' 

        self.options['host'] = host
        self.options['port'] = port
        self.options['database'] = database
        self.options['user'] = user
        self.options['password'] = passwd
        self.options['charset'] = charset

    def z_version(self, isecho):
        ''' Need to print the version number of the current program? '''
        if isecho:
            click.secho('%s' % self.version, fg='green')
            sys.exit(0) 

    def z_parse_opts(self):
        '''Analyze the user's input parameter options. 
           If there are default parameter options, the program will 
           actively read the content in the ~/.xgclirc configuration 
           file.
        '''
        cobj = ConfigObj(self.options['login']['config'], 
                list_values=True, interpolation=False, encoding='UTF-8')
        cobjks = cobj.keys()
        optsks = self.options.keys()
        def get(opt):
            if opt in cobjks and cobj[opt]:
                self.options[opt] = cobj[opt]
            return self.options[opt] 
 
        return {x: get(x) for x in optsks if not self.options[x]}


@click.command()
@click.option('-h', '--host', help='Host address of the database. In addition,'
  " the host IP address can also be specified through 'XHOST'"
  " environment variables and configuration files.", envvar='XHOST')
@click.option('-p', '--port', help='Port number to use for connection. In addition,'
  " the port number can also be specified by means of 'XHOST'"
  ' environment variables and configuration files.', envvar='XPORT', type=int)

@click.option('-u', '--user'    , help='User name to connect to the database.')
@click.option('-d', '--database', help='The name of the database to be connected.')
@click.option('-w', '--passwd'  , help='Password to connect to the database.')
@click.option('-v', '--version' , help='Output xgcli\'s version.', is_flag=True)
@click.option('--ssh/--no-ssh'  , help='Enable secure encrypted connection,'
  ' this feature is currently not supported.', default=False)

@click.option('--charset', help='Character set for xugusql session.'
  ' UTF-8 character set is used by default.', default='utf8')
def client(host, port, database, user, passwd, ssh, version, charset):
    """A xugusql terminal client with syntax highlighting and auto-completion.

    \b    
    Examples:
        - xgcli -h '127.0.0.1' -p 5138 -d 'SYSTEM' -u 'SYSDBA'
    """
    cli = XCli(host=host, port=port, database=database, user=user, 
               passwd=passwd, charset=charset)
    cli.z_version(version)
        
    pmp = {
        'host': 'Please input server URL',
        'port': 'Please input server port',
        'user': 'Please input user name',
        'database': 'Please input database name',
        'password': 'Please input password',
    }

    options = cli.z_parse_opts()
    if len(options) > 0:
        click.secho(" ") 
        click.secho("XGDBMS Terminal Client", fg='green')
        click.secho("Copyright (c) 2002, 2021, Xugu.  All rights reserved.", fg='green')
        click.secho(" ") 

        for key, value in options.items():
            if key == 'password':
                cli.options[key] = click.prompt(pmp[key], type=str, hide_input=True)
                continue
            cli.options[key] = click.prompt(pmp[key], type=str)

    print(cli.options)

if __name__ == '__main__':
    client()

