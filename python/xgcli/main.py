
import click
import sys

class XCli(object):
    version = '0.0.0'
    
    def __init__(self, host=None, port=5138, database=None, user=None, passwd=None, 
                        charset='UTF8'):
        pass
    def isecho_version(self, isecho):
        if isecho:
            click.secho('%s' % self.version, fg='green')
            sys.exit(0) 


@click.command()
@click.option('-h', '--host', envvar='XHOST', type=str, help='Host address of the database.'
                             '\'XHOST\' environment variable will be read by default.')
@click.option('-p', '--port', envvar='XPORT', default=5138, type=int, 
                   help='Port number to use for connection. '
                        '\'XPORT\' environment variable will be read by default.')
@click.option('-u', '--user', type=str, help='User name to connect to the database.')
@click.option('-d', '--database', type=str, help='The name of the database to be connected.')
@click.option('-w', '--passwd', type=str, help='Password to connect to the database.')
@click.option('-v', '--version' , is_flag=True,  help='Output xgcli\'s version.\n')

@click.option('--ssh/--no-ssh', default=False, help='Enable secure encrypted connection, '
                                        'this feature is currently not supported')
@click.option('--charset', default='utf8', type=str, 
                   help='Character set for xugusql session. '
                        'UTF-8 character set is used by default')
def client(host, port, database, user, passwd, ssh, version, charset):
    """A xugusql terminal client with auto-completion and syntax highlighting.
    
    \b
    Examples:
        - xgcli -h '127.0.0.1' -d 'SYSTEM' -u 'SYSDBA'
    """
    xobj = XCli(host=host, port=port, 
                  database=database, user=user, 
                  passwd=passwd, charset=charset)
    xobj.isecho_version(version)
    

if __name__ == '__main__':
    client()

