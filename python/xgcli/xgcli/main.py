
import click
import threading
import sys
import getpass
import os
import pygments.styles


from .xcompleter import SQLCompleter
from .xtoolbar import xbottom_toolbar, xbottom_binding, cli_multiline 
from .xsqlexer import XgCliLexer

from configobj import ConfigObj
from prompt_toolkit.completion import DynamicCompleter
from prompt_toolkit.shortcuts import PromptSession
from prompt_toolkit.styles import Style, merge_styles
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.styles.pygments import style_from_pygments_cls

class XCli(object):
    
    options = {
        'host' : None,
        'port' : None,
        'database' : None,
        'user': None,
        'password': None,
        'charset': None,
        'name': None,

        'login' : {
            'cnf' : None,
            'user' : None,
            'home' : None,
        }
    }
 
    version = '2.0.2'

    def __init__(self, host=None, port=None, database=None, user=None, 
                        passwd=None, charset=None):
        '''XCli's constructor'''
        self.options['login']['user'] = getpass.getuser()
        self.options['login']['home'] = os.environ.get('HOME')
        self.options['login']['cnf'] = os.path.expanduser('~/.xgclirc') 

        self.options['host'] = host
        self.options['port'] = port
        self.options['database'] = database
        self.options['user'] = user
        self.options['password'] = passwd
        self.options['charset'] = charset
        self.options['name'] = 'xgcli'

        self.completer = SQLCompleter(with_completion=True)
        self._completer_lock = threading.Lock() 
        self.xprompt = None
        self.multi_line = False
        self.multi_continuation = '\>'

    def xversion(self, isecho):
        ''' Need to print the version number of the current program? '''
        if isecho:
            click.secho('%s' % self.version, fg='green')
            sys.exit(0) 

    def xparse_opts(self):
        '''Analyze the user's input parameter options. 
           If there are default parameter options, the program will 
           actively read the content in the ~/.xgclirc configuration 
           file.
        '''
        cobj = ConfigObj(self.options['login']['cnf'], 
                list_values=True, interpolation=False, encoding='UTF-8')
        cobjks = cobj.keys()
        optsks = self.options.keys()
        def get(opt):
            if opt in cobjks and cobj[opt]:
                self.options[opt] = cobj[opt]
            return self.options[opt] 
 
        return {x: get(x) for x in optsks if not self.options[x]}

    def xlogin(self, prompt='\\l \\u@\\h:\\d> '):
        user = self.options['login']['user'] or '(none)'
        host = self.options['host'] or '(none)'
        dbname = self.options['database'] or '(none)'
        name = self.options['name']

        prompt = prompt.replace('\\l', name) 
        prompt = prompt.replace('\\u', user.lower())
        prompt = prompt.replace('\\h', host)
        prompt = prompt.replace('\\d', dbname.lower())
        prompt = prompt.replace('\\_', ' ')
        return ANSI(prompt)

    def doexec(self):
        """Entrance of the client terminal program"""
        def exec():
            try:
                text = self.xprompt.prompt()
            except KeyboardInterrupt:
                return
          
            if len(text) < 7 and ''.join(text.lower().split()) in ['quit;', 'exit;']:
                click.secho('See you again!', fg='green')
                sys.exit(0)

        def continuation(width, *_):
            if self.multi_continuation == '':
                pmp = ''
            elif self.multi_continuation:
                left = width - len(self.multi_continuation)
                pmp = " " * max((left - 1), 0) + self.multi_continuation + " "  
            else:
                pmp = ""

            return [('class:continuation', pmp)]

        print("")
        print("Welcome to use xugu database products.")
        print("Successfully connect to %s:%s %s as %s" %(self.options['host'], 
               self.options['port'], self.options['database'], self.options['user']))
        print("%s: %s" %(self.options['name'], self.version))
        print('Home: http://www.xugucn.com/')
        print("")

        bar = xbottom_toolbar(self)
        binding = xbottom_binding(self)

        def xstyle():
            elem = [ 
                    ('completion-menu.completion.current', 'bg:#ffffff #000000'),
                    ('completion-menu.completion', 'bg:#008888 #ffffff'),
                    ('completion-menu.meta.completion.current', 'bg:#44aaaa #000000'),
                    ('completion-menu.meta.completion', 'bg:#448888 #ffffff'),
                    ('completion-menu.multi-column-meta', 'bg:#aaffff #000000'),
                    ('scrollbar.arrow', 'bg:#003333'),
                    ('scrollbar', 'bg:#00aaaa'),
                    ('selected', '#ffffff bg:#6666aa'),
                    ('search', '#ffffff bg:#4444aa'),
                    ('output.header', '#00ff5f bold'),
                    ('output.odd-row', ''),
                    ('output.even-row', ''),
                    ('output.null', '#808080'),
                    ('search.current', '#ffffff bg:#44aa44'),
                    ('bottom-toolbar', 'bg:#222222 #aaaaaa'),
                    ('bottom-toolbar.off', 'bg:#222222 #888888'),
                    ('bottom-toolbar.on', 'bg:#222222 #ffffff'),
                    ('bottom-toolbar.transaction.valid', 'bg:#222222 #00ff5f bold'),
                    ('bottom-toolbar.transaction.failed', 'bg:#222222 #ff005f bold'),
                    ('search-toolbar', 'noinherit bold'),
                    ('search-toolbar.text', 'nobold'),
                    ('system-toolbar', 'noinherit bold'),
                    ('arg-toolbar', 'noinherit bold')]

            style = pygments.styles.get_style_by_name('default')
            override_style = Style([('bottom-toolbar', 'noreverse')])
            
            return merge_styles([style_from_pygments_cls(style),
                              override_style,
                              Style(elem)])

        self.xprompt = PromptSession(
                            message = self.xlogin(),
                            lexer = PygmentsLexer(XgCliLexer),
                            completer = DynamicCompleter(lambda: self.completer),
                            bottom_toolbar = bar,
                            style = xstyle(),
                            prompt_continuation = continuation,
                            key_bindings = binding,
                            multiline = cli_multiline(self),
                            complete_while_typing=True,
                            include_default_pygments_style=False, 
        )
        
        try:
            while True:
                exec()
        except EOFError:
            click.secho('See you again!', fg='green')
         


