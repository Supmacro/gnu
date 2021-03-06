
import logging

from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.filters import Condition
from prompt_toolkit.application import get_app
from prompt_toolkit.filters import completion_is_selected
from prompt_toolkit.key_binding import KeyBindings

_logger = logging.getLogger(__name__)


def xbottom_toolbar(xgcli):
    """
    Return 
    a list that generates the toolbar tokens.
    """
    def xtoolbar():
        xbar = []
        xbar.append(('class:bottom-toolbar', ' '))

        toolbar = {
            'multi_line.on' : ('class:bottom-toolbar.on', '[F3] Multiline: ON  '),
            'multi_line.off': ('class:bottom-toolbar.off', '[F3] Multiline: OFF  '),
            'smart_completion.on' : ('class:bottom-toolbar.on', '[F2] Smart Completion: ON  '),
            'smart_completion.off': ('class:bottom-toolbar.off', '[F2] Smart Completion: OFF  '),
            'delimiter': ('class:bottom-toolbar', '[\';\'] will end the line  ')
        }

        if xgcli.completer.with_completion:
            xbar.append(toolbar['smart_completion.on'])
        else: 
            xbar.append(toolbar['smart_completion.off'])

        if xgcli.multi_line:
            xbar.append(toolbar['multi_line.on'])
        else:
            xbar.append(toolbar['multi_line.off'])

        return xbar

    return xtoolbar


def xbottom_binding(xgcli):
    """Custom key bindings for xgcli"""
    kb = KeyBindings()

    @kb.add('f2')
    def _(event):
        """Enable/Disable SmartCompletion Mode."""
        xgcli.completer.with_completion = not xgcli.completer.with_completion

    @kb.add('f3')
    def _(event):
        """Enable/Disable smartcompletions mode."""
        _logger.debug('Detected F3 key.')        

        xgcli.multi_line = not xgcli.multi_line

    @kb.add('tab')
    def _(event):
        """Force autocompletion at cursor"""
        _logger.debug('Detected <Tab> key.')        

        x = event.app.current_buffer
        if x.complete_state:
            x.complete_next()
        else:
            x.start_completion(select_first=True)

    @kb.add('c-space')
    def _(event):
        """
        If the autocompletion menu is not showing, display it with the
        appropriate completions for the context.
        """
        _logger.debug('Detected <C-Space> key.')

        x = event.app.current_buffer
        if x.complete_state:
            x.complete_next()
        else:
            x.start_completion(select_first=False)

    @Condition
    def _enter():
        def delim(string):
            res = True

            if not string:
                return res

            slen = len(string) 
            j = -1
            while j+slen >= 0:
                if string[j] == ' ':
                    j -= 1
                    continue
                if string[j] == ';':
                    res = False
                break
            return res

        doc = get_app().layout.get_buffer_by_name(DEFAULT_BUFFER).document
        return True if delim(doc.text) else False             

    @kb.add('enter', filter=_enter)
    def _(event):
        event.app.current_buffer.insert_text('\n')
        xgcli.multi_line = True 
                

    @kb.add('enter', filter=completion_is_selected)
    def _(event):
        _logger.debug('Detected enter key.')

        event.current_buffer.complete_state = None
        x = event.app.current_buffer
        x.complete_state = None

    @kb.add('escape', 'enter')
    def _(event):
        """Introduces a line break regardless of multi-line mode or not."""
        _logger.debug('Detected alt-enter key.')
        event.app.current_buffer.insert_text('\n')
    
    return kb


def _mul_exec(text):
    origtext = text
    text = text.strip()

    if text.startswith('\\fs'):
        return origtext.endswitch('\n')

    return (

        text.startswith('\\') or
        text.lower().startswith('delimiter') or

        text.endswith(';') or
        text.endswith('\\g') or
        text.endswith('\\G') or
        text.endswith(r'\e') or
        text.endswith(r'\clip') or
        
        (text == 'exit') or
        (text == 'quit') or
        (text == ':q') or
        (text == '')
    )
    

def cli_multiline(xgcli):
    @Condition
    def rbool():
        doc = get_app().layout.get_buffer_by_name(DEFAULT_BUFFER).document
        
        if not xgcli.multi_line:
            return False
        else:
            return not _mul_exec(doc.text)
    return rbool;
