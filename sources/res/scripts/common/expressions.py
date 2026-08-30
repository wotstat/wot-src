from soft_exception import SoftException
import cStringIO, tokenize, token

class ParserException(SoftException):

    def __init__(self, message):
        super(ParserException, self).__init__(message)
        return


class _Tokenizer:

    def __init__(self, s):
        self.tokenizer = tokenize.generate_tokens(cStringIO.StringIO(s).readline)
        self.__currentToken = None
        return

    def __next(self):
        try:
            while True:
                toknum, tokval, _, _, _ = self.tokenizer.next()
                self.__currentToken = (toknum, tokval)
                if toknum not in (tokenize.NL, token.NEWLINE, token.INDENT, token.DEDENT):
                    break

        except StopIteration:
            self.__currentToken = None

        return

    def peek(self):
        if self.__currentToken is None:
            self.__next()
        return self.__currentToken

    def match(self, toknum, tokval=None):
        if self.__currentToken is None:
            self.__next()
        currentToken = self.__currentToken
        if currentToken is None or toknum != currentToken[0]:
            raise ParserException(b'unexpected token %s "%s", expected %s' % (
             token.tok_name[currentToken[0]], currentToken[1],
             token.tok_name[toknum]))
        if tokval is not None and tokval != currentToken[1]:
            raise ParserException(b'unexpected token %s "%s", expected %s "%s"' % (
             token.tok_name[currentToken[0]], currentToken[1],
             token.tok_name[toknum], tokval))
        self.__currentToken = None
        return currentToken[1]


class ExpressionParser(object):
    _CMP_OPERATORS = {b'==': (lambda left, right: (lambda context: left(context) == right(context))), 
       b'!=': (lambda left, right: (lambda context: left(context) != right(context))), 
       b'<': (lambda left, right: (lambda context: left(context) < right(context))), 
       b'<=': (lambda left, right: (lambda context: left(context) <= right(context))), 
       b'>': (lambda left, right: (lambda context: left(context) > right(context))), 
       b'>=': (lambda left, right: (lambda context: left(context) >= right(context)))}
    _SUM_OPERATORS = {b'+': (lambda left, right: (lambda context: left(context) + right(context))), 
       b'-': (lambda left, right: (lambda context: left(context) - right(context)))}

    def __init__(self):
        self.tokens = set()
        return

    def parseExpression(self, s):
        tokenizer = _Tokenizer(s.strip())
        expression = self._parseExpression(tokenizer)
        tokenizer.match(token.ENDMARKER)
        return (expression, self.tokens)

    def _parseOperator(self, tokenizer, operators):
        toknum, tokval = tokenizer.peek()
        if toknum == token.OP and tokval in operators:
            self._processToken(tokval)
            tokenizer.match(toknum)
            return operators[tokval]
        else:
            return
            return

    def _parseExpression(self, tokenizer):
        return self._parseOrExpression(tokenizer)

    def _parseOrExpression(self, tokenizer):
        left = self._parseAndExpression(tokenizer)
        toknum, tokval = tokenizer.peek()
        if toknum == token.NAME and tokval == b'or':
            self._processToken(tokval)
            tokenizer.match(token.NAME)
            right = self._parseOrExpression(tokenizer)
            return (lambda context: left(context) or right(context))
        else:
            if tokval == b'if':
                tokenizer.match(token.NAME)
                condition = self._parseCondition(tokenizer)
                tokenizer.match(token.NAME)
                right = self._parseExpression(tokenizer)
                return (lambda context: left(context) if condition(context) else right(context))
            return left

        return

    def _parseAndExpression(self, tokenizer):
        left = self._parseCondition(tokenizer)
        toknum, tokval = tokenizer.peek()
        if toknum == token.NAME and tokval == b'and':
            self._processToken(tokval)
            tokenizer.match(token.NAME)
            right = self._parseAndExpression(tokenizer)
            return (lambda context: left(context) and right(context))
        else:
            return left

        return

    def _parseCondition(self, tokenizer):
        toknum, tokval = tokenizer.peek()
        if toknum == token.NAME and tokval == b'not':
            tokenizer.match(token.NAME, b'not')
            expression = self._parseCondition(tokenizer)
            return (lambda context: not expression(context))
        else:
            left = self._parseSum(tokenizer)
            op = self._parseOperator(tokenizer, self._CMP_OPERATORS)
            if op is not None:
                right = self._parseSum(tokenizer)
                return op(left, right)
            return left
            return

    def _parseSum(self, tokenizer):
        toknum, tokval = tokenizer.peek()
        if toknum == token.OP and tokval == b'(':
            tokenizer.match(token.OP, b'(')
            expression = self._parseExpression(tokenizer)
            tokenizer.match(token.OP, b')')
            left = expression
        else:
            left = self._parseTerm(tokenizer)
        op = self._parseOperator(tokenizer, self._SUM_OPERATORS)
        if op is not None:
            right = self._parseSum(tokenizer)
            return op(left, right)
        else:
            return left
            return

    def _parseTerm(self, tokenizer):
        toknum, tokval = tokenizer.peek()
        if toknum == token.NAME:
            self.tokens.add(tokval)
            self._processToken(tokval)
            tokenizer.match(token.NAME)
            return (lambda context: context[tokval])
        if toknum == token.NUMBER:
            self._processToken(tokval)
            tokenizer.match(token.NUMBER)
            try:
                tokval = int(tokval)
            except ValueError:
                tokval = float(tokval)

            return (lambda context: tokval)
        if toknum == token.STRING:
            self._processToken(tokval)
            tokenizer.match(token.STRING)
            if tokval.startswith(b'"') and tokval.endswith(b'"') or tokval.startswith(b"'") and tokval.endswith(b"'"):
                tokval = tokval[1:-1].decode(b'string_escape')
            else:
                raise ParserException(b'unsupported string literal')
            return (lambda context: tokval)
        raise ParserException(b'expected term, but found %s (%s)' % (token.tok_name[toknum], tokval))
        return

    def _processToken(self, tokval):
        return


def parseExpression(condition):
    return ExpressionParser().parseExpression(condition)