@click.command()
@click.option('-h', '--host', help='Host address of the database. In addition,'
    " the host IP address can also be specified through 'XHOST'"
    " environment variables and configuration files.", envvar='XHOST')
@click.option('-p', '--port', help='Port number to use for connection.'
    " In addition, the port number can also be specified by means of 'XHOST'"
    ' environment variables and configuration files.', envvar='XPORT', type=int)

@click.option('-u', '--user'    , help='User name to connect to the database.')
@click.option('-d', '--database', help='The name of the database to be connected.')
@click.option('-w', '--passwd'  , help='Password to connect to the database.')
@click.option('-v', '--version' , help='Output xgcli\'s version.', is_flag=True)
@click.option('--ssh/--no-ssh'  , help='Enable secure encrypted connection,'
    ' this feature is currently not supported.', default=False)

@click.option('--charset', help='Character set for xugusql session. UTF-8'
    ' character set is used by default.', default='utf8')
def client(host, port, database, user, passwd, ssh, version, charset):
    """A xugusql terminal client with syntax highlighting and auto-completion.

    \b    
    Examples:
        - xgcli -h '127.0.0.1' -p 5138 -d 'SYSTEM' -u 'SYSDBA'
         ____ ____ ________  ________ _____ _____
        |    |    /        |/        |     |     |
         \       /    |____|    _____|     |_____|
         /       \    |_   |         |     |     |
        |____|____\________|\________|_____|_____|
  
    """
    cli = XCli(host=host, port=port, database=database, user=user, 
               passwd=passwd, charset=charset)
    cli.xversion(version)
        
    pmp = {
        'host': 'Please input server URL',
        'port': 'Please input server port',
        'user': 'Please input user name',
        'database': 'Please input database name',
        'password': 'Please input password',
    }

    options = cli.xparse_opts()
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

    if sys.stdin.isatty():
        cli.doexec()
 

if __name__ == '__main__':
    client()

