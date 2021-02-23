from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.shortcuts import PromptSession
from prompt_toolkit.completion import WordCompleter,Completer,Completion
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from prompt_toolkit.styles import Style
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from pygments.lexers.sql import SqlLexer
from pygments.styles import get_style_by_name

session = PromptSession()
mycompleter = WordCompleter(['SELECT','SEQUENCE', 'T1', 'T2', 'T3', 'T4', 'T5'])

class CusCompleter(Completer):
    def get_completions(self, document, completion_event):
        yield Completion('SELECT', start_position=0, style='bg:ansiyellow fg:ansiblack')

#style = style_from_pygments_cls(get_style_by_name('native'))
style = Style.from_dict({
    'name' : 'ansigreen',
    'user' : '#FFFFFF',
    'at'   : '#FFFFFF',
    'host' : '#FFFFFF',
    'pmt'  : '#FFFFFF',
    '' : '#aaaaaa',
    'bottom': 'bg:#222222 #aaaaaa',
})

#def bottom_toolbar():
#    return [('class:bottom', '[F4] Print Help  xugu database console')]
bottom_toolbar = [('class:bottom', '[F4] Print Help  xugu database console')]

xprompt = [
        ('class:name', 'xugusql '),
        ('class:user', 'root'),
        ('class:at', '@'),
        ('class:host', '127.0.0.1'),
        ('class:pmt', '> '),
]

while True:
    text = session.prompt(xprompt, lexer=PygmentsLexer(SqlLexer), \
                style=style, completer=mycompleter, auto_suggest=AutoSuggestFromHistory(), \
                bottom_toolbar=bottom_toolbar) 
    if text == 'exit':
        break
    print('%s' % text)

