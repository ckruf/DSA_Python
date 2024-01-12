class Empty(Exception):
  pass

class ArrayStack:

  def __init__(self):
    self._data = []

  def push(self, value):
    self._data.append(value)

  def pop(self):
    if len(self._data) > 0:
      return self._data.pop()
    else:
      raise Empty("Can't pop from empty stack")
    
  def top(self):
    if len(self._data) > 0:
      return self._data[-1]
    else:
      raise Empty("Stack is empty")
    
  def is_empty(self):
    return len(self._data) == 0
  
  def __len__(self):
    return len(self._data)
  



def is_matched(expr: str) -> bool:
  """
  Given an arithmetic expression in the form of the string, such as '[(x+y)-(3x+2y)]',
  determine whether all delimiters properly match. Return True if they do and False otherwise.
  """
  lefty = "{(["
  righty = "})]"

  stack = ArrayStack()

  for symbol in expr:
    if symbol in lefty:
      stack.push(symbol)
    elif symbol in righty:
      if stack.is_empty():
        return False
      if righty.index(symbol) != lefty.index(stack.pop()):
        return False
      
  return stack.is_empty()


def is_matched_html(raw: str) -> bool:
  """
  Given a raw string representing HTML, determine whether all the tags are properly matched.
  Return True if they are and False otherwise.
  """
  stack = ArrayStack()
  opening_tag_index = raw.find("<")

  # .find() returns - 1 when not found
  while opening_tag_index != -1:

    closing_tag_index = raw.find(">", opening_tag_index)
    if closing_tag_index == -1:
      return False
    tag = raw[opening_tag_index+1:closing_tag_index]
    
    # opening tag
    if not tag.startswith("/"):
      stack.push(tag)
    # closing tag
    else:
      if stack.is_empty():
        return False
      elif stack.pop() != tag[1:]:
        return False
    
    opening_tag_index = raw.find("<", closing_tag_index + 1)


  return stack.is_empty()


def test_is_matched_html_pass():
  """
  Test function for is_matched_html(), with a valid HTML string
  """
  matched_html = """
  <html>
    <body>
      <h1>Hello, world</h1>
      <p>Lorem ipsum doloraes</p>
    </body>
  </html>
  """
  assert is_matched_html(matched_html)
  print("test passed")


def test_is_matched_html_fail_non_matching():
  """
  Test function for is_matched_html(), with HTML string which is invalid
  because opening and closing tags do not match (<h1></h2>)
  """
  mismatched_html = """
  <html>
    <body>
      <h1>Hello, world</h2>
      <p>Lorem ipsum doloraes</p>
    </body>
  </html>
  """
  assert is_matched_html(mismatched_html) is False
  print("test passed")


def test_is_matched_html_fail_missing_matching():
  """
  Test with HTML string which is invalid because of a missing closing HTML tag (<html>)
  """
  missing_matching_html = """
  <html>
    <body>
      <h1>Hello, world</h2>
      <p>Lorem ipsum doloraes</p>
    </body>
  """
  assert is_matched_html(missing_matching_html) is False
  print("test passed")


def test_is_matched_html_fail_tag_unclosed():
  """
  Test with HTML string which is invalid because of an unclosed HTML tag(<p ).
  """
  missing_matching_html = """
  <html>
    <body>
      <h1>Hello, world</h2>
      <p Lorem ipsum doloraes</p>
    </body>
  """
  assert is_matched_html(missing_matching_html) is False
  print("test passed")

def test_is_matched_html_fail_tag_unclosed_no_space():
  """Same as test above, but no space after p"""
  missing_matching_html = """
  <html>
    <body>
      <h1>Hello, world</h2>
      <pLorem ipsum doloraes</p>
    </body>
  """
  assert is_matched_html(missing_matching_html) is False
  print("test passed")


  

if __name__ == "__main__":
  test_is_matched_html_pass()
  test_is_matched_html_fail_non_matching()
  test_is_matched_html_fail_missing_matching()
  test_is_matched_html_fail_tag_unclosed()
  test_is_matched_html_fail_tag_unclosed_no_space()
