from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
                            Number, Operator, Generic

from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

completer = NestedCompleter.from_nested_dict({
    'show':{
        'version' : None,
        'clock' : None,
        'ip' : {
            'interface' : {'brief'}
        },
    },
    'exit' : None,
})

while True:
    text = prompt('> ', completer=completer, complete_while_typing=True)
    if text == 'exit' :
        break

