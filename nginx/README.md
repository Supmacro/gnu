
# location
```
location [ = | ~ | ~* | ^~ | @ ] /uri/ {...}
```
There are two types of matching strings: literal string and regular expression, where '\~' and '\~\*' 
are used for regular expressions, and other prefixes and no prefixes are used for normal strings.

## rule
1. Match the ordinary string first, and store the most accurate match temporarily.
2. Then perform regular expression matching according to the declaration order in the configuration file. 
    As long as a regular expression is matched, the matching will stop, and the regular expression will 
    be used as the matching result.
3. If all regular expressions fail to match, the result stored in 1 is taken.
4. If neither the normal string nor the regular expression can match, a general match is performed.

```
    =       Exact prefix matching, only an exact match can take effect.
    ^~      Regular matching will not be performed after ordinary string matching.
    ~       Case-sensitive regular matching.
    ~*      Case-insensitive regular matching.
    /uri    Without any modifier, it means prefix match.
    /       General matching, any request that does not match other 'locations' will be matched
```

