
from prompt_toolkit.completion import Completer, Completion

from .xparser import plast_word 

class SQLCompleter(Completer):
    keywords = ['ABORT', 'ABOVE', 'ABSOLUTE', 'ACCESS', 'ACCOUNT', 'ACTION', 'ADD',
                'AFTER', 'ALL', 'ALTER', 'ANALYSE', 'AND', 'ANY', 'AOVERL', 'APS',
                'APPEND', 'ARCHIVELOG', 'ARE', 'ARRAY', 'AS', 'ASC', 'AT', 'AUDIT', 
                'AUDITOR', 'AUTHID', 'AUTHORIZATION', 'AUTO', 'BACKUP', 'BACKWARD',
                'BADFILE', 'BCONTAINS', 'BEFORE', 'BEGIN', 'BETWEEN', 'BINARY', 
                'BINTERSECTS', 'BIT', 'BLOCK', 'BLOCKS', 'BODY', 'BOTH', 'BOUND', 
                'BOVERLAPS', 'BREAK', 'BUFFER_POOL', 'BUILD', 'BULK', 'BWITHIN', 'BY', 
                'CACHE', 'CALL', 'CASCADE', 'CASE', 'CAST', 'CATCH', 'CATEGORY', 
                'CHAIN', 'CHAR', 'CHARACTER', 'CHARACTERISTICS', 'CHECK', 'CHECKPOINT',
                'CHUNK', 'CLOSE', 'CLUSTER', 'COALESCE', 'COLLATE', 'COLLECT', 'COLUMN',
                'COMMENT', 'COMMIT', 'COMMITTED', 'COMPLETE', 'COMPRESS', 'COMPUTE', 
                'CONNECT', 'CONSTANT', 'CONSTRAINT', 'CONSTRAINTS', 'CONSTRUCTOR', 
                'CONTAINS', 'CONTEXT', 'CONTINUE', 'COPY', 'CORRESPONDING', 'CREATE',
                'CREATEDB', 'CREATEUSER', 'CROSS', 'CROSSES', 'CUBE', 'CURRENT',
                'CURSOR', 'CYCLE', 'DATABASE', 'DATAFILE', 'DATE', 'DATETIME', 'DAY',
                'DBA', 'DEALLOCATE', 'DEC', 'DECIMAL', 'DECLARE', 'DECODE', 'DECRYPT',
                'DEFAULT', 'DEFERRABLE', 'DEFERRED', 'DELETE', 'DELIMITED', 
                'DELIMITERS', 'DEMAND', 'DESC', 'DESCRIBE', 'DETERMINISTIC', 'DIR', 
                'DISABLE', 'DISASSEMBLE', 'DISCORDFILE', 'DISJOINT', 'DISTINCT', 'DO', 
                'DOMAIN', 'DOUBLE', 'DRIVEN', 'DROP', 'EACH', 'ELEMENT', 'ELSE', 
                'ELSEIF', 'ELSIF', 'ENABLE', 'ENCODING', 'ENCRYPT', 'ENCRYPTOR', 'END',
                'ENDCASE', 'ENDFOR', 'ENDIF', 'ENDLOOP', 'EQUALS', 'ESCAPE', 'EVERY', 
                'EXCEPT', 'EXCEPTION', 'EXCEPTIONS', 'EXCLUSIVE', 'EXEC', 'EXECUTE', 
                'EXISTS', 'EXIT', 'EXPIRE', 'EXPLAIN', 'EXPORT', 'EXTEND', 'EXTERNAL',
                'EXTRACT', 'FALSE', 'FAST', 'FETCH', 'FIELD', 'FIELDS', 'FILTER', 
                'FINAL', 'FINALLY', 'FIRST', 'FLOAT', 'FOLLOWING', 'FOR', 'FORALL',
                'FORCE', 'FOREIGN', 'FORWARD', 'FOUND', 'FREELIST', 'FREELISTS', 
                'FROM', 'FULL', 'FUNCTION', 'GENERATED', 'GET', 'GLOBAL', 'GOTO',
                'GRANT', 'GREATEST', 'GROUP', 'GROUPING', 'GROUPS', 'HANDLER', 'HASH',
                'HAVING', 'HEAP', 'HIDE', 'HOTSPOT', 'HOUR', 'IDENTIFIED', 'IDENTIFIER',
                'IDENTITY', 'IF', 'ILIKE', 'IMMEDIATE', 'IMPORT', 'IN', 'INCLUDE',
                'INCREMENT', 'INDEX', 'INDEXTYPE', 'INDICATOR', 'INDICES', 'INHERITS',
                'INIT', 'INITIAL', 'INITIALLY', 'INITRANS', 'INNER', 'INOUT', 
                'INSENSITIVE', 'INSERT', 'INSTANTIABLE', 'INSTEAD', 'INTERSECT', 'IO',
                'INTERSECTS', 'INTERVAL', 'INTO', 'IS', 'ISNULL', 'ISOLATION', 'ISOPEN',
                'JOB', 'JOIN', 'KEEP', 'KEY', 'KEYSET', 'LABEL', 'LANGUAGE', 'LAST',
                'LEADING', 'LEAST', 'LEAVE', 'LEFT', 'LEFTOF', 'LENGTH', 'LESS',
                'LEVEL', 'LEVELS', 'LEXER', 'LIBRARY', 'LIKE', 'LIMIT', 'LINK', 'LIST',
                'LISTEN', 'LOAD', 'LOB', 'LOCAL', 'LOCATION', 'LOCATOR', 'LOCK',
                'LOGFILE', 'LOGGING', 'LOGIN', 'LOGOUT', 'LOOP', 'LOVERLAPS', 'MATCH',
                'MATERIALIZED', 'MAX', 'MAXEXTENTS', 'MAXSIZE', 'MAXTRANS', 'MAXVALUE',
                'MAXVALUES', 'MEMBER', 'MEMORY', 'MERGE', 'MINEXTENTS', 'MINUS',
                'MINUTE', 'MINVALUE', 'MISSING', 'MODE', 'MODIFY', 'MONTH', 'MOVEMENT',
                'NAME', 'NAMES', 'NATIONAL', 'NATURAL', 'NCHAR', 'NESTED', 'NEWLINE',
                'NEW', 'NEWLINE', 'NEXT', 'NO', 'NOARCHIVELOG', 'NOAUDIT', 'NOCACHE',
                'NOCOMPRESS', 'NOCREATEDB', 'NOCREATEUSER', 'NOCYCLE', 'NODE', 'NOFORCE',
                'NOFOUND', 'NOLOGGING', 'NONE', 'NOORDER', 'NOPARALLEL', 'NOT', 
                'NOTFOUND', 'NOTHING', 'NOTIFY', 'NOTNULL', 'NOVALIDATE', 'NOWAIT', 
                'NULL', 'NULLIF', 'NULLS', 'NUMBER', 'NUMERIC', 'NVARCHAR', 'NVL2',
                'NVL', 'NVARCHAR2', 'OBJECT', 'OF', 'OFF', 'OFFLINE', 'OFFSET',
                'OIDINDEX', 'OIDS', 'OLD', 'ON', 'ONLINE', 'ONLY', 'OPEN', 'OPERATOR',
                'OPTION', 'OR', 'ORDER', 'ORGANIZATION', 'OTHERVALUES', 'OUT', 'OUTER', 
                'OVER', 'OVERLAPS', 'OWNER', 'PACKAGE', 'PARALLEL', 'PARAMETERS',
                'PARTIAL', 'PARTITION', 'PARTITIONS', 'PASSWORD', 'PCTFREE', 'PCTINCREASE',
                'PCTUSED', 'PCTVERSION', 'PERIOD', 'POLICY', 'PRAGMA', 'PREBUILT', 
                'PRECEDING', 'PRECISION', 'PREPARE', 'PRESERVE', 'PRIMARY', 'PRIOR',
                'PRIORITY', 'PRIVILEGES', 'PROCEDURAL', 'PROCEDURE', 'PROTECTED', 'PUBLIC',
                'QUERY', 'QUOTA', 'RAISE', 'RANGE', 'RAW', 'READ', 'READS', 'REBUILD',
                'RECOMPILE', 'RECORD', 'RECORDS', 'RECYCLE', 'REDUCED', 'REFERENCES',
                'REF', 'REFERENCING', 'REFRESH', 'REINDEX', 'RELATIVE', 'RENAME',
                'REPEATABLE', 'REPLACE', 'REPLICATION', 'RESOURCE', 'RESTART', 'RESTORE',
                'RESTRICT', 'RESULT', 'RETURN', 'RETURNING', 'REVERSE', 'REVOKE', 
                'REWRITE', 'RIGHT', 'RIGHTOF', 'ROLE', 'ROLLBACK', 'ROLLUP', 'ROVERLAPS',
                'ROW', 'ROWCOUNT', 'ROWID', 'ROWS', 'ROWTYPE', 'RULE', 'RUN', 'SAVEPOINT',
                'SCHEMA', 'SCROLL', 'SECOND', 'SEGMENT', 'SELECT', 'SELF', 'SEQUENCE', 
                'SERIALIZABLE', 'SESSION', 'SET', 'SETOF', 'SETS', 'SHARE', 'SHOW', 
                'SHUTDOWN', ' SIBLINGS', 'SIZE', 'SLOW', 'SNAPSHOT', 'SOME', 'SPATIAL',
                'SPLIT', 'SSO', 'STANDBY', 'START', 'STATEMENT', 'STATIC', 'STATISTICS',
                'STEP', 'STOP', 'STORAGE', 'STORE', 'STREAM', 'SUBPARTITION', 
                'SUBPARTITIONS', 'SUBTYPE', 'SUCCESSFUL', 'SYNONYM', 'SYSTEM', 'TABLE',
                'TABLESPACE', 'TEMP', 'TEMPLATE', 'TEMPORARY', 'TERMINATED', 'THAN',
                'THEN', 'THROW', 'TIME', 'TIMESTAMP', 'TO', 'TOP', 'TOPOVERLAPS', 
                'TOUCHES', 'TRACE', 'TRAILING', 'TRAN', 'TRANSACTION', 'TRIGGER', 'TRUE',
                'TRUNCATE', 'TRUSTED', 'TRY', 'TYPE', 'UNBOUNDED', 'UNDER', 'UNDO', 
                'UNIFORM', 'UNION', 'UNIQUE', 'UNLIMITED', 'UNLISTEN', 'UNLOCK', 
                'UNPROTECTED', 'UNTIL', 'UOVERLAPS', 'UPDATE', 'USE', 'USER', 'USING',
                'VACUUM', 'VALID', 'VALIDATE', 'VALUE', 'VALUES', 'VARCHAR', 'VARCHAR2', 
                'VARRAY', 'VARYING', 'VERBOSE', 'VERSION', 'VIEW', 'VOCABLE', 'WAIT',
                'WHEN', 'WHENEVER', 'WHERE', 'WHILE', 'WITH', 'WITHIN', 'WITHOUT',
                'WORK', 'WRITE', 'XML', 'YEAR', 'ZONE']

    functions = ['AVG', 'COUNT'] 
    
    def __init__(self, with_completion=True, keyword_casing='auto'):
        super(self.__class__, self).__init__()
        self.with_completion = with_completion
        self.unrepeat_words = set()
        for x in self.keywords:
            self.unrepeat_words.update(x.split())
        self.reset_completions()

    def reset_completions(self):
        self.all_completions = set(self.keywords + self.functions)

    @staticmethod
    def match_word(text, words, word_case=None, with_completion=True):
        """
            Given the user's input text and a collection of available completions,
            find completions matching the last word of the text.
        """
        word = plast_word(text)
        text = word.lower()        

        completions = []
        if with_completion and word != '':
            for x in sorted(words):
                index = x.lower().find(text, 0, len(x))
                if index == 0:
                    completions.append((len(text), index, x))
        
        if word_case == 'auto':
            word_case = 'lower' if word and word[-1].islower() else 'upper'
        def smart_case(alpha):
            if word_case == 'upper':
                return alpha.upper()
            else:
                return alpha.lower()

        return (Completion(c if word_case is None else smart_case(c), -len(text))
                    for a, b, c, in sorted(completions)) 
                
    def get_completions(self, document, complete_event):
        wbc = document.get_word_before_cursor(WORD=True)
        return self.match_word(wbc, self.all_completions, \
                         with_completion=self.with_completion)

