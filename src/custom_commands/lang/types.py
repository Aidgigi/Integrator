import enum

class LexTypes(enum.Enum):
    # Variable Types
    VarType             = 'var'
    LetKeyword          = 'let'
    ConstKeyword        = 'const'

    # Control Flow
    IfKeyword           = 'if'
    ElseKeyword         = 'else'
    ElifKeyword         = 'elif'
    ForKeyword          = 'for'
    WhileKeyword        = 'while'
    BreakKeyword        = 'break'
    ContinueKeyword     = 'cont'

    # Simple Operators
    Set                 = '='
    Add                 = '+'
    AddSet              = '+='
    Sub                 = '-'
    SubSet              = '-='
    Mult                = '*'
    MultSet             = '*='
    Div                 = '/'
    DivSet              = '/='
    Mod                 = '%'
    ModSet              = '%='

    # Boolean Operators
    IsEqu               = '=='
    Not                 = '!'
    Or                  = '|'
    And                 = '&'
    Less                = '<'
    LessEqu             = '<='
    Greater             = '>'
    GreaterEqu          = '>='

    # Literals
    NumLiteral          = 'NUM'
    StringLiteral       = 'STRING'
    CharLiteral         = 'CHAR'
    BooleanLiteral      = 'BOOL'
    IDLiteral           = 'ID'
    NoneLiteral         = 'NONE'

    # Syntax 
    OpenBrace           = '['
    OpenParen           = '('
    OpenCurl            = '{'
    CloseBrace          = ']'
    CloseParen          = ')'
    CloseCurl           = '}'
    Quote               = '"'
    EscapeChar          = '\\'
    Comma               = ','
    Colon               = ':'
    Semicolon           = ';'
    Dot                 = '.'

    Other               = 'OTHER'

class Types(enum.Enum):
    string              = 'str'
    character           = 'char' 
    number              = 'Num'
    boolean             = 'bool'

class DiscordTypes(enum.Enum):
    user                = 'usr'
    server              = 'svr'
    channel             = 'ch'
    # IDK how to implement something to create a thread
    thread              = 'th'
    message             = 'msg'
    embed               = 'ebd'
